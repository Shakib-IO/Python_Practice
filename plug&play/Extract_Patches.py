import numpy as np
from PIL import Image

# Patch Extractor Class
class PatchExtractor:
    def __init__(self, img, patch_size, stride):
        self.img = img
        self.patch_size = patch_size
        self.stride = stride

    def extract_patches(self):
        wp, hp = self.shape()
        return [self.extract((w, h)) for h in range(hp) for w in range(wp)]

    def extract(self, patch):
        return self.img.crop((
            patch[0] * self.stride,  # left
            patch[1] * self.stride,  # up
            patch[0] * self.stride + self.patch_size[0],  # right
            patch[1] * self.stride + self.patch_size[1]  # down
        ))

    def shape(self):
        wp = int((self.img.width - self.patch_size[0]) / self.stride + 1)
        hp = int((self.img.height - self.patch_size[1]) / self.stride + 1)
        return wp, hp

img_path = '/content/ca.png'
img = Image.open(img_path)
img_size = (1234, 1120)
patch_size = (32, 32)
extractor = PatchExtractor(img=img, patch_size=patch_size, stride=128)
patches = extractor.extract_patches()

count = 0  # Initialize count outside the loop

for p in patches:
    count += 1  # Increment count for each patch
    p.save(f"{count}_patches_image.png")  # Save each patch with a unique filename
