from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

from sklearn.datasets import load_iris
from sklearn.preprocessing import OneHotEncoder

iris=load_iris()
X=iris.data
y=iris.target.reshape(-1,1)

encoder= OneHotEncoder()
y=encoder.fit_transform(y)

model=Sequential()
model.add(Dense(4,input_shape=(4,),activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(3,activation='softmax'))
optimizer=Adam(lr=0.001)

print(model.summary())
model.compile(optimizer,loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(X,y,batch_size=5,verbose=2,epochs=100)
results=model.evaluate(X,y)
print(results[0])
print(results[1])








