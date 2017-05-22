#coding: utf-8
import tensorflow as tf
import numpy as np
def readVocTable(fileName):
	content = open(fileName,'r')

def CharacterEmbeddingLayer(contextSentences,vocTable):
	'''contextSentences: a list of word id'''
	shape = contextSentences.get_shape()

	
	return 0

if __name__ == '__main__':
	d = 100
	context = tf.placeholder(tf.int32,shape=[d,None])
	print(context.get_shape()[1])
