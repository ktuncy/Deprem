import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.stats import skew

df5=pd.read_excel('C:/Users/Asus/Desktop/dışarda.xlsx',usecols=[5])

count = np.array(df5)

mean1 = np.mean(count)
std1 = np.std(count)

p = np.max(count)
d = np.min(count)

pivy = df5.pivot_table(index = ['Unnamed: 5'], aggfunc = 'size')

fig,ax = plt.subplots(figsize=(12,10))

counts,bins1,ignored = plt.hist(count,13,density=True)
plt.plot(bins1,1/(std1*np.sqrt(2*np.pi))*np.exp(-(bins1-mean1)**2/(2*std1**2)),linewidth=2,color='r')
plt.xlim(d,p)
plt.text(3,0.10,'Standard Deviation : 3.5\nMean : 9.1\nSkewness : -0.1\nMin - Max : 2 - 15', fontsize = 15)
plt.show()

print(skew(count, bias=False))
print(mean1)
print(std1)
print(p)
print(d)


