import tensorflow as tf  # 导入tensorflow模块
import numpy as np  # 导入numpy模块
import math

# 随机数返回32行2列的矩阵，表示32组 数据作为输入
X = np.arange(0,2*math.pi,0.001)
# 从X这个32行2列的矩阵中取出一行 判断如果小于1 给Y赋值1，如果不小于1 给Y赋值0
# 作为数据数据集的标签（正确答案）,数据标注
Y = [math.sin(i) for i in X]
print('X:\n', X)
print('Y:\n', Y)
Y_=np.array(Y)
# (1) 用placeholder 实现输入定义（sess.run 中喂入一组数据）的情况,特征有体积和重量，数据为体积 0.7、重量 0.5


BATCH_SIZE = 8  # 一次输入网络的数据，称为batch。一次不能喂太多数据



# 1定义神经网络的输入、参数和输出,定义前向传播过程。
x = tf.placeholder(tf.float32, shape=(None, 1))
y_ = tf.placeholder(tf.float32, shape=(None, 1))

w1 = tf.Variable(tf.random_normal([1, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 2定义损失函数及反向传播方法。
loss = tf.reduce_mean(tf.square(y - y_))
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)  # 三种优化方法选择一个就可以
# train_step = tf.train.MomentumOptimizer(0.001,0.9).minimize(loss_mse)
# train_step = tf.train.AdamOptimizer(0.001).minimize(loss_mse)

# 3生成会话，训练STEPS轮
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    # 输出目前（未经训练）的参数取值。
    print("w1:\n", sess.run(w1))
    print("w2:\n", sess.run(w2))
    print("\n")

    # 训练模型。
    STEPS = 3000
    for i in range(STEPS):               #0-2999

        sess.run(train_step, feed_dict={x:X[i], y_:Y_[i]})
        if i % 500 == 0:
            total_loss = sess.run(loss, feed_dict={x: X, y_: Y_})
            print("After %d training step(s), loss on all data is %g"%(i,total_loss))

    # 输出训练后的参数取值。
    print("\n")
    print("w1:\n", sess.run(w1))
    print("w2:\n", sess.run(w2))

