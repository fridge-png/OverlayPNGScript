from PIL import Image
import os

# This script layers png images on top of each other and creates a final layered png file
# The order of the image must be appended to the end of its name like so: SampleImage_1.png
# An image with a lower order will apear behind an image with a higher order

#========================================
# FIELDS TO CHANGE 
# path of the directory that contains your images 
imageDir = "SampleImages/"
# path of the directory that you want your final image to be saved in 
saveDir = "SavedIMages/"
# what you want your final image to be called
finalImageName = "FinalImage"
#========================================

# checks if the directories exist
def checkDir():
    if(os.path.isdir(imageDir) and os.path.isdir(saveDir)):
        return True
    else:
        return False

# gets the order of the image for sorting
def getNum(img):
    try:
        return int(img[img.rindex('_')+1:img.rindex('.')])
    except ValueError:
        return float('inf')

# uses the PIL library to layer images and saves to the save directory
def layerImages():
    images = os.listdir(imageDir)
    images.sort(key=getNum)
    try:
        img1 = Image.open(imageDir + images[0])
    except:
        print("Error while reading images.")
        return
    for image in images:
        if(image[-4:].lower() == ".png"):
            if (getNum(image) == float('inf')):
                print("File {image} is not named correctly.\nMake sure the file ends with \'_\' and its order.\n".format(image = image))
            else:
                try:
                    img2 = Image.open(imageDir + image)
                    img1.paste(img2, (0,0), mask = img2)
                except:
                    print("Error while reading images.")
                    return
        else:
            print("File {image} is not a .png file.\n".format(image = image))

        img1.save(saveDir + finalImageName + ".png")


if(checkDir()):
    layerImages()
else:
    print("The image directory you specified was not found.")