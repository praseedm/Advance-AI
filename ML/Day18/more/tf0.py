import tensorflow as tf
a=tf.constant(5)
b=tf.constant(15)
c=tf.multiply(a,b,name="c")

sess=tf.Session()
output=sess.run(c)
print(c)
print(output)


writer=tf.summary.FileWriter('./tfb1',sess.graph)
writer.close()

sess.close()
