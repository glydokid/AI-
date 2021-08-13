from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

X = [[0.0, 0.0], [0.1, 1.0], [1.0, 0.0], [1.0, 1.0]]
y = [[-1], [1], [1], [1]]

n_input = 2
n_output = 1

perceptron = Sequential()
perceptron.add(Dense(units = n_output, activation='tanh', input_shape = (n_input,),
                     kernel_initializer='random_uniform', bias_initializer= 'zero'))

perceptron.compile(loss = 'mse', optimizer = SGD(learning_rate= 0.1), metrics=['mse'])
perceptron.fit(X,y, epochs = 500, verbose= 2)

res = perceptron.predict(X)
print(res)