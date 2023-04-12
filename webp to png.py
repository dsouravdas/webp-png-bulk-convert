from PIL import Image
import os

def convert_from_webp(filename, path="C:/Users/User/Downloads/Internal/", new_extention= "png"):
    fname = filename.split('.')[0]
    img = Image.open(path + filename)

    if new_extention == "png":
        img.save((path+fname+".png"), "PNG")
    if new_extention == "jpg":
        img.save((path+fname+".jpg"), "JPEG", )

def convert_all(path="C:/Users/User/Downloads/Internal/"):
    for root, dirs, files in os.walk(path):
        for imagefile in files:
            if imagefile.endswith(".webp") or imagefile.endswith(".jpg") or imagefile.endswith(".jpeg"):
                convert_from_webp(imagefile, os.path.join(root, ""))

if __name__ == "__main__":
    convert_all()