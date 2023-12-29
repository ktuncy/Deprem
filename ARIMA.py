import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA

df6=pd.read_excel('C:/Users/Asus/Desktop/deprem.xlsx',usecols=[2])

f = plt.figure(figsize=(15,15))

ax1 = f.add_subplot(3,4,1)
ax1.plot(df6)

ax2 = f.add_subplot(3,4,2)
ax2.plot(df6.diff())

ax3 = f.add_subplot(3,4,3)
ax3.plot(df6.diff().diff())

ax4 = f.add_subplot(3,4,4)
ax4.plot(df6.diff().diff().diff())

ax11 = f.add_subplot(3,4,5)
plot_acf(df6.dropna(),ax = ax11)

ax12 = f.add_subplot(3,4,6)
plot_acf(df6.diff().dropna(),ax=ax12)

ax13 = f.add_subplot(3,4,7)
plot_acf(df6.diff().diff().dropna(),ax=ax13)

ax14 = f.add_subplot(3,4,8)
plot_acf(df6.diff().diff().diff().dropna(),ax=ax14)

ax21 = f.add_subplot(3,4,9)
plot_pacf(df6.dropna(),ax = ax21)

ax22 = f.add_subplot(3,4,10)
plot_pacf(df6.diff().dropna(),ax=ax22)

ax23 = f.add_subplot(3,4,11)
plot_pacf(df6.diff().diff().dropna(),ax=ax23)

ax24 = f.add_subplot(3,4,12)
plot_pacf(df6.diff().diff().diff().dropna(),ax=ax24)

result1 = adfuller(df6.dropna())
result2 = adfuller(df6.diff().dropna())
result3 = adfuller(df6.diff().diff().dropna())
result4 = adfuller(df6.diff().diff().diff().dropna())

print(' p-value: ', result1[1])
print(' p-value: ', result2[1])
print(' p-value: ', result3[1])
print(' p-value: ', result4[1])

arima_model = ARIMA(df6, order = (0,0,1))
model = arima_model.fit()
msk = (df6.index < len(df6)-100)
df_train = df6[msk].copy()
df_test = df6[~msk].copy()
forecast_test = model.forecast(len(df_test))
df6['forecast'] = [None]*len(df_train) + list(forecast_test)
df6.plot()
print(model.summary())
