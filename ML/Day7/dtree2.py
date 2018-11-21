from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score,KFold
iris=load_iris()
X=iris.data
y=iris.target
kfold=KFold(n_splits=10,random_state=7)
tree1=DecisionTreeClassifier()
a=cross_val_score(tree1,X,y,cv=kfold)
print(a)

