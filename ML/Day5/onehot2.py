import pandas as pd
from sklearn import  preprocessing
le=preprocessing.LabelEncoder()

data=pd.read_csv('banking.csv', delimiter=',')
d=data.as_matrix()
X=d[:,1]
le.fit(X)
k=le.transform(X)
print(k[0:20])
print(X[0:20])


enc =preprocessing.OneHotEncoder()
print(k.shape)
k=k.reshape(-1,1)
print(k.shape)
enc.fit(k)

p=enc.transform(k[0:20])

print(p[0:20])

