# Standardize the data attributes for the Iris dataset.
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier


from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
# load the Iris dataset
iris = load_iris()
print(iris.data.shape)
# separate the data and target attributes
X = iris.data
y = iris.target
# standardize the data attributes
s_X = preprocessing.normalize(X)

print(s_X)
knn1=KNeighborsClassifier(n_neighbors=3)
knn2=KNeighborsClassifier(n_neighbors=3)
knn1.fit(X,y)
knn2.fit(s_X,y)
y_pred1=knn1.predict(X)
y_pred2=knn2.predict(s_X)

print(confusion_matrix(y,y_pred1))
print(confusion_matrix(y,y_pred2))

