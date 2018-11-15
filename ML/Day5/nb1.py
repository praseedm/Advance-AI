from sklearn import datasets
from sklearn.metrics import confusion_matrix
iris = datasets.load_iris()
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
print(confusion_matrix(iris.target,y_pred))
