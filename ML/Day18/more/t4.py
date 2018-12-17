import tensorflow as tf
sess=tf.Session()
print(sess.run(tf.div(3,4)))
print(sess.run(tf.truediv(3,4)))
print(sess.run(tf.floordiv(3.0,4.0)))
print(sess.run(tf.mod(22.0,5.0)))
print(sess.run(tf.cross([1.,0.,0.],[0.,1.,0.])))
print(sess.run(tf.sin(3.1416)))
print(sess.run(tf.cos(3.1416)))
print(sess.run(tf.tan(3.1416/4)))

def ploy(x):
	return(tf.subtract(3*tf.square(x),x)+10)
	#return(tf.subtract(x,x)+x)

for n in range(1,12):
	print(sess.run(ploy(n)))

writer=tf.summary.FileWriter('tfb3',sess.graph)
	
sess.close()
