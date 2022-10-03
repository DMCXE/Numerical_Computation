import numpy as np
arr = np.array([[1,2],[3,4],[5,6],[7,8]])
arr2 = np.array([[1,3],[2,4],[7,6],[7,9]])
x = arr[:,0]

n = len(arr)
a = np.ones((n,n))
x3 = x*a

x3[np.eye(4,dtype=bool)]=0
b = (x*a).T
b[~np.eye(4,dtype=bool)].reshape(4,3)
res = b-x3
res2 = np.prod(res,axis=1,where=res!=0,keepdims=False)
print(b)
print(x3)
print(res)
print(res2)
c = np.array([4,5,6,7])
d = np.array([1,2,3,4])
print(c)
print(res2/c)
print(np.sum(d*res2/c))
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B=A[~np.eye(A.shape[0],dtype=bool)].reshape(A.shape[0],-1)

print(B)
def f(x):
    one = np.ones((4, 4))
    arro = sum((x * one).T)
    return arro
y = np.zeros(1)
x = np.linspace(1,10,5)
for i in x:
        y = np.append(y,f(i))
y = y[1:]
print(y)