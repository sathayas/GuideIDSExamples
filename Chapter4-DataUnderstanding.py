import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# loading the iris data set
iris = datasets.load_iris()
X = iris.data   # 2D data array
varNames = iris.feature_names  # variable names

# histogram of the petal length
plt.hist(X[:,2])
plt.show()

# histogram with 20 bins
plt.hist(X[:,2], 20)
plt.show()
