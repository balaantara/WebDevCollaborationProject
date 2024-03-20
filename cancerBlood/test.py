from PIL import Image

import PIL
import numpy as np
import cv2
import matplotlib.pyplot as plt

Image.MAX_IMAGE_PIXELS = None
mat = Image.open(r"./Blood_Cancer/Sample_7667.tiff")
img = np.array(mat)
print(img.shape)


import os
os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2,40).__str__()

images=[]

#Reading a image from the dataset
img = cv2.imread('./Blood_Cancer/Sample_7667.tiff')

# print('IMAGE SIZE: '+str(img.shape[:2]))

#Append images for presentation
images.append(img)

#Transforming from RGB to GrayScale, preserving original image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  

dta = []
# apply binary thresholding
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
for i in range(len(thresh)):

    dta.append(thresh[i])



#Append Binary Image
images.append(thresh)

thresh = 255-thresh

# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
                                     
# draw contours on copy of the original image
img_copy = img.copy()
cv2.drawContours(image=img_copy, contours=contours, contourIdx=-1, color=(255, 200, 200), thickness=1, lineType=cv2.LINE_AA)

print(img)
#Append images for presentation
images.append(img_copy)

# print(images)
#Showing steps in contour drawing
plt.figure(figsize=(8,8))
for i, img in enumerate(images):
    
    plt.subplot(2,2,i+1)
    plt.grid(False)
    plt.imshow(img)

# f = open("biinery.txt", "w")
# f.write(str(dta))
# f.close()

plt.show()
