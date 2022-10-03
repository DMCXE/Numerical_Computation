from Lagrange import Lagrange as la
import numpy as np
import matplotlib.pyplot as plt
import time
arr = np.array([[1960,180671],[1970,205052],[1980,227225],[1990,249623],[2000,282162],[2010,309327],[2020,329484]])
st = time.time()
Lag = la(arr)
#Lag.visualize(1940,2040,100)
po1 = Lag.num(1950)
stt = time.time()
print(stt-st)
print(po1)