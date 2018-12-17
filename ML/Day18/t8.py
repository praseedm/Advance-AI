import tensorflow as tf
p1= tf.placeholder(tf.float32)
p2= tf.placeholder(tf.float32)

sess=  tf.Session() 
sess.run(tf.global_variables_initializer())
psum=tf.add_n([p1,p2])
print(sess.run(psum,feed_dict={p1:10,p2:20}))
sess.close()



	
