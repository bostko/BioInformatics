from sklearn import datasets
from sklearn import preprocessing
from sklearn import svm

iris = datasets.load_iris()

svc = svm.SVC() # NB същия метод за скалиране на въпросите (потребителските данни)
X_normalized = preprocessing.normalize(iris.data[:10], norm='l2')
print(X_normalized)

print("OrdinalEncoder")
enc = preprocessing.OrdinalEncoder()
X = [['male', 'from US', 'uses Safari'], ['female', 'from Europe', 'uses Firefox']]

X_train = enc.transform([['female', 'from US', 'uses Safari']])
# Пример: линейна регресия
# Сплитване на датасет
# GroupKFold
# https://scikit-learn.org/stable/modules/classes#module-sklearn.model_selection
# train test split използва Shuffle

# Представя графика
# Cross validation извършваме за да видим до каква степен нашия модел наистина е предиктнал правилно
# Coefficient of determination
# Всеки модел има метод score r2_score
# Validating
# SUPERVISED learning
# при медицински данни НЕ ни трябва deep learning
# защото
#
# Unsupervised - deep learning
#
# н на брой