import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats

df1=pd.read_excel('C:/Users/Asus/Desktop/temperature.xlsx',usecols=[1])
df2=pd.read_excel('C:/Users/Asus/Desktop/temperature.xlsx',usecols=[2])
df3=pd.read_excel('C:/Users/Asus/Desktop/temperature.xlsx',usecols=[3])
df4=pd.read_excel('C:/Users/Asus/Desktop/temperature.xlsx',usecols=[4])
df5=pd.read_excel('C:/Users/Asus/Desktop/temperature.xlsx',usecols=[5])
df6=pd.read_excel('C:/Users/Asus/Desktop/temperature.xlsx',usecols=[6])
df7=pd.read_excel('C:/Users/Asus/Desktop/temperature.xlsx',usecols=[7])
df8=pd.read_excel('C:/Users/Asus/Desktop/temperature.xlsx',usecols=[8])

victor = []
vitoria = []
victoria = []
victory = []
vimeo = []

b = 0
c = 0
im = 0

pivy = df1.pivot_table(index = ['Unnamed: 0'], aggfunc = 'size')
pivy = np.array(pivy.values.tolist())

# x ekseni

for m in range(0,7979):
    if gas1[m] != gas1[m+1]:
        vimeo.append(gas1[m]) 
      
vimeo = np.array(vimeo)
vimeo1 = np.insert(vimeo,72,616)

# y ekseni 
   
for i in range(0,73):
        b = b + pivy5[i]
        victor.append(b)

victor = np.array(victor)

for j in range(0,73):
    while im < victor[j]:
        c = c + temperature[im]
        im = im + 1 
    vitoria.append(c)
    
vitoria = np.array(vitoria)

for k in range(1,73):
     d = vitoria[k] - vitoria[k-1]
     victoria.append(d)

victoria = np.array(victoria)
victoria1 = np.insert(victoria,0,618.)
   
victory = victoria1/pivy0

res = stats.linregress(vimeo1,victory)

mn = np.min(vimeo1)
mx = np.max(vimeo1)

pivy = np.linspace(mn,mx,73)
y1 = (res.slope*pivy) + res.intercept

fig,ax = plt.subplots(figsize=(10,10))

plt.plot(vimeo1,victory,'o')
plt.xlabel('GAS1',fontsize = 20)
plt.ylabel('TEMPERATURE',fontsize = 20)
plt.plot(pivy,y1,'-r')

