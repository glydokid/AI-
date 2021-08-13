import tensorflow as tf
import numpy as np

t = tf.random.uniform([2,3],0,1)
n = np.random.uniform(0,1,[2,3])

print("tensorflow로 생성한 텐서: \n",t,"\n")
print("numpy로 생성한 어레이: \n", n,"\n")

sum = t + n
print("덧셈:\n",sum)