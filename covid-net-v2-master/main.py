import numpy as np
import tensorflow as tf
import pandas as pd
import cv2
import os
main_model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(256, 256)),
    #256 * 256 pixels per image
    #tf.keras.layers.Dense(2, activation = 'relu'),
    #How many hidden layers?
    #tf.keras.layers.Dense(2, activation  = 'sigmoid')
    #We can use sigmoid functions for the output-layer
])
main_model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
              #Temporary set functions(Can change later)
#loss, accuracy2 = main_model.evaluate(inputs, expected outputs)
#print('Accuracy: %.2f' % (accuracy2 *100))