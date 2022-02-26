# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 17:19:39 2022

@author: callu
"""
import CoinCounterSegmentation as CCSeg
import cv2

mainPath = 'C://Users//callu//Documents//Projects//Coin Counter//ObjectDetector//'
resizeFactor = 10

#Load the image
imagePath = mainPath + 'Original Images//image1.jpg'
img = cv2.cvtColor(cv2.imread(imagePath), cv2.COLOR_BGR2RGB)

# Create the scaled image
# resize the image by a set factor
newSizeX = int(img.shape[1]/resizeFactor)
newSizeY = int(img.shape[0]/resizeFactor)

imgScaled = cv2.resize(img, (newSizeX, newSizeY))

# Get the key points
keypoints = CCSeg.GetImageKeyPoints(imgScaled)

# Seperate each instance
CCSeg.SegmentFromScaledImg(imgScaled, keypoints, 5, mainPath+ 'SegmentedCoinsScaled//')
CCSeg.SegmentFromOriginalImg(img, keypoints, 5, mainPath + 'SegmentedCoins//', resizeFactor)

# Perform the classification