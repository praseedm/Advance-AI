import tensorflow as tf

k=tf.linspace(10.0,20.0,3,name="l")


sess=tf.Session()
p=tf.range(10,40,2)

output=sess.run(p)
print(output)
print(k)
sess.close()
