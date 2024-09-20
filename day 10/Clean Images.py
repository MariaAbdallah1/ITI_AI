import os
from PIL import Image
from hashlib import md5

image_dir = "Source/Images"

# Remove duplicates based on MD5 hash
def remove_duplicates():
    image_hashes = set()
    deleted=[]
    for filename in os.listdir(image_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            file_path=os.path.join(image_dir, filename)
            with open(file_path, "rb") as img_file:
                img_hash = md5(img_file.read()).hexdigest()
                if img_hash in image_hashes:
                    c=str.lower( input(f'the image {filename} is already exist before Do you want to remove it (y=yes or n=No)?'))
                    if c=='y':
                        deleted.append(os.path.join(image_dir, filename))
                    elif c=='n':
                        print('Not Removed')
                        image_hashes.add(img_hash)
                else:
                    image_hashes.add(img_hash)
    if len(deleted)!=0:
        for path in deleted:
            os.remove(path)
            print(f"{path} deleted successfully.")
remove_duplicates()

# Remove corrupted or incomplete images
def remove_corrupted_images():
    for filename in os.listdir(image_dir):
        img_path = os.path.join(image_dir, filename)
        try:
            with Image.open(img_path) as img:
                img.verify()
                print(f'{filename} is verified')
        except (IOError, SyntaxError) as e:
            os.remove(img_path)
            print(f'{filename} is removed')

# remove_corrupted_images()