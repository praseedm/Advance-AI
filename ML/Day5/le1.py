from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(["paris", "paris", "tokyo", "amsterdam"])
k=le.transform(["tokyo", "tokyo", "paris"])

print(k)



