from sklearn.datasets import load_boston
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

data=load_boston()
X=data.data
y=data.target

rf=SVR()
rf.fit(X,y)
p=rf.predict(X)
print(mean_squared_error(y,p))
plt.scatter(y,p)
plt.show()

