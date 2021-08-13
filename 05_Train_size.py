#정확률 계산 데이터를 훈련집합+테스트집합 으로 나누어서 학습, 예측수행 -> 일반화를 높이기 위해서->새로운 데이터가 들어와도 값을 낸다
from sklearn import datasets 
from sklearn import svm #svm모델을 사용하여 학습
from sklearn.model_selection import train_test_split
import numpy as np #매트릭스를 만들기위해

digit = datasets.load_digits() #데이터 받아오는 부분
x_train, x_test, y_train, y_test = train_test_split(digit.data, digit.target, train_size=0.6) #피처와 라벨, train_size를 60퍼 쓰겠다

s = svm.SVC(gamma=0.001)
s.fit(x_train, y_train) #학습(모델링) 피처와 라벨

res = s.predict(x_test)

conf = np.zeros((10,10)) #10x10의 매트릭스 만들기
for i in range(len(res)): 
    conf[res[i]][y_test[i]] += 1 #res = 예측값, y_test = 실제값
print(conf)

correct = 0 #맞은 부분만 더해서 값을 냄
correct += conf[i][i]
accuracy = correct/len(res)
print("Accuracy is", accuracy*100, "%.")