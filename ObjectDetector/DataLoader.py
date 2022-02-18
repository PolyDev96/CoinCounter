# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:35:54 2022

@author: callum
"""

#%% Read txt from file into an array of strings
# Also removes all \n from the strings
# Input file path
# Output array of lines

def ReadTxtFromFile(filePath):
    # Open file
    file = open(filePath, 'r')

    # Set deafult values
    lines = []
    
    # Iterate through each line of the file
    with file as f:
        lines = f.readlines()
        
    # Iterate through each line and remove \n
    count = 0
    
    for line in lines:
        lines[count] = line.replace('\n', '')
        count = count + 1

    
    
    # close file
    file.close();

    return lines