from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from keras.wrappers.scikit_learn import KerasRegressor
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

iris=load_boston()
X=iris.data
y=iris.target#.reshape(-1,1)


def b_model():
	model=Sequential()
	model.add(Dense(13,input_shape=(13,),kernel_initializer='normal',activation='relu'))
#model.add(Dense(10,activation='relu'))
	model.add(Dense(1,kernel_initializer='normal'))
	optimizer=Adam(lr=0.001)

	model.compile(optimizer,loss='mean_squared_error',metrics=['accuracy'])
	return model

estimator=KerasRegressor(build_fn=b_model,epochs=10)
kfold=KFold(n_splits=10,random_state=7)
results=cross_val_score(estimator,X,y,cv=kfold)
print(results.mean())


print(model.summary())
model.fit(X,y,verbose=2,epochs=100)
results=model.evaluate(X,y)
print("results")
print(results[0])

print(results[1])





