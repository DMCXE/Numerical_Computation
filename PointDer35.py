import numpy as np
#三点插值微分
def point3(x,y):
    h = np.abs(x[-1]-x[0])/len(x)
    df = np.array([])
    df = np.append(df,(-3*y[0]+4*y[1]-y[2])/(2*h))
    for i in range(1,len(x)-1):
        df = np.append(df,(y[i+1]-y[i-1])/(2*h))
    df = np.append(df,(3*y[-1]-4*y[-2]+y[-3])/(2*h))
    return df
#五点插值微分
def point5(x,y):
    h = np.abs(x[-1]-x[0])/len(x)
    df = np.array([])
    df = np.append(df,(y[0]-8*y[1]+8*y[2]-y[3])/(12*h))
    df = np.append(df,(y[1]-8*y[2]+8*y[3]-y[4])/(12*h))
    for i in range(2,len(x)-2):
        df = np.append(df,(y[i+2]-8*y[i+1]+8*y[i-1]-y[i-2])/(12*h))
    df = np.append(df,(y[-4]-8*y[-3]+8*y[-2]-y[-1])/(12*h))
    df = np.append(df,(y[-3]-8*y[-2]+8*y[-1]-y[-0])/(12*h))
    return df