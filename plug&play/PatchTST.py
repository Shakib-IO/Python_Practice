"""PatchTST from https://github.com/yuqinie98/PatchTST"""
from torch import nn
import numpy as np
import torch 
import torch.nn.functional as F

class ProjectionLayer(nn.Module):
    def __init__(self, d, p, n):
        super(ProjectionLayer, self).__init__()
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # Initialize learnable parameters
        self.matrix1 = nn.Parameter(torch.randn(p, d)).to(device)
        self.matrix2 = nn.Parameter(torch.randn(n, d)).to(device)
        
    def forward(self, x):
        # Get the dimensions of the input tensor
        batch_size, seq, n, p = x.shape
        
        # Reshape the input tensor to (batch_size * seq, p, n)
        x = x.view(batch_size * seq, n, p)
        
        # Multiply the input tensor by matrix1 and add matrix2
        # print('haha', x.shape)
        # print('mama',self.matrix1.shape)
        # print('kaka', self.matrix2.shape)
        result = torch.matmul(x, self.matrix1) + self.matrix2
        
        # Reshape the result to (batch_size, seq, d, n)
        result = result.view(batch_size, seq, -1, result.size(-1))
        
        return result
    
class ExtendedMultiHeadAttentionWithFC(nn.Module):
    def __init__(self, d, h):
        super(ExtendedMultiHeadAttentionWithFC, self).__init__()
        self.d = d
        self.h = h
        self.d_head = d // h

        # Define the projection layers for queries, keys, and values
        self.query_projection = nn.Linear(d, d)
        self.key_projection = nn.Linear(d, d)
        self.value_projection = nn.Linear(d, d)

        # Define a linear layer to combine the multi-head outputs
        self.out_projection = nn.Linear(d, d)

        # Define batch normalization layers
        self.batch_norm1 = nn.BatchNorm2d(d)
        self.batch_norm2 = nn.BatchNorm2d(2*d)
        self.batch_norm3 = nn.BatchNorm2d(d)

        # Define fully connected layers
        self.fc1 = nn.Linear(d, 2 * d)
        self.fc2 = nn.Linear(2 * d, d)
        
        # Define activation function
        self.activation = nn.ReLU()

    def scaled_dot_product_attention(self, queries, keys, values):
        d_head = queries.size(-1)
        scores = torch.matmul(queries, keys.transpose(-2, -1)) / torch.sqrt(torch.tensor(d_head, dtype=torch.float32))
        attention_weights = F.softmax(scores, dim=-1)
        attention_output = torch.matmul(attention_weights, values)
        return attention_output, attention_weights


    def forward(self, x):
        b, m, n, d = x.shape

        # print('incoming shape', x.shape)
        # Project input tensor to queries, keys, and values
        queries = self.query_projection(x)  # Shape: (b, m, n, d)
        keys = self.key_projection(x)       # Shape: (b, m, n, d)
        values = self.value_projection(x)   # Shape: (b, m, n, d)

        # Reshape and transpose for multi-head attention
        queries = queries.view(b, m, n, self.h, self.d_head).transpose(2, 3)  # Shape: (b, m, h, n, d_head)
        keys = keys.view(b, m, n, self.h, self.d_head).transpose(2, 3)        # Shape: (b, m, h, n, d_head)
        values = values.view(b, m, n, self.h, self.d_head).transpose(2, 3)    # Shape: (b, m, h, n, d_head)

        # Calculate the attention output
        attention_output, _ = self.scaled_dot_product_attention(queries, keys, values)  # Shape: (b, m, h, n, d_head)

        # Concatenate the multi-head outputs
        attention_output = attention_output.transpose(2, 3).contiguous().view(b, m, n, d)  # Shape: (b, m, n, d)

        # Project the concatenated outputs
        attention_output = self.out_projection(attention_output)  # Shape: (b, m, n, d)

        # Add residual connection
        attention_output += x  # Shape: (b, m, n, d)

        # Perform batch normalization
        # Note: BatchNorm2d expects input of shape (batch_size, channels, height, width)
        # Reshape to (b, d, m, n) for batch normalization
        attention_output = attention_output.permute(0, 3, 1, 2)  # Shape: (b, d, m, n)
        attention_output = self.batch_norm1(attention_output)     # Shape: (b, d, m, n)
        
        # Reshape back to (b, m, n, d)
        attention_output = attention_output.permute(0, 2, 3, 1)  # Shape: (b, m, n, d)

        # print('after attention', attention_output.shape)
        # First fully connected layer with expansion
        fc1_output = self.fc1(attention_output)  # Shape: (b, m, n, 2d)
        fc1_output = self.activation(fc1_output)  # Apply activation
        fc1_output = fc1_output.permute(0, 3, 1, 2)  # Reshape for batch normalization
        fc1_output = self.batch_norm2(fc1_output)    # Apply batch normalization
        fc1_output = fc1_output.permute(0, 2, 3, 1)  # Reshape back

        # Second fully connected layer with shrinking
        fc2_output = self.fc2(fc1_output)  # Shape: (b, m, n, d)
        fc2_output = self.activation(fc2_output)  # Apply activation
        fc2_output = fc2_output.permute(0, 3, 1, 2)  # Reshape for batch normalization
        fc2_output = self.batch_norm3(fc2_output)    # Apply batch normalization
        fc2_output = fc2_output.permute(0, 2, 3, 1)  # Reshape back
        fc2_output += attention_output  # Add residual connection

        return fc2_output


class StackedMultiHeadAttentionModel(nn.Module):
    def __init__(self, d, h, num_layers=3):
        super(StackedMultiHeadAttentionModel, self).__init__()
        self.layers = nn.ModuleList([ExtendedMultiHeadAttentionWithFC(d, h) for _ in range(num_layers)])

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x


class FlattenAndFullyConnected(nn.Module):
    def __init__(self, n, d, z):
        super(FlattenAndFullyConnected, self).__init__()
        # Fully connected layer
        self.fc = nn.Linear(n * d, z)

    def forward(self, x):
        b, m, n, d = x.shape

        # Flatten the last two dimensions
        x = x.view(b, m, -1)  # Shape: (b, m, n * d)

        # Apply the fully connected layer
        x = self.fc(x)  # Shape: (b, m, z)

        return x

class patch_tst(nn.Module):
    def __init__(self, p = 3, s = 2):
        super().__init__()
        self.p = p
        self.s = s

    def standardize(self, x):
        # Get the dimensions of the input tensor
        batch_size, embed_size, sequence_len = x.shape
        
        # Initialize tensors to store means, standard deviations, and standardized tensor
        means = torch.empty(batch_size, embed_size)
        stds = torch.empty(batch_size, embed_size)
        standardized_tensors = torch.empty(batch_size, embed_size, sequence_len)
        
        # Iterate over each batch size
        for i in range(batch_size):
            # Iterate over each embed_size
            for j in range(embed_size):
                # Extract the rows corresponding to the current batch size and embed_size
                rows = x[i, j]
                
                # Calculate the mean and standard deviation of each row
                row_means = rows.mean()
                row_stds = rows.std()
                
                # Standardize the rows
                standardized_rows = (rows - row_means) / row_stds
                
                # Store means, standard deviations, and standardized rows
                means[i, j] = row_means
                stds[i, j] = row_stds
                standardized_tensors[i, j] = standardized_rows
        # print(f'Tensor device: {standardized_tensors.device}')
        return means, stds, standardized_tensors

    def padding(self, x, s):
        # Get the dimensions of the input tensor
        batch_size, embed_size, sequence_len = x.shape
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # Initialize an empty list to store the tensors with appended values
        appended_tensors = []
        
        # Iterate over each batch
        for i in range(batch_size):
            # Initialize an empty list to store the tensors with appended values for the current batch
            batch_tensors = []
            
            # Iterate over each embed_size
            for j in range(embed_size):
                # Extract the row corresponding to the embed_size and batch index
                row = x[i, j]
                
                # Get the last value of the sequence length
                last_value = row[-1]
                
                # Create a tensor of shape (s,) with the last value repeated
                values_to_append = torch.full((s,), last_value.item()).to(device)
                # Concatenate the original tensor row with the values to append
                appended_row = torch.cat([row, values_to_append])
                
                # Append the updated row to the list for the current batch
                batch_tensors.append(appended_row)
            
            # Stack the tensors for the current batch along the embed_size dimension
            batch_tensors = torch.stack(batch_tensors)
            
            # Append the tensors for the current batch to the list of appended tensors
            appended_tensors.append(batch_tensors)
        
        # Stack the tensors for all batches along the batch dimension
        appended_tensors = torch.stack(appended_tensors)
        return appended_tensors

    def patching(self, x, p, s):
        # Get the dimensions of the input tensor
        batch_size, embed_size, sequence_len = x.shape
        
        # Initialize an empty list to store the sub-arrays
        subarrays = []
        
        # Iterate over each batch
        for i in range(batch_size):
            # Iterate over each embed_size
            for j in range(embed_size):
                # Extract the row corresponding to the embed_size and batch index
                row = x[i, j]
                
                # Calculate the number of sub-arrays based on the given parameters
                num_subarrays = (len(row) - p) // s + 1
                
                # Create sub-arrays
                for k in range(num_subarrays):
                    subarray = row[k * s: k * s + p]
                    subarrays.append(subarray)
        
        # Convert the list of sub-arrays to a tensor
        subarrays_tensor = torch.stack(subarrays)
        
        # Reshape the tensor to have shape (batch * embed_size * num_subarrays, p)
        subarrays_tensor = subarrays_tensor.view(batch_size, embed_size, num_subarrays, p)
        
        return subarrays_tensor
    
    def project(self, x):
        b, m, n, p = x.shape
        d = 8 * p
        projection_layer = ProjectionLayer(d, p, n)

        return projection_layer(x)

    def transformer(self, x):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        b, m, n, d = x.shape
        SMHA = StackedMultiHeadAttentionModel(d, h = 1, num_layers=3).to(device)
        x = SMHA(x)
        return x
    
    def flatten(self, x):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        b, m, n, d = x.shape
        FFC = FlattenAndFullyConnected(n, d, 50).to(device)
        return FFC(x)

    def forward(self, x):

        # batch_size = 2
        # embed_size = 3
        # sequence_len = 11
        # p = 3
        # s = 2
        # x = torch.randn(batch_size, embed_size, sequence_len)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        s = self.s
        p = self.p
        # print('A', x.shape)
        means, std, x = self.standardize(x)
        x = x.to(device)
        # print(x.device)
        # print('B', x.shape)
        x = self.padding(x, s).to(device)
        # print('C', x.shape)
        x = self.patching(x, p, s)
        # print('D', x.shape)
        x = self.project(x)
        # print('F',x.shape)
        x = self.transformer(x)
        # print('trans', x.shape)
        x = self.flatten(x)
        # print('flat',x.shape)
        return x
