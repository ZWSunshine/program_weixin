from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn import cluster
import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(100, 2)
estimator = KMeans(n_clusters=3)
res = estimator.fit_predict(data)
lable_pred = estimator.labels_
centroids = estimator.cluster_centers_
inertia = estimator.inertia_
# print res
print(lable_pred)
print(centroids)
print(inertia)


for i in range(len(data)):
    if int(lable_pred[i]) == 0:
        plt.scatter(data[i][0], data[i][1], color='red')
    if int(lable_pred[i]) == 1:
        plt.scatter(data[i][0], data[i][1], color='black')
    if int(lable_pred[i]) == 2:
        plt.scatter(data[i][0], data[i][1], color='blue')
plt.show()
