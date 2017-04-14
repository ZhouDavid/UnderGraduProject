#coding:utf-8
import json
articleNum = 100
content = open('../../dataset/output/change','r').read()
dataDict = json.loads(content)
articleList = dataDict['data'][:articleNum]
smallDict={}
smallDict['version'] = dataDict['version']
smallDict['data'] = articleList
open('../../dataset/output/changeSmall','w').write(json.dumps(smallDict))