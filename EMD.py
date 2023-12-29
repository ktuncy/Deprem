import matplotlib.pyplot as plt
import numpy as np
import emd as emd
import pandas as pd

df5=pd.read_excel('C:/Users/Asus/Desktop/dışarda.xlsx',usecols=[5])
counts=np.array(df5)

imf0 = []
counts0 = []
imf1 = []
counts1 = []
imf2 = []
counts2 = []
imf3 = []
counts3 = []

imf = emd.sift.sift(counts)

for i in range(0,89):
        b = imf[i][0]
        imf0.append(b)
        c = imf[i][1]
        imf1.append(c)
        d = imf[i][2]
        imf2.append(d)
        e = imf[i][3]
        imf3.append(e)
        
imf0 = np.array(imf0)
imf1 = np.array(imf1)
imf2 = np.array(imf2)
imf3 = np.array(imf3)
summed = imf0 + imf1 + imf2 + imf3

plt.plot(imf0)
plt.plot(imf1)
plt.plot(imf2)
plt.plot(imf3)
plt.plot(summed)
