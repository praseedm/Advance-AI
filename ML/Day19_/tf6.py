#https://medium.com/@saxenarohan97/intro-to-tensorflow-solving-a-simple-regression-problem-e87b42fd4845
import tensorflow as tf
from sklearn.datasets import load_boston
from sklearn.preprocessing import scale
from matplotlib import pyplot as plt

# Get the data
total_features, total_prices = load_boston(True)
print(total_prices.shape)
# Keep 300 samples for training
train_features = scale(total_features[:300])
train_prices = total_prices[:300]

# Keep 100 samples for validation
valid_features = scale(total_features[300:400])
valid_prices = total_prices[300:400]

# Keep remaining samples as test set
test_features = scale(total_features[400:])
test_prices = total_prices[400:]


t_f = scale(total_features[499:])
t_p = total_prices[499:]

w = tf.Variable(tf.truncated_normal([13, 1], mean=0.0, stddev=1.0, dtype=tf.float64),name="w")
b = tf.Variable(tf.zeros(1, dtype = tf.float64),name="b")


def calc(x, y):

# Returns predictions and error

	predictions = tf.add(b, tf.matmul(x, w),name="addition")
	error = tf.reduce_mean(tf.square(y - predictions),name="sum")

	return [ predictions, error ]

y, cost = calc(train_features, train_prices)

# Feel free to tweak these 2 values:

learning_rate = 0.025

epochs = 3000

points = [[], []] # You'll see later why I need this


init = tf.global_variables_initializer()
optimizer = tf.train.GradientDescentOptimizer(learning_rate,name="optz").minimize(cost)

with tf.Session() as sess:

    sess.run(init)
    print(sess.run(w))
    print(sess.run(b))
    for i in list(range(epochs)):

        sess.run(optimizer)

        if i % 10 == 0.:
            points[0].append(i+1)
            points[1].append(sess.run(cost))

        if i % 100 == 0:
            print(sess.run(cost))

    plt.plot(points[0], points[1], 'r--')
    plt.axis([0, epochs, 50, 600])
    plt.show()

    print(sess.run(w))
    valid_cost = calc(valid_features, valid_prices)[1]

    print('Validation error =', sess.run(valid_cost), '\n')

    test_cost = calc(test_features, test_prices)[1]

    print('Test error =', sess.run(test_cost), '\n')

'''''''''''''
    t_cost =calc(t_f,t_p)[1]
    print('Final Error =',sess.run(t_cost))
    predictions = tf.add(b, tf.matmul(t_f, w),name="new")
    print(t_p)
    print(sess.run(predictions))

''''''''''''''
writer= tf.summary.FileWriter('./tfb1',sess.graph)
writer.close()




