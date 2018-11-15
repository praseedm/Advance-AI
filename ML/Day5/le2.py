import pandas as pd
data=pd.read_csv("train.csv",delimiter="\t")
# Importing LabelEncoder and initializing it
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
for col in data.columns.values:
       # Encoding only categorical variables
	if data[col].dtypes=='object':
	    	le.fit(data[col].values)
       		data[col]=le.transform(data[col])
print(data)
