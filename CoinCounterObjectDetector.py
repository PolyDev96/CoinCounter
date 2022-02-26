# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 12:55:00 2022

@author: callum
"""

# Import packages
import cv2
import DataLoader


import matplotlib.pyplot as plt


# Config parameters
mainPath = 'C://Users//callu//Documents//Projects//Coin Counter//ObjectDetector//'

#%% Load and check first image and annotations
#Load the image
imagePath = mainPath + 'Training Dataset//image1.jpg'
img = cv2.cvtColor(cv2.imread(imagePath), cv2.COLOR_BGR2RGB)

# Add the annotations
# Load the annotation names
classFile = open(mainPath + 'class_list.txt', 'r')

classNames = DataLoader.ReadTxtFromFile(classFile)

# Load the annotations
annotationPath = mainPath + 'Training Dataset//image1.txt'
annotationFile = open(annotationPath, 'r')

annotations = []
with annotationFile as f:
    annotations = f.readlines()

classFile.close();

print(annotations)

#Plot the image
#plt.imshow(img)

#%% Load the full datasets
# load the training dataset


# load the test dataset



#%% Functions

#%% Read txt from file into an array of strings
# Also removes all \n from the strings
# Input file path
# Output array of lines