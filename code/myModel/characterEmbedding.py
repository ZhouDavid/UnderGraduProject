#coding: utf-8
import tensorflow as tf

def CharacterEmbeddingLayer(contextSentences):
	'''contextSentences: a list of word id'''
	shape = contextSentences.get_shape()
	
	return 0

if __name__ == '__main__':
	d = 100
	context = tf.placeholder(tf.int32,shape=[d,None])
	print(context.get_shape()[1])
