# Used .ipynb
from PIL import Image
from torchvision import transforms
# Read the original image
img = Image.open("./dog_and_cat.jpg")
img.show()

# Original image Tensor
transform = transforms.Compose([ 
    transforms.PILToTensor() 
]) 

img_tensor = transform(img) 
print("Original image tensor: ", img_tensor)

# Now Apply Hugging Face feature extractor
from transformers import AutoFeatureExtractor
feature_extractor = AutoFeatureExtractor.from_pretrained("google/vit-base-patch16-224-in21k")
img_features = feature_extractor(images=img, return_tensors="pt")
print("Image features: ", img_features)

# Now show the image features
transform = transforms.ToPILImage()
img = transform(img_features['pixel_values'].squeeze(0))
img.show()
