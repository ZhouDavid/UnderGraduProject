#coding:utf-8
import json
import collections
from collections import Counter
import nltk 

dataPath = '../../dataset/GraduData/SQuAD\\train-v1.1.json'
trainJsonStr = open(dataPath,'r').read()
trainDict = json.loads(trainJsonStr)
trainData = trainDict['data']
cleanTrainData={}
cleanTrainData['version'] = trainDict['version']
cleanTrainData['data'] = []
wordCounter=Counter()
vobSize = 20000

def clean(sentences):
	sentences = [sentence for sentence in nltk.sent_tokenize(sentences)]
	tokens=[]
	for sentence in sentences:
		tokens.extend([token.replace("''", '"').replace("``", '"') for token in nltk.word_tokenize(sentence)])
	return tokens


def wordCount(string):
	sentences = string.strip()
	words =  clean(sentences)
	for word in words:
		wordCounter[word]+=1

def transform(text):
	transformedText=[]
	tokens = clean(text)
	for token in tokens:
		if token in wordEmbedding:
			transformedText.append(wordEmbedding[token])
		else:
			transformedText.append(wordEmbedding['UNK'])
	return str(transformedText)

#traverse raw data first time to get word dictionary
for c in trainData:
	title = c['title']
	paras = c['paragraphs']
	for para in paras:
		context = para['context']
		wordCount(context)
		qas = para['qas']
		for qa in qas:
			question = qa['question']
			wordCount(question)
print('finishing...')
print(len(wordCounter))
commonWordsDict = wordCounter.most_common()[:vobSize]

# one-hot word embedding
commonWordsDict.append(('UNK',1))
vobSize = len(commonWordsDict)
wordEmbedding = {}
vecSize = vobSize
print('one hot embedding...')
for i,item in enumerate(commonWordsDict):
	wordEmbedding[item[0]] = i
	#wordEmbedding[item[0]][i] = 1

#遍历traindata, 进行数据转化
print('transforming...')

for c in trainData:
	tmp={}
	title = c['title']
	paras = c['paragraphs']
	tmp['title'] = transform(title)
	tmp['paragraphs']=[]
	for para in paras:
		ttmp = {}
		ttmp['context'] = transform(para['context'])
		ttmp['qas'] = []
		for qa in para['qas']:
			tttmp = {}
			tttmp['question'] = transform(qa['question'])
			tttmp['answers'] = []
			for ans in qa['answers']:
				ttttmp = {}
				ttttmp['answer_start'] = ans['answer_start']
				ttttmp['text'] = transform(ans['text'])
				tttmp['answers'].append(ttttmp)
			ttmp['qas'].append(tttmp)
		tmp['paragraphs'].append(ttmp)
	cleanTrainData['data'].append(tmp)

open('../../dataset/output/change','w').write(json.dumps(cleanTrainData))
# wordDict = collections.OrderedDict(sorted(commonWordsDict,key = lambda x:x[1],reverse = True))
# open('tmp','w').write(json.dumps(wordDict))

