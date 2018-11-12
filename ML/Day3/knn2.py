from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import accuracy_score,confusion_matrix

iris =load_iris()
X=iris.data
y=iris.target


knn=KNeighborsClassifier(n_neighbors=1)
#X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2)

score=cross_val_score(knn,X,y,cv=20)
print(score)
#knn.fit(X_train,y_train)
#predictions=knn.predict(X_test)
'''
print(predictions)
print(y_test)
print(accuracy_score(y_test,predictions))
print(confusion_matrix(y_test,predictions))
'''

