#coding:utf-8
import bs4
from bs4 import BeautifulSoup
import requests
import genEntity

def replacedString(string):
    starts = []
    ends = []
    for i,s in enumerate(string):
        if s=='[':starts.append(i)
        elif s==']':ends.append(i)

    newString=""
    start = 0
    for i in range(len(starts)):
        newString+=string[start:starts[i]]
        start = ends[i]+1
        if start>len(string):break

    if start<len(string):
        newString+=string[start:len(string)]
    return newString

def cleanContext(rawContextList):
    cleanedContext = ""
    for context in rawContextList:
        if isinstance(context,bs4.element.NavigableString):
            cleanedContext+=context.strip()
        else:
            cleanedContext+=cleanContext(context.contents)
    return cleanedContext

def getContext(soup):
    contexts=[]
    # description = soup.find("meta",attrs={"name":"description"})
    # if description:
    #     contexts.append(description.get('content'))
    divs = soup.find_all('div',class_="para")
    for div in divs:
        cleanedContext = cleanContext(div.contents)+'\n'
        if len(cleanedContext)>30:
            cleanedContext = replacedString(cleanedContext)
            contexts.append(cleanedContext)
    return contexts

def getHtmlContent(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    htmlContent = response.text
    return htmlContent

def filt(urls):
    uurls = []
    for url in urls:
        if url:
            if url.startswith('/item'):
                uurls.append(url)
    return uurls

def getURLs(soup):
    urls = soup.find_all('a')
    urls = [url.get('href') for url in urls]
    urls = filt(urls)
    urls = ['http://baike.baidu.com'+url for url in urls]
    return urls

def parse(count,url):
    print('parsing {}...'.format(count))
    try:
        htmlContent = getHtmlContent(url)
        soup = BeautifulSoup(htmlContent)
        newURLs = getURLs(soup)
        newContexts = getContext(soup)
        newContexts = [context.encode('utf-8') for context in newContexts]
        contexts.extend(newContexts)
        return newURLs
    except:
        print('got exception...')
        return None

def parseAll(pageNum):
    count = 0
    while not len(urlList) == 0:
        url = urlList.pop()
        count+=1
        urls = parse(count,url)
        if count >pageNum:
            break
        if len(urlList) < pageNum:
            urlList.extend(urls)
if __name__ == '__main__':

urlList = genEntity.genURLs('E:\\Graduation-Project\\code\\wikiParser\\names')
pageNum = 100
contexts = []
for i in range(len(urlList)):
    parse(i,urlList[i])
#parseAll(pageNum)
open('test','wb').writelines(contexts)
