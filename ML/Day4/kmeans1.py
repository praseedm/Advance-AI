from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,accuracy_score

X,y_true=make_blobs(n_samples=300,centers=4,cluster_std=0.60)
kmeans=KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans=kmeans.predict(X)


#print(y_true)
plt.scatter(X[:,0],X[:,1],s=50)
plt.show()

plt.scatter(X[:,0],X[:,1],s=50,c=y_kmeans,cmap='viridis')
plt.show()


print(confusion_matrix(y_true,y_kmeans))
