from sklearn import datasets
from sklearn import svm
# import matplotlib.pypot as plt

iris = datasets.load_iris()
# print(iris.DESCR)

# Ще използваме Support Vector Machine

scv = svm.SVC()
print(scv.fit(iris.data[:-3], iris.target[:-3])) # Всяко трениране се извършва с fit метод
# за [6.2, 3.4, 5.4, 2.3] получаваме на Y 0 или 1

print(iris.data[-3:])

print('Predicted')
# print(scv.predict(iris[-3:]))

# plt.figure(1, figsize=(3, 3))
# plt.imshow(iris.images[-1], cmap=plt.cm.gray, interpolation='nearest')

from sklearn import preprocessing
import numpy as np

X_train = np.array([[1., -1, 2.], [2.]])

scaler = preprocessing.StandardScaler().fit(iris.data[:10])
print('Transform')
print(scaler.transform(iris.data[:10]))

