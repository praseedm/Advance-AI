import tensorflow as tf
a=tf.constant(5)
b=tf.constant(5)
c=tf.add(a,b,name="add")
sess=tf.Session()
output=sess.run(c)
print(c)
print(output)
print(a)
print(b)

writer=tf.summary.FileWriter('./tfb1',sess.graph)
writer.close()

sess.close()

