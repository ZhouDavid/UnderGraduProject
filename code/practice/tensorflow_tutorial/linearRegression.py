#coding:utf-8
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
rng = np.random

#parameter
learning_rate = 0.01
training_epochs = 1000
display_step = 100

#Training_Data
trainX = np.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
                         7.042,10.791,5.313,7.997,5.654,9.27,3.1])

trainY = np.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
                         2.827,3.465,1.65,2.904,2.42,2.94,1.3])

sampleNum = trainX.shape[0]

#tf Graph Input
X = tf.placeholder('float')
Y = tf.placeholder('float')

#Set model weights
print(rng.randn())