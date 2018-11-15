from sklearn import preprocessing
le=preprocessing.LabelEncoder()

le.fit(["kochi","tvm","calicut","calicut"])
k=le.transform(["kochi","calicut","tvm"])
print(k)


