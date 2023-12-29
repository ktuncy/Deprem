import pandas as pd
import numpy as np
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

gas1=np.array(df1)
gas2=np.array(df2)
system_voltage=np.array(df3)
high_voltage=np.array(df4)
counts=np.array(df5)
temperature=np.array(df6)
humidity=np.array(df7)
pressure=np.array(df8) 

system_voltage1=system_voltage*2*(5./1024.)
high_voltage1=high_voltage*(5./1024.)

fig,ax = plt.subplots(figsize=(13,20))

#plt.subplot(2,1,1)
#plt.plot(temperature[0:1523],humidity[0:1523])
#plt.subplot(2,1,2)
#plt.plot(temperature[1523:7215],humidity[1523:7215])

#plt.subplot(2,1,1)
#plt.plot(temperature[0:1523],gas1[0:1523],'o',ms="3")
#plt.subplot(2,1,2)
#plt.plot(temperature[1523:7215],gas1[1523:7215],'o',ms="3")

#plt.subplot(2,1,1)
#plt.plot(temperature[0:1523],gas2[0:1523],'o',ms="3")
#plt.subplot(2,1,2)
#plt.plot(temperature[1523:7215],gas2[1523:7215],'o',ms="3")

#plt.subplot(2,1,1)
#plt.plot(temperature[0:1523],high_voltage1[0:1523],'o',ms="3")
#plt.subplot(2,1,2)
#plt.plot(temperature[1523:7215],high_voltage1[1523:7215],'o',ms="3")

#plt.subplot(2,1,1) 
#plt.plot(temperature[0:1523],system_voltage1[0:1523],'o',ms="3")
#plt.subplot(2,1,2)
#plt.plot(temperature[1523:7215],system_voltage1[1523:7215],'o',ms="3")

#plt.subplot(2,1,1)
#plt.plot(gas1[0:1523],gas2[0:1523],'o',ms="3")
#plt.subplot(2,1,2)
#plt.plot(gas1[1523:7215],gas2[1523:7215],'o',ms="3")

#plt.subplot(2,1,1)
#plt.plot(gas1[0:1523],high_voltage1[0:1523],'o',ms="3")
#plt.subplot(2,1,2)
#plt.plot(gas1[1523:7215],high_voltage1[1523:7215],'o',ms="3")

#plt.subplot(2,1,1)
#plt.plot(gas2[0:1523],high_voltage1[0:1523],'o',ms="3")
#plt.subplot(2,1,2)
#plt.plot(gas2[1523:7215],high_voltage1[1523:7215],'o',ms="3")

#plt.subplot(2,1,1)
#plt.plot(gas1[0:1523],system_voltage1[0:1523],'o',ms="3")
#plt.subplot(2,1,2)
#plt.plot(gas1[1523:7215],system_voltage1[1523:7215],'o',ms="3")

#plt.subplot(2,1,1)
#plt.plot(gas2[0:1523],system_voltage1[0:1523],'o',ms="3")
#plt.subplot(2,1,2)
#plt.plot(gas2[1523:7215],system_voltage1[1523:7215],'o',ms="3")

#plt.subplot(2,1,1)
#plt.plot(gas1[0:1523],humidity[0:1523],'o',ms="3")
#plt.subplot(2,1,2)
#plt.plot(gas1[1523:7215],humidity[1523:7215],'o',ms="3")

plt.subplot(2,1,1)
plt.plot(gas2[0:1523],humidity[0:1523],'o',ms="3")
plt.subplot(2,1,2)
plt.plot(gas2[1523:7215],humidity[1523:7215],'o',ms="3")
