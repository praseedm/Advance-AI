from sklearn.datasets import load_iris
iris =load_iris()


X=iris.data
y=iris.target

from sklearn.linear_model import LogisticRegression

lg1=LogisticRegression()
lg1.fit(X,y)
print(lg1.predict([[3,5,4,2]]))


