from sklearn import preprocessing
import numpy as np
X_train = np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])
print(X_train)
scaler = preprocessing.StandardScaler().fit(X_train)
print(scaler)

print( scaler.mean_)                                      
                           

print(scaler.transform(X_train))   

