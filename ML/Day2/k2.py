from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import pandas as pd
train1=pd.read_csv("/home/common/ML/Day2/train.csv",delimiter="\t")
test1=pd.read_csv("/home/common/ML/Day2/test.csv",delimiter="\t")
print(train1)
print(test1)

train=train1.as_matrix()
test=test1.as_matrix()
print(train.shape)
print(test.shape)

knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(train[:,[0,1]],train[:,2])
p=knn.predict(test[:,[0,1]])
print(confusion_matrix(test[:,2],p))
print(knn)
