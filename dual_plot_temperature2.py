import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1=pd.read_excel('C:/Users/Asus/Desktop/temperature2.xlsx',usecols=[1])
df2=pd.read_excel('C:/Users/Asus/Desktop/temperature2.xlsx',usecols=[2])
df3=pd.read_excel('C:/Users/Asus/Desktop/temperature2.xlsx',usecols=[3])
df4=pd.read_excel('C:/Users/Asus/Desktop/temperature2.xlsx',usecols=[4])
df5=pd.read_excel('C:/Users/Asus/Desktop/temperature2.xlsx',usecols=[5])
df6=pd.read_excel('C:/Users/Asus/Desktop/temperature2.xlsx',usecols=[6])
df7=pd.read_excel('C:/Users/Asus/Desktop/temperature2.xlsx',usecols=[7])
df8=pd.read_excel('C:/Users/Asus/Desktop/temperature2.xlsx',usecols=[8])

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

fig,ax = plt.subplots(figsize=(13,13))

font1 = {'family':'serif','color':'black','size':20}
font2 = {'family':'serif','color':'black','size':20}

plt.plot(temperature[0:454],humidity[0:454])
plt.xlabel("TEMPERATURE",fontdict=font1)
plt.ylabel("HUMIDITY",fontdict=font2)



