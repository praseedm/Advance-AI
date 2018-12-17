import numpy as np
import tensorflow as tf
x = tf.placeholder(tf.float32,(3,4))
y =  x 
 
sess = tf.Session()
#print(sess.run(y)) # will cause an error
 
s = np.random.rand(3,4)

k=sess.run(y, feed_dict={x:s})
print(k)

sess.close()
