from Lagrange import Lagrange as la
import numpy as np
import matplotlib.pyplot as plt
import time
#arr = np.array([[1960,180671],[1970,205052],[1980,227225],[1990,249623],[2000,282162],[2010,309327],[2020,329484]])
N = 8
arr_y = 100*np.sin(np.random.random(N))
arr_x = np.linspace(0,100,N)
arr = np.c_[arr_x,arr_y]
st = time.time()
Lag = la(arr)
Lag.visualize(0,100,100,text=False)
po1 = Lag.num(19)
stt = time.time()
print(stt-st)
print(po1)