import numpy as np
import tensorflow as tf
filename_queue = tf.train.string_input_producer(['iris_test.csv','iris_training.csv'])
reader = tf.TextLineReader()
key,value = reader.read(filename_queue)
record_defaults = [[1],[1],[1],[1],[1]]
col1,col2,col3,col4,col5 = tf.decode_csv(value,record_defaults=record_defaults)
features = tf.stack([col1,col2,col3,col4])
with tf.Session() as sess:
        
