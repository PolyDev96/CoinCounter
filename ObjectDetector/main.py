# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 12:55:00 2022

@author: callum
"""

# Import packages
import cv2
import torch


import matplotlib.pyplot as plt


import DataLoader

# Config parameters
mainPath = 'C://Users//callu//Documents//Projects//Coin Counter//ObjectDetector//'

#%% Load and check first image and annotations
#Load the image
imagePath = mainPath + 'Training Dataset//image1.jpg'
img = cv2.cvtColor(cv2.imread(imagePath), cv2.COLOR_BGR2RGB)

# Load and add the annotations
# Load the annotation names

classNames = DataLoader.ReadTxtFromFile(mainPath + 'class_list.txt')

# Load the annotations
annotations = DataLoader.ReadTxtFromFile(mainPath + 'Training Dataset//image1.txt')

#Add each annotation
for annotation in annotations:
    
    # split the annotation into each part
    splitAnnotation = annotation.split()
    
    className = classNames[int(splitAnnotation[0])]
    xCenter = float(splitAnnotation[1])
    yCenter = float(splitAnnotation[2])
    xWidth = float(splitAnnotation[3])
    yHeight = float(splitAnnotation[4])
    
    # Calculate the pixel postion
    imgSize = img.shape
    
    xWidthPixel = imgSize[1] * xWidth
    yHeightPixel = imgSize[0] * yHeight
    
    
    xTopRight = (imgSize[1] * xCenter) + xWidthPixel/2
    yTopRight = (imgSize[0] * yCenter) - yHeightPixel/2
    
    xBottomLeft = (imgSize[1] * xCenter) - xWidthPixel/2
    yBottomLeft = (imgSize[0] * yCenter) + yHeightPixel/2

    
    cv2.rectangle(img,(int(xTopRight), int(yTopRight)),
              (int(xBottomLeft), int(yBottomLeft)),
              color=(0, 255, 0),thickness=10)
    
    
    ((label_width, label_height), _) = cv2.getTextSize(className, fontFace=cv2.FONT_HERSHEY_PLAIN,
        fontScale=10, thickness=2)
    
    cv2.rectangle(img, (int(xBottomLeft), int(yBottomLeft)),
                 (int(xBottomLeft + label_width + label_width * 0.05), 
                 int(yBottomLeft + label_height + label_height * 0.25)),
      color=(0, 255, 0), thickness=cv2.FILLED)
    
    cv2.putText( img, className,org=(int(xBottomLeft), int(yBottomLeft + label_height + label_height * 0.25)), # bottom left
      fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=10, color=(0, 0, 0), thickness=10)


#Plot the image
plt.imshow(img)

#%% Load the full datasets
# load the training dataset


# load the test dataset




    


