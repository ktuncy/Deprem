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

fig,ax = plt.subplots(figsize=(20,20))

plt.subplot(4,2,1)
plt.plot(gas1)
plt.xlabel('GAS1',fontsize = 20)

plt.subplot(4,2,2)
plt.plot(gas2)
plt.xlabel('GAS2',fontsize = 20)

plt.subplot(4,2,3)
plt.plot(system_voltage1)
plt.xlabel('SYSTEM VOLTAGE',fontsize = 20)

plt.subplot(4,2,4)
plt.plot(high_voltage1)
plt.xlabel('HIGH VOLTAGE',fontsize = 20)

plt.subplot(4,2,5)
plt.plot(counts)
plt.xlabel('COUNTS',fontsize = 20)

plt.subplot(4,2,6)
plt.plot(temperature)
plt.xlabel('TEMPERATURE',fontsize = 20)

plt.subplot(4,2,7)
plt.plot(humidity)
plt.xlabel('HUMIDITY',fontsize = 20)

plt.subplot(4,2,8)
plt.plot(pressure)
plt.xlabel('PRESSURE',fontsize = 20) 

#res = stats.linregress(temperature,counts)

#mn = np.min(temperature)
#mx = np.max(temperature)

#x1 = np.linspace(mn,mx,2000)
#y1 = (res.slope*x1) + res.intercept

#plt.style.use('ggplot')
#plt.plot(humidity,gas1,linestyle = (0,(1,10)), linewidth="3")

#plt.plot(x1,y1,'-r')