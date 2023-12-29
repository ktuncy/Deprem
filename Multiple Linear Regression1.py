import pandas as pd
import numpy as np 
import seaborn as sns  
import matplotlib.pyplot as plt 
from sklearn import linear_model

df=pd.read_excel('C:/Users/Asus/Desktop/humidity_sand_mix.xlsx', usecols=range(1,9))
df.rename(columns = {'Unnamed: 1': 'GAS1','Unnamed: 5': 'COUNTS','Unnamed: 6':'TEMPERATURE','Unnamed: 7':'HUMIDITY','Unnamed: 8':'PRESSURE'}, inplace = True)

corr = df[['COUNTS', 'TEMPERATURE', 'HUMIDITY']].corr()

print('Pearson correlation coefficient matrix for each independent variable: \n')  
print(corr)

masking = np.zeros_like(corr, dtype = bool)  
np.fill_diagonal(masking, val = True)
  
figure, axis = plt.subplots(figsize = (4, 3))  
    
c_map = sns.diverging_palette(220, 10, as_cmap = True, sep = 100)  
c_map.set_bad('grey') 
 
sns.heatmap(corr, mask = masking, cmap = c_map, vmin = -1, vmax = 1, center = 1, linewidths = 1)  
figure.suptitle('Heatmap visualizing Pearson Correlation Coefficient Matrix', fontsize = 14)  
axis.tick_params(axis = 'both', which = 'major', labelsize = 10) 
 
#features = ['HUMIDITY']

#X = df[features].values.reshape(-1,len(features))
#y = df['TEMPERATURE'].values

#regr = linear_model.LinearRegression()
#model = regr.fit(X,y)

#predicted = regr.predict([[19.]])

#print('Features                :  %s' % features) 
#print('Predicted Value         :  %.2f' % predicted)
#print('Regression Coefficients : ', [round(item, 2) for item in model.coef_])
#print('R-squared               :  %.2f' % model.score(X, y))
#print('Y-intercept             :  %.2f' % model.intercept_)
