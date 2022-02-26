# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 11:22:00 2022

@author: callum

This is the code used to create the training data

Version 1.0.0
"""

# Import packages
import cv2

import DataLoader as dt

import PredicitionEvaluation as evaluator
import CoinCounterSegmentation as CCSeg

import os
from os import path
import random

# Config parameters
mainPath = 'C://Users//callu//Documents//Projects//Coin Counter//ObjectDetector//'
datasetName = 'Original Images//'
numberOfImages = 18

valSplit = 10
testSplit = 20

#%% Load and check first image and annotations
#Load the image
imagePath = mainPath + datasetName + 'image1.jpg'
img = cv2.cvtColor(cv2.imread(imagePath), cv2.COLOR_BGR2RGB)

# Load and add the annotations
# Load the annotation names
classNames = dt.ReadTxtFromFile(mainPath + 'class_list.txt')

# Load the annotations
annotations = dt.ReadTxtFromFile(mainPath + datasetName + 'image1.txt')

evaluator.AnnotateImageText(img, annotations, classNames)

#%% Load the full datasets
# load the training dataset
for imageIndex in range(numberOfImages):
    
    # Load the image
    imagePath = mainPath +  datasetName + 'image' + str(imageIndex+1) + '.jpg'
    img = cv2.cvtColor(cv2.imread(imagePath), cv2.COLOR_BGR2RGB)

    # Load the annotations
    annotations = dt.ReadTxtFromFile(mainPath + datasetName + '//image' + str(imageIndex+1) + '.txt')
    
    # Segment the coins
    CCSeg.SegmentUsingLabelText(img, annotations, classNames, mainPath + 'SegmentedDataset//', 25)
    


#%% Split the dataset into train, test, and val
    
for className in classNames:
    
    # create the required test and val folders
    for objectClass in classNames:
        
        testDirectory = mainPath + 'SegmentedDataset//test//' + className
        valDirectory = mainPath + 'SegmentedDataset//val//' + className
        
        if not path.exists(testDirectory):
            os.mkdir(testDirectory)
            
        if not path.exists(valDirectory):
            os.mkdir(valDirectory)
    
    # Find the number of images in the class
    imageCount = len(os.listdir(mainPath + 'SegmentedDataset//' + className+ '//'))
    
    # Find the number of test and val images
    testImageCount = int(imageCount * testSplit/100)
    valImageCount = int(imageCount * valSplit/100)
    
    # Get the samples
    sampledImages = random.sample(range(1, imageCount), testImageCount + valImageCount)
    
    # Split the samples into test and val
    testImages = sampledImages[0:testImageCount-1]
    valImages = sampledImages[testImageCount:]
    
    
    # Get the test images
    for testImage in testImages:
        
        originalFilePath = mainPath + 'SegmentedDataset//' + className + '//image' + str(testImage) + '.png'
        newFilePath = mainPath + 'SegmentedDataset//test//' + className + '//image' + str(testImage) + '.png'
        
        os.rename(originalFilePath, newFilePath)
        
    # Get the val images
    for valImage in valImages:
        
        originalFilePath = mainPath + 'SegmentedDataset//' + className + '//image' + str(valImage) + '.png'
        newFilePath = mainPath + 'SegmentedDataset//val//' + className + '//image' + str(valImage) + '.png'
        
        os.rename(originalFilePath, newFilePath)
        
        
        

