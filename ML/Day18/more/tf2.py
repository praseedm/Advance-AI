import tensorflow as tf
a=tf.Variable(2,name="scalar")
a_times_two=a.assign(a*2)
init = tf.global_variables_initializer()


with tf.Session() as sess:
	sess.run(init)
	sess.run(a_times_two)
	sess.run(a_times_two)
	print(sess.run(a_times_two))
'''

W=tf.Variale(10)
with tf.Session() as sess:
	sess.run(W.initializer)
	print(sess.run(W.assign_add(10))
#	print(sess.run(W.assign_sub(2))
'''
