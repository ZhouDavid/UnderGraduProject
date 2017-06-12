#coding：utf-8
from pylab import *
import numpy as np
x=np.linspace(-np.pi,np.pi,256,endpoint=True)
y1,y2=np.cos(x),np.sin(x)
plot(x,y1)
plot(x,y2)
show()
