#coding:utf-8
import json
import os

def extracTrainData(trainDataFileName):
	articleNum = 1000
	content = open(trainDataFileName,'r').read()
	
def extracTrainData(trainDataFileName):
	articleNum = 100
	content = open(trainDataFileName,'r').read()
	dataDict = json.loads(content)
	articleList = dataDict['data'][:articleNum]
	version = dataDict['version']
	smallDict={}
	smallDict['data'] = articleList
	smallDict['version'] = version
	print('article number:',len(dataDict['data']))
	data = dataDict['data'][0]
	para = data['paragraphs'][0]
	qas = para['qas'][0]
	print(qas.keys())
	return smallDict
	#open('small_train.json','w').write(json.dumps(smallDict))

def extractLineFile(lineFileName,lineNum):
	fileLines = open(lineFileName,'r',encoding='utf-8').readlines()
	extractLines = fileLines[:lineNum]
	for i in range(len(extractLines)):
		extractLines[i] = extractLines[i]
	return extractLiness



if __name__ == '__main__':
	path = os.path.join('..','..','..','dataset','GraduData','Word2Vec','GoogleNews-vectors-negative300.bin')
	trainDataFileName ='E:\Graduation-Project\dataset\GraduData\SQuAD\\train-v1.1.json' 
	content = extractLineFile(path,10)
	open('smallWord2Vec','w',encoding='utf-8').writelines(content)