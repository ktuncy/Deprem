import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA

df6=pd.read_excel('C:/Users/Asus/Desktop/dışarda.xlsx',usecols=[6])
df6.rename(columns = {'Unnamed: 6': 'Temperature'},inplace = True)
                     
msk = (df6.index < len(df6)-10)
df_train = df6[msk].copy()
df_test = df6[~msk].copy()

f = plt.figure(figsize=(15,15))

ax1 = f.add_subplot(3,4,1)
ax1.plot(df_train)

ax2 = f.add_subplot(3,4,2)
ax2.plot(df_train.diff())

ax3 = f.add_subplot(3,4,3)
ax3.plot(df_train.diff().diff())

ax4 = f.add_subplot(3,4,4)
ax4.plot(df_train.diff().diff().diff())

ax11 = f.add_subplot(3,4,5)
plot_acf(df_train.dropna(),ax = ax11)

ax12 = f.add_subplot(3,4,6)
plot_acf(df_train.diff().dropna(),ax=ax12)

ax13 = f.add_subplot(3,4,7)
plot_acf(df_train.diff().diff().dropna(),ax=ax13)

ax14 = f.add_subplot(3,4,8)
plot_acf(df_train.diff().diff().diff().dropna(),ax=ax14)

ax21 = f.add_subplot(3,4,9)
plot_pacf(df_train.dropna(),ax = ax21)

ax22 = f.add_subplot(3,4,10)
plot_pacf(df_train.diff().dropna(),ax=ax22)

ax23 = f.add_subplot(3,4,11)
plot_pacf(df_train.diff().diff().dropna(),ax=ax23)

ax24 = f.add_subplot(3,4,12)
plot_pacf(df_train.diff().diff().diff().dropna(),ax=ax24)

result1 = adfuller(df_train.dropna())
result2 = adfuller(df_train.diff().dropna())
result3 = adfuller(df_train.diff().diff().dropna())
result4 = adfuller(df_train.diff().diff().diff().dropna())

print(' P-value1: ', result1[1])
print(' P-value2: ', result2[1])
print(' P-value3: ', result3[1])
print(' P-value4: ', result4[1])

model = ARIMA(df_train, order=(0,2,1))
model_fit = model.fit()
print(model_fit.summary())

forecast_test = model_fit.forecast(len(df_test))
df6['Forecast Temperature'] = [None]*len(df_train) + list(forecast_test)
df6.plot()

