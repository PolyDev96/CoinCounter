# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:35:56 2022

Code used to rename the images to imageX.png

@author: callu
"""

import os
import cv2

#%% Config parameters
mainPath = 'C://Users//callu//Documents//Projects//Coin Counter//ObjectDetector//Images//'
newPath = 'C://Users//callu//Documents//Projects//Coin Counter//ObjectDetector//Renamed//'

files = os.listdir(mainPath)

imageIndex = 1

for file in files:
    
    # Load the origional image
    img = cv2.cvtColor(cv2.imread(mainPath + file), cv2.COLOR_BGR2RGB)
    
    # Save the new image
    cv2.imwrite(newPath + 'image' + str(imageIndex) + ".jpg", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    
    imageIndex = imageIndex + 1