from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
import matplotlib.pyplot as plt
iris=load_iris()

X=iris.data
y=iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
print(X_train.shape)
print(X_test.shape)
scores=[]
for i in range(1,25):
	knn=KNeighborsClassifier(n_neighbors=i)
	knn.fit(X_train,y_train)
	p=knn.predict(X_test)
	a=accuracy_score(y_test,p)
	scores.append(a)

print(scores)
plt.plot(range(1,25),scores)
plt.xlabel("Value of k")
plt.ylabel("Accuracy score")
plt.show()

