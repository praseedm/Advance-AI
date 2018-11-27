from sklearn.preprocessing import normalize,scale
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd
train1=pd.read_csv('Immunotherapy.csv' )
 

train=train1.as_matrix()
test =train1.as_matrix()
print(train)
print(test)

X_train,X_test,y_train,y_test = train[:,0:7],test[:,0:7],train[:,7],test[::,7]
X_train,X_test,y_train,y_test =train_test_split(train[:,0:7],train[:,7])
knn=KNeighborsClassifier(n_neighbors=3,weights='distance')


X_train1=scale(X_train)
X_test1=scale(X_test)


print(X_train)
print(X_test)
knn.fit(X_train,y_train)
predictions=knn.predict(X_test)
print(mean_squared_error(y_test,predictions))


knn.fit(X_train1,y_train)
predictions=knn.predict(X_test1)
print(mean_squared_error(y_test,predictions))


