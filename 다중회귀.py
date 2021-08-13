#다중 회귀
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
 
x1data = [73,93,90,95,72,74] # 모의고사 점수 
x2data = [80,88,92,98,66,81] # 모의고사 점수 
x3data = [75,92,90,100,70, 76] # 모의고사 점수 
ydata = [152,185,180,195,140,7] # 수능 점수 

x1 = tf.placeholder(tf.float32)
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

w1 = tf.Variable(tf.random_normal([1]))
w2 = tf.Variable(tf.random_normal([1]))
w3 = tf.Variable(tf.random_normal([1]))
b = tf.Variable(tf.random_normal([1]))

# 가설함수 
hf = x1*w1 + x2 * w2 + x3 * w3 + b 

# 비용함수
cost = tf.reduce_mean(tf.square(hf - y))

# 트레이닝 
opt = tf.train.GradientDescentOptimizer(0.00001)
train = opt.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cv, hfv, _ = sess.run([cost, hf, train], feed_dict={x1:x1data, x2:x2data, x3:x3data , y:ydata})
    if step%10==0:
        print(step,"cost:",cv, "\n prediction:",hfv)