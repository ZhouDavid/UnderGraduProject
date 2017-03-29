#coding:utf-8
import hashlib
import urllib
import requests

def md5(str):
	m = hashlib.md5()
	m.update(str)
	return m.hexdigest()

salt = '1435660288'
q='邢佳栋1972年7月1日出生于山西太原，毕业于北京电影学院表演系95班本科。2006年在电视剧《士兵突击》中出演“伍六一”一角。2009年6月12日参演电视剧《我的团长我的团》。后在2010年电视剧《烈火红岩》中饰演杜荫山；2011年电视剧《缉毒精英》中饰演大义警察“李涤凡”；2012年电视剧《战雷》中饰演舍己为人的滚雷英雄“林峰”；2013年主演年代悬疑剧《麻雀春天》。2014年10月29日，主演的电视剧《养父的花样年华》在央八开播。'
appid = '20170328000043661'
key = '3Lp28tN3wuavY4K8LET2'
sign = (appid+q+salt+key).encode('utf-8')
sign = md5(sign)
q = urllib.parse.quote(q)
url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?q='+q+'&from=zh&to=en&appid='+appid+'&salt='+salt+'&sign='+sign
url = url.encode('utf-8')
req = requests.get(url=url)
print(req.text)
