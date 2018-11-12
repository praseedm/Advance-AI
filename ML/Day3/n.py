from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import matplotlib.pyplot as plt

iris =load_iris()
X=iris.data
y=iris.target


knn=KNeighborsClassifier(n_neighbors=1)
X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2)

knn.fit(X_train,y_train)
predictions=knn.predict(X_test)

print(predictions)
print(y_test)
print(accuracy_score(y_test,predictions))
print(classification_report(y_test,predictions))
plt.scatter(y_test,predictions)
plt.show()

