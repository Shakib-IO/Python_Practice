import os

# Set as a base directory
path = os.path.abspath(os.getcwd())

# Join the images path
images = os.listdir(os.path.join(path, "images"))
print(f"Images: {len(images)}")

# Join the label path
label = os.listdir(os.path.join(path, "labels"))
print(f"Label: {len(label)}")


missing_files = []
for img in images:
    img_name = os.path.splitext(img)[0]
    if img_name not in [os.path.splitext(lab)[0] for lab in label]:
        missing_files.append(img_name)

print("Status of Missing labels.")
if len(missing_files) == 0:
    print("No missing labels found!!!")
else:
    for i in missing_files:
        print(i)
