from sklearn.datasets import load_iris 
iris = load_iris() 
type(iris) 
print(iris.feature_names) 
print(iris.data) 
X=iris.data 
y=iris.target 


from sklearn import svm
model =svm.SVC()

model.fit(X,y) 
print(model.predict([[3,5,4,2]])) 

