#accuracy score 
#confusion matrix
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score,confusion_matrix 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X=iris.data
y=iris.target
rf=RandomForestClassifier()
#print(rf)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
rf.fit(X_train,y_train)
predictions=rf.predict(X_test)

print (accuracy_score(y_test,predictions))
print(confusion_matrix(y_test,predictions))
