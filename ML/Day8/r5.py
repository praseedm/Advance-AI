#accuracy score 
#confusion matrix
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.linear_model import Lasso 
import matplotlib.pyplot  as plt
data = load_boston()
X=data.data
y=data.target
rf=SVR()

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
rf.fit(X_train,y_train)
predictions=rf.predict(X_test)
print (mean_squared_error(y_test,predictions))
plt.scatter(y_test,predictions)
plt.show()
