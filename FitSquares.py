import numpy as np
import matplotlib.pyplot as plt

class FitSquares_polynomial:
    def __init__(self,arr1,n):
        self.arr1 = arr1
        self.arr1_x = arr1[:,0]
        self.arr1_y = arr1[:,1]
        self.lenth = len(arr1)
        self.n = n
        self.an = self.phiprod()[0]

    def phiprod(self):
        n = self.n
        G = np.array([])
        d = np.array([])
        for i in range(0,n):
            d = np.append(d,np.sum((self.arr1_y)*(self.arr1_x**i)))
            for j in range(0,n):
                G = np.append(G,np.sum((self.arr1_x**i)*(self.arr1_x**j)))
        G = G.reshape(n,n)
        #通过np求逆求解，待更新轮子解法
        an = np.dot(np.linalg.inv(G), d)
        return an,G,d

    def num(self,x):
        num = 0
        for i in range(0,self.n):
            num = num+(self.an[i])*(x**i)
        return num

    def visualize(self,start,end,step,text):
        x = np.linspace(start,end,step)
        y = np.zeros(1)
        for i in x:
            y = np.append(y,self.num(i))
        y = y[1:]
        plt.figure()
        plt.scatter(self.arr1_x, self.arr1_y, c='red')
        if text is True:
            for j in range(0,self.lenth):
                plt.text(self.arr1_x[j],self.arr1_y[j],(self.arr1_x[j],self.arr1_y[j]))
        plt.plot(x,y)
        plt.show()




arr1 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
arr2 = np.array([[1,1.629],[1.25,1.756],[1.5,1.876],[1.75,2.008],[2,2.135]])

a = FitSquares_polynomial(arr1,5)
a.visualize(0,10,100,False)
print(a.phiprod()[0])
print(a.num(1))


        
