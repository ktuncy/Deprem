from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

df4=pd.read_excel('C:/Users/Asus/Desktop/excll/kitap12.xlsx',usecols=[0])
df5=pd.read_excel('C:/Users/Asus/Desktop/excll/kitap12.xlsx',usecols=[1])

bool_series=df5.duplicated()
bool_series=np.array(bool_series).astype(str)
      
radon=df4.values.tolist()
radon=np.array(radon).astype(int)

df51=df5.pivot_table(index = ['Unnamed: 1'], aggfunc = 'size')
pivy = df51.values.tolist()
pivy = np.array(pivy)

temper=df5.values.tolist()
temper=np.array(temper).astype(float)

victor = []
vitoria = []
victoria = []
victory = []
vimeo = []

b = 0
c = 0
im = 0
       
for i in range(0,972):
        b = b + pivy[i]
        victor.append(b)

victor = np.array(victor)

for j in range(0,972):
    while im < victor[j]:
        c = c + radon[im]
        im = im + 1 
    vitoria.append(c)
    
vitoria = np.array(vitoria)

for k in range(1,972):
     d = vitoria[k] - vitoria[k-1]
     victoria.append(d)

victoria = np.array(victoria)
victoria1 = np.insert(victoria,0,2172)
   
victory = victoria1/pivy

for m in range(0,7979):
    if temper[m] != temper[m+1]:
        vimeo.append(temper[m])
      
vimeo = np.array(vimeo)
vimeo1 = np.insert(vimeo,971,39.18)

A = 50
B = np.mean(vimeo1)
C = np.std(vimeo1)

def Gauss(vimeo1,A,B,C,offset):
     return A*np.exp(-(vimeo1-B)**2/(2*C**2)) + offset

parameters, covariance = curve_fit(Gauss,vimeo1,victory,p0=(A,B,C,100))

fit_A = parameters[0]
fit_B = parameters[1]
fit_C = parameters[2]
fit_D = parameters[3]

curvex = np.linspace(np.min(vimeo1),np.max(vimeo1),972)

fit_y = Gauss(vimeo1,fit_A,fit_B,fit_C,fit_D)

fig,ax = plt.subplots(figsize=(9,9))

plt.plot(vimeo1,victory,'o')

plt.plot(curvex,fit_y,'-')

plt.show()

        
           

        




    



    


