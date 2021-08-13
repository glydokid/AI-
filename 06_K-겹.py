from sklearn import datasets 
from sklearn import svm
from sklearn.model_selection import cross_val_score

digit = datasets.load_digits()
s= svm.SVC(gamma = 0.001)

for i in range(5,11):
    accuracies = cross_val_score(s, digit.data, digit.target, cv=i) #cv= k겹 -> 5겹
    print(accuracies)
    print("평균정확률: ", accuracies.mean()*100,"%" )