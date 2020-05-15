import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import AgglomerativeClustering

# Loading the iris data
iris = datasets.load_iris()
X = iris.data  # array for the features
y = iris.target  # array for the target
feature_names = iris.feature_names   # feature names
target_names = iris.target_names   # target names


#
# HIEAARCHICAL CLUSTERING
#

# Hierarchical clustering
hc = AgglomerativeClustering(n_clusters=3, linkage='ward')
hc.fit(X)  # actually fitting the data
y_clus = hc.labels_   # clustering info resulting from hieararchical

# Plotting the clusters
plt.scatter(X[:,3],X[:,0],c=y_clus,marker='+')
plt.show()


#
#  DENDROGRAM
#

from scipy.cluster.hierarchy import dendrogram, linkage

D = linkage(X, 'ward')
dn = dendrogram(D)
plt.show()
