#MNIST 데이터 셋으로 확장
from sklearn.datasets import fetch_openml #mnist 데이터 불러오기
from sklearn.neural_network import MLPClassifier
import numpy as np

mnist = fetch_openml('mnist_784') #28x28 = 784픽셀
mnist.data = mnist.data/255.0 #0~255까지 데이들이 너무 방대해서 0~1사이의 수로 정규화 시켜주는 작업
x_train = mnist.data[:60000]; x_test = mnist.data[60000:]
y_train = np.int16(mnist.target[:60000]); y_test = np.int16(mnist.target[60000:]) #np.int16 = 16진수로 받아옴 ->mnist가 string로 되어있기 때문에

mlp = MLPClassifier(hidden_layer_sizes = (100), learning_rate_init = 0.001,
                    batch_size = 512, solver = 'adam', verbose=True) #batch 는 보통 2의 n승으로 설정

mlp.fit(x_train, y_train)

res = mlp.predict(x_test)

conf = np.zeros((10,10))
for i in range(len(res)):
    conf[res[i]][y_test[i]] += 1
print(conf)

correct = 0
for i in range(10):
    correct += conf[i][i]
accuracy = correct / len(res)
print("테스트 집합에 대한 정확률: ", accuracy*100, "%")