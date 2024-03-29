# OverlayPNGScript-Python
## Overlay PNG Python Script

This script layers png images on top of each other and creates a final layered png file.  
The order of the image must be appended to the end of its name like so: SampleImage_1.png.  
An image with a lower order will appear behind an image with a higher order.  

## Original Images
<div>
<img src="/SampleImages/Circle_1.png?raw=true" style="display: inline" alt="Image not found" width="100" height="100">
<img src="/SampleImages/Circle_2.png?raw=true" style="display: inline" alt="Image not found" width="100" height="100">
<img src="/SampleImages/Circle_3.png?raw=true" style="display: inline" alt="Image not found" width="100" height="100">
</div>

## Final Image
<img src="/SavedImages/FinalImage.png?raw=true" alt="Image not found" width="500" height="500">
 
## Changing parameters
Make sure to change the parameters at the top in the code.  
**imageDir**: Path of the directory that contains your images.  
**saveDir**: Path of the directory that you want your final image to be saved in.  
**croppedDir**: Path of the directory that you want your cropped images to be saved in (if save is set to true).  
**finalImageName**: What you want your final image to be called.  
**imageDim**: x,y dimensions of your images (all images will be cropped to this size).  
**offsetCrop**: x,y offset of your cropped images (the coordinates of the topleft corner of your image).  
**saveCroppedImages**: set to true if you want your cropped images to be saved in the croppedDir set above.  


## How Cropping Offset Works
![Image not found](/Screenshots/CropOffsetScreenshot.png?raw=true "How cropping offset works")

