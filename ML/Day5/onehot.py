from sklearn import preprocessing
enc = preprocessing.OneHotEncoder()
X=[[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]]
enc.fit(X)  
Y=enc.transform(X)
print(Y.toarray())

