#iris 데이터 셋 읽기 기계학습 적용(원리)
from sklearn import datasets

d=datasets.load_iris() #iris 데이터 셋을 읽고
print(d.DESCR) #내용출력

for i  in range(0,len(d.data)): #샘플을 순서대로 출력
    print(i+1,d.data[i],d.target[i])
from sklearn import svm

s = svm.SVC(gamma=0.14, C=10) #svm 분류 모델 SVC 객체 생성하고
s.fit(d.data, d.target) #iris 데이터로 학습

new_d = [[6.4 ,3.2, 6.0, 2.5],[7.1, 3.1, 4.7, 1.35]] #101번째와 51번째 샘플을 변형하여 새로운 데이터 생성
res=s.predict(new_d)
print("새로운 2개의 샘플의 부류는",res)


#데이터 그래프화
import plotly.express as px

df = px.data.iris() #iris 데이터 불러오기
fig = px.scatter_3d(df, x='sepal_length', y='petal_length', z='petal_width', color = 'species')
fig.show(renderer="browser") #브라우져로 보여줌
