#coding:utf-8
import hashlib
import urllib
import requests

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
	print('translating:q=',q)
	q = urllib.parse.quote(q)
	url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?q='+q+'&from=en&to=zh&appid='+appid+'&salt='+salt+'&sign='+sign
	url = url.encode('utf-8')
	req = requests.get(url=url)
	trans = req.text
	return trans
if __name__ == '__main__':
	orignText = open('rnet-origin.txt','r',encoding='utf-8').read()
	transText = translate(originText)
	open('rnet-trans.txt','w').write(transText)
