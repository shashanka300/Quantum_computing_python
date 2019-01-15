#W=ax+by
#x=0
#y=1
import numpy as np
a=(0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1)
b=(1,.9,.8,.7,.6,.5,.4,.3,.2,.1,0)
def estimator(a,b):
    prob=(a,b)
    #choose 1 of the 2 choises with probablity
    w=np.random.choice([0,1],1,p=prob)
    print(w)
for (x,y) in zip(a,b):
    estimator(x,y)
