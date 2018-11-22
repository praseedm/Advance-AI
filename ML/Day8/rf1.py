from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

data=load_iris()
X=data.data
y=data.target
rf=RandomForestClassifier()
rf.fit(X,y)
p=rf.predict(X)
print(confusion_matrix(y,p))
