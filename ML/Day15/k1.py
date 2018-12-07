from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

iris=load_iris()
X=iris.data
y=iris.target.reshape(-1,1)


encoder=OneHotEncoder()
y=encoder.fit_transform(y)

model=Sequential()
model.add(Dense(10,input_shape=(4,),activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(3,activation='softmax'))
optimizer=Adam(lr=0.001)

model.compile(optimizer,loss='mean_squared_error',metrics=['accuracy'])
print(model.summary())
model.fit(X,y,verbose=2,epochs=100)
results=model.evaluate(X,y)

print(results[0])

print(results[1])





