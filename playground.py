import numpy as np
arr1 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
a = [[1,2]]
a.append([2,5,6])
print(len(a))
ab = np.array([])
b = np.append(ab,1)
aa = np.random.random(8)
print(2*np.ones(8))
bq = np.append(np.append(np.zeros(1),aa),0)
print(bq)