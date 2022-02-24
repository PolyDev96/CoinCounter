# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 13:12:51 2022

This code is used to train an object classifier 

@author: callu
"""
import matplotlib.pyplot as plt
import numpy as np
import os  
os.environ["CUDA_VISIBLE_DEVICES"]="-1" 

import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator


#%% Config parameters
batch_size = 32
img_height = 180
img_width = 180

epochs=10

datasetDir = 'C://Users//callu//Documents//Projects//Coin Counter//ObjectDetector//SegmentedDataset//'


#%% Load the datasets
# Load the training dataset
train_datagen = ImageDataGenerator(rescale=1./255)

train_ds = train_datagen.flow_from_directory(
    directory= datasetDir + "train/",
    target_size=(img_height, img_width),
    color_mode="rgb",
    batch_size=32,
    class_mode="categorical",
    shuffle=True,
    seed=42
)


# Load the val dataset
val_datagen = ImageDataGenerator(rescale=1./255)

val_ds = val_datagen.flow_from_directory(
    directory= datasetDir + "val/",
    target_size=(img_height, img_width),
    color_mode="rgb",
    batch_size=32,
    class_mode="categorical",
    shuffle=False,
    seed=42
)

# Load the test dataset
test_datagen = ImageDataGenerator(rescale=1./255)

test_ds = test_datagen.flow_from_directory(
    directory= datasetDir + "test/",
    target_size=(img_height, img_width),
    color_mode="rgb",
    batch_size=32,
    class_mode="categorical",
    shuffle=False,
    seed=42
)


#%% Create the basic model
num_classes = 8

model = Sequential([
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(num_classes)
])

model.compile(optimizer='adam', loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


#%% Perform the training
history = model.fit(train_ds, validation_data=val_ds, epochs=epochs)


#%% Plot the training information
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

#%% Make predictions using the model
predictions = model.predict(test_ds)
score = tf.nn.softmax(predictions[0])

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format('name', 100 * np.max(score))
)
