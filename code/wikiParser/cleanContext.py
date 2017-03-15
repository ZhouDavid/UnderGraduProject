#coding:utf-8
def cleanContext(contextFileName,minContextNum):
    newContexts=[]
    contexts = open(contextFileName,'rb').readlines()
    tmp=''
    for c in contexts:
        c = c.decode('utf-8').strip()
        if len(tmp)<minContextNum:
            tmp+=c
        else:
            newContexts.append(tmp)
            tmp=c
    if len(tmp)<minContextNum:
        newContexts.append(tmp)
    return newContexts

if __name__ == '__main__':
    contexts = cleanContext('E:\\Graduation-Project\\code\\wikiParser\\test',200)
    contexts = [(c+'\n').encode('utf-8') for c in contexts]
    open('test2','wb').writelines(contexts)