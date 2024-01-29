from numpy.random import randint
from numpy import sum,arange,array
def convolution(x:list,y:list):
    l1 = len(x)
    l2 = len(y)
    z = [0]*(l1+l2)
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            z[i+j-1] += x[i-1]*y[j-1]
    return z

c = 6
x = x0 = [1/c]*c
N = 2
for i in range(N-1):
    x = convolution(x,x0)

L = [0]*len(x)
for iterat in range(10000):
    z = sum(randint(1,7,N))
    L[z-1] += 1

from matplotlib.pyplot import plot,show,xticks,legend
plot(arange(1,len(x)+1),x,'r-*')
plot(arange(1,len(x)+1),array(L)/sum(L),'b-*')
xticks(range(1,len(x)+1))
legend(['expected','actual'])
show()