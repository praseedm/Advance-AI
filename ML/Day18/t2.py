import tensorflow as tf
a=tf.constant([[1,1,1],[1,1,1]],name="a")
b=tf.constant([[1,1,1],[1,1,1]],name="b")
c=tf.reduce_sum(a,0)
sess=tf.Session()
output=sess.run(a)
print(a)
print(output)
print(b)
sess.close()

