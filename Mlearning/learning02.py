import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

x = tf.placeholder(tf.float32,[None,784])

# 初始化变量
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

# 创建模型
y = tf.nn.softmax(tf.matmul(x,W)+b)

# 计算交叉熵
y_ = tf.placeholder("float",[None,10])
cross_entropy = -tf.reduce_sum(y_*tf.log(y))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        batch_xs,batch_ys = mnist.train.next_batch(100)
        sess.run(train_step,feed_dict={x: batch_xs,y_: batch_ys})

    correct_prediction = tf.equal(tf.argmax(y_,1),tf.argmax(y,1))
    # bool值转为float,再取平均
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,"float"))
    print(sess.run(accuracy,feed_dict={x: mnist.test.images,y_: mnist.test.labels}))