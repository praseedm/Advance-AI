from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint

import numpy 
seed=7
numpy.random.seed(seed)
dataset=numpy.loadtxt("pimaindians.csv",delimiter=",")
X=dataset[:,0:8]
Y=dataset[:,8]


model= Sequential()
model.add(Dense(12,input_dim=8,kernel_initializer="uniform",activation="relu"))
model.add(Dense(8,kernel_initializer='uniform',activation='relu'))
model.add(Dense(1,kernel_initializer='uniform',activation='sigmoid'))
model.load_weights("weights-best.hdf5")
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

filepath="weights-best.hdf5"
checkpoint=ModelCheckpoint(filepath,monitor='val_acc',verbose=1,save_best_only=True,mode="max")
callbacks_list=[checkpoint]
model.fit(X,Y,validation_split=0.33,epochs=30,batch_size=10,callbacks=callbacks_list,verbose=0)

