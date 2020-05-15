import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

# Loading the iris data
iris = datasets.load_iris()
X = iris.data  # array for the features
y = iris.target  # array for the target
feature_names = iris.feature_names   # feature names
target_names = iris.target_names   # target names

# z-score normalization using fit_transform method
X_norm = StandardScaler().fit_transform(X)


#
# HIEAARCHICAL CLUSTERING
#

# Hierarchical clustering
hc = AgglomerativeClustering(n_clusters=3, linkage='ward')
hc.fit(X_norm)  # actually fitting the data
y_clus = hc.labels_   # clustering info resulting from hieararchical

# Plotting the clusters
plt.scatter(X_norm[:,3],X_norm[:,0],c=y_clus,marker='+')
plt.show()


#
#  DENDROGRAM
#

from scipy.cluster.hierarchy import dendrogram, linkage

D = linkage(X_norm, 'ward')
dn = dendrogram(D)
plt.show()
