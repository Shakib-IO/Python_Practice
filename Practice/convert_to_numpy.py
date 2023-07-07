import os
import cv2
import numpy as np
from tqdm import tqdm

def crop_and_resize(img, resize_dim=224):
    img = cv2.resize(img, (resize_dim, resize_dim), interpolation=cv2.INTER_AREA)
    return img

def get_data(chobi):
    img = cv2.imread(chobi)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    img = crop_and_resize(img)
    return img

def convert_to_numpy(path):
    inp_feat = []
    image_files = os.listdir(path)
    for file_name in tqdm(image_files[:3389]):
        file_path = os.path.join(path, file_name)
        img = get_data(file_path)
        inp_feat.append(img)

    inp_feat = np.array(inp_feat)
    print(inp_feat.shape)

    np.save("leukemia_malignant_test.npy", inp_feat)
    print("Done!")

read_path = "/content/drive/MyDrive/CSE465/Dataset/Leukemia/Test/all"
convert_to_numpy(read_path)

####################################################
import os
import cv2
import numpy as np
from tqdm import tqdm

Resize the image
def crop_and_resize(img, resize_dim=224):
    img = cv2.resize(img, (resize_dim, resize_dim), interpolation=cv2.INTER_AREA)
    return img

# Read images and convert it to RGB
def get_data(images):
    img = cv2.imread(images)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    img = crop_and_resize(img)
    return img

# Load images and convert it to numpy
def convert_to_numpy(path):
    print("path", path)
    folder_name = os.path.basename(path)  # Get the folder name
    inp_feat = []
    image_files = os.listdir(path)
    for file_name in tqdm(image_files):
        file_path = os.path.join(path, file_name)
        print(file_path)
        img = get_data(file_path)
        inp_feat.append(img)

    inp_feat = np.array(inp_feat)
    print(inp_feat.shape)
    print(f"Saving: {folder_name}")
    np.save(f"{folder_name}.npy", inp_feat)  # Save the .npy file with the folder name
    print("Done!")

root_path = "/content/drive/MyDrive/CSE465/Dataset/Leukemia"

train_path = os.path.join(root_path, "Train")
hem_train_path = os.path.join(train_path, "leukaemia_benign")
all_train_path = os.path.join(train_path, "leukaemia_malignant")

convert_to_numpy(hem_train_path)
convert_to_numpy(all_train_path)

test_path = os.path.join(root_path, "Test")
hem_test_path = os.path.join(test_path, "hem")
all_test_path = os.path.join(test_path, "all")

convert_to_numpy(hem_test_path)
convert_to_numpy(all_test_path)
