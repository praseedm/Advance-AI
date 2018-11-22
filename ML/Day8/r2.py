#accuracy score 
#confusion matrix
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error,mean_absolute_error 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot  as plt
data = load_boston()
X=data.data
y=data.target
print(data.feature_names)
print(X.shape)
print(X[:,1:10])
print(y)
rf=RandomForestRegressor()

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
rf.fit(X_train,y_train)
predictions=rf.predict(X_test)
print (mean_squared_error(y_test,predictions))
print (mean_absolute_error(y_test,predictions))
plt.scatter(y_test,predictions)
plt.show()
