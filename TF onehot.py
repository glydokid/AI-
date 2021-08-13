import tensorflow as tf
import tensorflow.keras.datasets as ds

(x_train, y_train),(x_test, y_test) = ds.mnist.load_data() #load_data를 통해(x_train, y_train),(x_test, y_test)에 넣기
yy_train = tf.one_hot(y_train, 10, dtype = tf.int8) #on_hot-> 벡터로 표현 -> yy에 넣기
print("MNIST:", x_train.shape, y_train.shape, yy_train.shape)


(x_train, y_train),(x_test, y_test) = ds.cifar10.load_data()
yy_train = tf.one_hot(y_train, 10, dtype = tf.int8)
print("CIFAR-10:", x_train.shape, y_train.shape, yy_train.shape)