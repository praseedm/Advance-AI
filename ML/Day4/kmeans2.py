from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,accuracy_score
import pandas as pd
import numpy as np

data=pd.read_csv('xclara.txt',delimiter='\t')
f1=data['V1'].values
f2=data['V2'].values
X=np.array(zip(f1,f2))



kmeans=KMeans(n_clusters=3)
kmeans.fit(X)
y_kmeans=kmeans.predict(X)


plt.scatter(X[:,0],X[:,1],s=50)
plt.show()
centers=kmeans.cluster_centers_


plt.scatter(X[:,0],X[:,1],s=50,c=y_kmeans,cmap='viridis')
plt.scatter(centers[:,0],centers[:,1],s=200,c='red')
plt.show()


