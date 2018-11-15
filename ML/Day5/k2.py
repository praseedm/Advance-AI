from sklearn import preprocessing
import pandas as pd

data=pd.read_csv("train.csv",delimiter="\t")
le=preprocessing.LabelEncoder()
for col  in data.columns.values:
	if data[col].dtypes=='object':
		le.fit(data[col].values)
		data[col]=le.transform(data[col])


print(data)


