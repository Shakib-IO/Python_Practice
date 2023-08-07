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
##########################################################
import os
import cv2
import numpy as np
from tqdm import tqdm
from PIL import Image
import matplotlib.pyplot as plt


class ErrorForMultipleImage(Exception):
    def __init__(self, message:str) -> None:
        super().__init__()
        self.message = message

class ErrorForSingleImage(Exception):
    def __init__(self, message:str) -> None:
        super().__init__()
        self.message = message
        
# Resize the image
def crop_and_resize(img, resize_dim=1024):
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
    print(path)
    folder_name = os.path.basename(path)  # Get the folder name
    inp_feat = []
    image_files = os.listdir(path)
    for file_name in tqdm(image_files):
        file_path = os.path.join(path, file_name)
        img = get_data(file_path)
        inp_feat.append(img)

    inp_feat = np.array(inp_feat)
    print(inp_feat.shape)
    np.save(f"{folder_name}.npy", inp_feat)  # Save the .npy file with the folder name
    print("Done!")

# Folder Structure
"""
Dataset:
    - Images
        - image_01
        - image_02
        - image_03
"""
from matplotlib import pyplot as plt

def main() -> None:

    data_path = "./Datasett/"

    image_path = os.path.join(data_path, "Images")

    convert_to_numpy(image_path)


    """Optional"""

def single_image(data):
    image_data = data.reshape(1024,1024,3)
    pil_image = Image.fromarray(image_data)
    plt.imshow(pil_image)


def show_multiple_images(data):
  row = 1
  columns = len(image_data)
  fig, axarr = plt.subplots(row, columns, figsize=(15, 5))


  for i, img_array in tqdm(enumerate(data)):

    # Convert it to Image
    to_image = Image.fromarray(img_array)

    # Display each image on its corresponding subplot
    axarr[i].imshow(to_image)

  # Remove the extra empty subplots (if any)
  for i in range(len(data), row * columns):
      fig.delaxes(axarr.flatten()[i])

  plt.tight_layout()
  plt.show()

if __name__ == "__main__":
    main()
    
    """if you want to see your converted .npy file as image."""
    image_data = np.load("Images.npy")
    
    if image_data.shape[0] == 1:
        single_image(image_data)
    else:
        show_multiple_images(image_data)

    """
    # For multiple Images
    try:
        show_multiple_images(image_data)
    except:
        raise ErrorForMultipleImage("You have a single image!! Your image shape is {} and batch size is: {}".format(image_data.shape, image_data.shape[0]))

    # For Single Images
    try:
        single_image(image_data)
    except:
        raise ErrorForSingleImage("You have a multiple image!! Your image shape is {} and batch size is: {}".format(image_data.shape, image_data.shape[0]))
    """

##########################################################
import os
import cv2
import argparse
import numpy as np
from tqdm import tqdm
from PIL import Image
import matplotlib.pyplot as plt


"""
Assuming Dataset Folder Structure.

Dataset:
    - Images
        - image_01
        - image_02
        - image_03

Example: 
python images_to_numpy.py --root_data_path "./Dataset" --image_path "Images" --saved_folder_name "to_numpy" --visualize yes --visualize_for multiple 
"""

parser = argparse.ArgumentParser(description= 'Convert images to numpy array')
parser.add_argument('--root_data_path', type= str, required= True, default = "./Dataset", help = 'Define root dataset path.')
parser.add_argument('--image_path', type= str, required= True, default= "Images", help = 'Set images path.')
parser.add_argument('--saved_file_name', type= str, required= True, default= "images_to_nparray", help = 'Define saved file name.')
parser.add_argument('--visualize', type= str, choices= ['no', 'yes'], default= "no", required= True, help = 'Visualize images.')
parser.add_argument('--visualize_for', type= str, choices= ['single', 'multiple', "no"], default="no", required= False, help = 'Choose Visualize for single/multiple images.')

args = parser.parse_args()


def crop_and_resize(img, resize_dim = 256):
    """
    Resize the input image.
    
    Aurguments:
        img: Orginal input image
        resized_dim: Size of new image (Default: 256)
    
    Returns:
        img: new image
    """
    img = cv2.resize(img, (resize_dim, resize_dim), interpolation=cv2.INTER_AREA)
    return img

def get_data(images):
    """
    Read images and convert it to RGB. By default OpenCV read images in BGR format.

    Aurguments:
        img: input image

    Returns:
        img: RGB image

    """
    img = cv2.imread(images)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = crop_and_resize(img)
    return img

def convert_to_numpy(path) -> None:
    """
   Load images and convert it to numpy

    Aurguments:
        path: input image path

    Returns:
        None

    """

    inp_feat = []
    image_files = os.listdir(path)
    for file_name in tqdm(image_files):
        file_path = os.path.join(path, file_name)
        img = get_data(file_path)
        inp_feat.append(img)

    inp_feat = np.array(inp_feat)
    print(inp_feat.shape)
    np.save(f"{args.saved_file_name}.npy", inp_feat)  # Save the .npy file with the folder name
    print("Done!")


def visualize(data):
    """
    (Optional) 
    Visualization of ndarray as Images. 
    """
    if args.visualize_for == "single":
        image_data = data.reshape(1024,1024,3)
        pil_image = Image.fromarray(image_data)
        plt.imshow(pil_image)

    else:
        row = 1
        columns = len(data)
        fig, axarr = plt.subplots(row, columns, figsize=(15, 5))

        for i, img_array in tqdm(enumerate(data)):
            # Convert it to Image
            to_image = Image.fromarray(img_array)
            # Display each image on its corresponding subplot
            axarr[i].imshow(to_image)
        
        # Remove the extra empty subplots (if any)
        for i in range(len(data), row * columns):
            fig.delaxes(axarr.flatten()[i])

        plt.tight_layout()
        plt.show()

def main() -> None:

    root_data_path = args.root_data_path 
    image_path = os.path.join(root_data_path, args.image_path)
    convert_to_numpy(image_path)

if __name__ == "__main__":
    main()
    
    
    """if you want to visualize your converted .npy file as image."""
    converted_image_data = np.load(args.saved_folder_name + '.npy')
    
    if args.visualize == 'no':
        print("Nothing to Show!!")
    else:
        visualize(converted_image_data)
        
