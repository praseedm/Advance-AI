import tensorflow as tf

x=tf.zeros([3,4],tf.int32)
y=tf.zeros_like([[2,3],[2,5]],tf.int32)

sess=tf.Session()
output=sess.run(x)

sess2=tf.Session()
output2=sess2.run(y)

print(x)
print(output)
print(y)
print(output2)
sess.close()
sess2.close()
