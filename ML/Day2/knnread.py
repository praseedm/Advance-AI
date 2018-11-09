
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
train1=pd.read_csv('train.csv' ,delimiter ='\t')
test1=pd.read_csv('test.csv', delimiter ='\t')

train = train1.as_matrix()
test =test1.as_matrix()
print(train)
print(test)

X_train,X_test,y_train,y_test = train[:,[0,1]],test[:,[0,1]],train[:,[2]],test[:,[2]]
knn=KNeighborsClassifier(n_neighbors=3,weights='distance')

print(X_train)

print(X_test)
print(y_train)
print(y_test)
knn.fit(X_train,y_train)
predictions=knn.predict(X_test)
print(predictions)
print(y_test)
