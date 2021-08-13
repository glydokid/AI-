#필기체 데이터
from sklearn import datasets
from matplotlib import pyplot as plt

digit = datasets.load_digits() #digit 객체에 필기데이터 저장

plt.figure(figsize=(3,3)) #그래프 사이즈 설정
plt.imshow(digit.images[13], cmap = plt.cm.gray_r) #13번째 숫자 출력, t색을 그레이로 바꿈 _r은 색반전

plt.show() #실제 화면상에 출력
print(digit.data[13])
print("이 숫자는", digit.target[13],"입니다")