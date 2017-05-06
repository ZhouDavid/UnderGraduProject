#coding:utf-8
import json
articleNum = 100
trainDataFileName ='E:\Graduation-Project\dataset\GraduData\SQuAD\\train-v1.1.json' 
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
open('small_train.json','w').write(json.dumps(smallDict))