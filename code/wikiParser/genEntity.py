#coding:utf-8
def proRawName(fileIn,fileOut):
    lines = open(fileIn,'rb').readlines()
    starNames=[]
    lines = [line.decode('utf-8') for line in lines]
    for line in lines:
        names = line.strip().split()
        names= [name+' ' for name in names]
        starNames.extend(names)
    starNames = [name.encode('utf-8') for name in starNames]
    print(len(starNames))
    open(fileOut,'wb').writelines(starNames)

def genURLs(fileName):
    names =open(fileName,'rb').read()
    names = names.decode('utf-8')
    names = names.split()
    urls = [u'http://baike.baidu.com/search/word?word='+name for name in names]
    return urls
if __name__ == '__main__':
    fileName = 'E:\\Graduation-Project\\code\\wikiParser\\names'
    urls = genURLs(fileName)



