# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 17:19:56 2022

@author: callum

This code has been developed to segment the coins from the image
using computer vision methods

Version 1.0.0
"""
#%% Imported libaries
import cv2

import os
from os import path


#%% Function to find the key points through canny and blod detection
def GetImageKeyPoints(img):

    #%% Configer the image
    
    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    #%% Perform the edge detection 
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
    
    #%% detect the blobs ("coins")
    detector = cv2.SimpleBlobDetector_create()
    
    keypoints = detector.detect(edges)
    
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    #im_with_keypoints = cv2.drawKeypoints(edges, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    #plt.imshow(im_with_keypoints)
    
    return keypoints

#%% Function to segment the keypoints into seperate images
# Uses the scaled image
def SegmentFromScaledImg(img, keypoints, border, filePath):
    
    # Loop through each keypoint and segment the surrounding area
    keyPointIndex = 0
    
    for keypoint in keypoints:
        
        # Define the crop box from the keypoint
        topLeftX = int((keypoint.pt[0] - keypoint.size/2) - border)
        topLeftY = int((keypoint.pt[1] - keypoint.size/2) - border)
        
        bottomRightX = int((keypoint.pt[0] + keypoint.size/2) + border)
        bottomRightY = int((keypoint.pt[1] + keypoint.size/2) + border)
        
        cropped_image = img[topLeftY:bottomRightY, topLeftX:bottomRightX, :]
        cv2.imwrite(filePath + "image" + str(keyPointIndex) + ".png", cropped_image)
        
        keyPointIndex = keyPointIndex + 1
        
    return 
    
    
#%% Function to segment the keypoints into seperate images
# Uses the original image
def SegmentFromOriginalImg(img, keypoints, border, filePath, scaleFactor):
    

    # Loop through each keypoint and segment the surrounding area
    keyPointIndex = 0
    
    for keypoint in keypoints:
        
        # Define the crop box from the keypoint
        topLeftX = int((keypoint.pt[0] - keypoint.size/2) - border) * scaleFactor
        topLeftY = int((keypoint.pt[1] - keypoint.size/2) - border) * scaleFactor
        
        bottomRightX = int((keypoint.pt[0] + keypoint.size/2) + border) * scaleFactor
        bottomRightY = int((keypoint.pt[1] + keypoint.size/2) + border) * scaleFactor
        
        cropped_image = img[topLeftY:bottomRightY, topLeftX:bottomRightX, :]
        cv2.imwrite(filePath + "image" + str(keyPointIndex) + ".png", cropped_image)
        
        keyPointIndex = keyPointIndex + 1
    
    return

#%% Function used to segment the coins using labelled data
def SegmentUsingLabelText(img, annotations, classNames, filePath, border):
    
    # Create each class directory
    for objectClass in classNames:
        
        directory = filePath + objectClass + '//'
        
        if not path.exists(directory):
            os.mkdir(directory)

    
    #Segment each annotation
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
        
        
        topLeftX = int((imgSize[1] * xCenter) - xWidthPixel/2) - border
        topLeftY = int((imgSize[0] * yCenter) - yHeightPixel/2) - border
        
        bottomRightX = int((imgSize[1] * xCenter) + xWidthPixel/2) + border
        bottomRightY = int((imgSize[0] * yCenter) + yHeightPixel/2) + border
    
        # Segment from the image
        cropped_image = img[topLeftY:bottomRightY, topLeftX:bottomRightX, :]
        
        # Save in the correct location
        # find how many images exist in the directory        
        imageCount = len(os.listdir(filePath + className+ '//')) + 1
        
        cv2.imwrite(filePath + className+ '//' + "image" + str(imageCount) + ".png", cv2.cvtColor(cropped_image, cv2.COLOR_RGB2BGR))
        

        
    return