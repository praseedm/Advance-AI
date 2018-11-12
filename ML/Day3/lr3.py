import pandas as pd
from sklearn.linear_model import LinearRegression

from sklearn.cross_validation import train_test_split
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("/home/vimala/mypython/Advertising.csv",index_col=0)
print(data.head())
feature_cols1 = ['TV','radio','newspaper']
feature_cols2 = ['TV','radio']
X1=data[feature_cols1]

X2=data[feature_cols2]

#print(X.head())

y=data['sales']
#print(y) 

X_train1,X_test1,y_train1,y_test1=train_test_split(X1,y,test_size=0.4,random_state=4)

X_train2,X_test2,y_train2,y_test2=train_test_split(X2,y,test_size=0.4,random_state=4)
linreg1=LinearRegression()
linreg2=LinearRegression()
linreg1.fit(X_train1,y_train1)
linreg2.fit(X_train2,y_train2)
#print(linreg.coef_)
#print(linreg.intercept_)



y_pred1=linreg1.predict(X_test1)
y_pred2=linreg2.predict(X_test2)
#print(y_pred)
#print(y_test)


#print(y_pred.shape)
#print(y_test.shape)




#scores.append(metrics.accuracy_score(y_test,y_pred))

#print("Accuracy")
print("Absolute Error")
print("Mean Squared Error")
print("Root Mean Squared Error")

#print( metrics.accuracy_score(y_test,y_pred))
print( metrics.mean_absolute_error(y_test1,y_pred1))
print( metrics.mean_absolute_error(y_test2,y_pred2))
print( metrics.mean_squared_error(y_test1,y_pred1))
print( metrics.mean_squared_error(y_test2,y_pred2))
print( np.sqrt(metrics.mean_squared_error(y_test1,y_pred1)))
print( np.sqrt(metrics.mean_squared_error(y_test2,y_pred2)))

plt.scatter(y_test1,y_pred1)
plt.show()

