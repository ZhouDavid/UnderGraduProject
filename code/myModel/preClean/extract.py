#coding:utf-8
import json

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
	return extractLines



if __name__ == '__main__':
	trainDataFileName ='E:\Graduation-Project\dataset\GraduData\SQuAD\\train-v1.1.json' 
	content = extractLineFile('one-hot',10)
	open('small-one-hot','w',encoding='utf-8').writelines(content)