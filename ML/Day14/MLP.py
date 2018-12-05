from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
iris = load_iris()
type(iris)
print(iris.feature_names)
print(iris.data)
X=iris.data
y=iris.target



mlp=MLPClassifier(hidden_layer_sizes=(2))
print(mlp.coefs_)


mlp.fit(X,y)
print(mlp.predict([[3,5,4,2]]))
p=mlp.predict(X)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y,p))

