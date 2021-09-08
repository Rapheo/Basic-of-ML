import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
# import mglearn

from sklearn.model_selection import train_test_split

from sklearn.datasets import load_iris
iris_dataset = load_iris()

# print(iris_dataset['data'])
# print(iris_dataset['data'].shape) #(150,4) row, colomn
# print(iris_dataset['data'][:10]) #first 10 values
# print(iris_dataset['data'][0])
# Stratified will take all the target value not leaving any unique one taking the ratio from train set
# Stratify ~ classify takes all unique values atleast once from the target or label 1,2,4,5,1,2,3 will split with 1,2,3,4,5 and will leave any unique values



# df2 = pd.DataFrame(np.array([[23, 99, 78], [65, 95, 90], [90, 98, 96]]),columns=['krish', 'ishwar', 'raj'])
# print(df2)

y = pd.DataFrame(iris_dataset['target'])
print(y,"k")

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], test_size = 0.8, stratify = y, random_state = 0)
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)

print("X_test shape:", X_test.shape)
print("y_train shape:", y_test.shape)

# iris_dataframe_train = pd.DataFrame(X_train, columns = iris_dataset.feature_names)
# #scatter matrix, color by y_train
# pd.plotting.scatter_matrix(iris_dataframe_train, c = y_train, figsize=(12, 12),marker = 'o', hist_kwds={'bins':20}, s = 60,alpha=1)
# plt.show()

# fig,ax = plt.subplots()
# ax.hist(y_train)
# ax.set_title('Frequency of classes')
# ax.set_xlabel('class label')
# ax.set_ylabel('no of flowers')
# plt.show()

# mglearn.plots.plot_knn_classification(n_neighbors = 3)
# plt.show()

knn = KNeighborsClassifier(n_neighbors = 4)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print(y_pred)
print(y_test)

count = 0
for i in range(len(y_test)):
    if y_pred[i] != y_test[i]:
        count = count + 1
        print("x")
error = count / len(y_pred)
print("Error = %f" % (error*100) + '%')
accuracy = (1-error)
print("Accuracy = %f" % (accuracy*100) + '%')

print("Test set score: {:.2f}".format(knn.score(X_test, y_test))) #same as the for loop above

print("Test set score :{:.2f}".format(np.mean(y_pred == y_test)))