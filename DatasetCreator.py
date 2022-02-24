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

# Config parameters
mainPath = 'C://Users//callu//Documents//Projects//Coin Counter//ObjectDetector//'
datasetName = 'Training Dataset//'
numberOfImages = 2

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
    



    


