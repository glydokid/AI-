import tensorflow as tf

X = [[0.0, 0.0], [0.1, 1.0], [1.0, 0.0], [1.0, 1.0]]
y = [[-1], [1], [1], [1]]

w = tf.Variable(tf.random.uniform([2,1], -0.5, 0.5)) # 1*2 -=.5~0.5 값 세팅
b = tf.Variable(tf.zeros([1])) #0차원

opt = tf.keras.optimizers.SGD(learning_rate= 0.1)

def forward(): #전방계산
    s = tf.add(tf.matmul(X, w),b)
    o = tf.tanh(s)
    return o

def loss(): #손실함수
    o = forward()
    return tf.reduce_mean((y-o)**2) #오차 제곱

for i in range(500):
    opt.minimize(loss, var_list = [w,b]) #W,b값을 조절하면서 loss값 최소화
    if(i%100 == 0):
        print("loss at rpoch", i , "=", loss().numpy())
        
o =forward() #예측
print(o)