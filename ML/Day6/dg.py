import  matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix
data=load_digits()
X=data.images
y=data.target
ilabels=list(zip(X,y))
for index,(image,label) in enumerate(ilabels[:4]):
	plt.subplot(2,4,index+1)
	plt.axis('off')
	plt.imshow(image,cmap=plt.cm.gray_r,interpolation='nearest')
	plt.title(label)
plt.show()
print(X.shape)
n=len(X)
X=X.reshape(n,-1)
print(X.shape)
X_train=X[:n//2]
y_train=y[:n//2]
X_test=X[n//2:]
y_test=y[n//2:]
model=SVC(gamma=0.001)
model.fit(X_train,y_train)
p=model.predict(X_test)

print(y_train.shape)
print(p.shape)
c=classification_report(y_test,p)
print(confusion_matrix(y_test,p))
print(c)


ilabels=list(zip(data.images[n//2:],p))
for index,(image,label) in enumerate(ilabels[:4]):
        plt.subplot(2,4,index+1)
        plt.axis('off')
        plt.imshow(image,cmap=plt.cm.gray_r,interpolation='nearest')
        plt.title(label)
plt.show()

