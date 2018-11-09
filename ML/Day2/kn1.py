
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.neighbors import KNeighborsClassifier


iris=load_iris()

X=iris.data
y=iris.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20)

print(X_train.shape)
print(X_test.shape)

knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X,y)
p=knn.predict([[3,5,4,2]])
print(p)
print(iris.feature_names)


