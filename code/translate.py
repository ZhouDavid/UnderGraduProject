#coding:utf-8
import hashlib
import urllib
import requests
import chardet
import string

def cleanText(rawOriginText):
	f = filter(lambda x:x in string.printable,rawOriginText)
	cleanOiriginText = [item for item in f]
	return str(cleanOiriginText)

def md5(str):
	m = hashlib.md5()
	m.update(str)
	return m.hexdigest()

def translate(origin):
	q = origin
	trans=''
	salt = '1435660288'
	appid = '20170328000043661'
	key = '3Lp28tN3wuavY4K8LET2'
	sign = (appid+q+salt+key).encode('utf-8')
	sign = md5(sign)
	# print('translating:q=',q)
	q = urllib.parse.quote(q)
	url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?q='+q+'&from=en&to=zh&appid='+appid+'&salt='+salt+'&sign='+sign
	url = url.encode('utf-8')
	req = requests.get(url=url)
	trans = req.text
	return trans
if __name__ == '__main__':
	originText = open('origin-rnet.txt','r',encoding='utf-8').read()
	originText = cleanText(originText)
	#transText = translate(originText).encode('latin-1').decode('unicode_escape').encode('utf-8')
	open('trans-rnet.txt','w').write(originText)
