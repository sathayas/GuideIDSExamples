import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

# loading the iris data set
iris = datasets.load_iris()
X = pd.DataFrame(iris.data)   # 2D data array
X.columns = ['sepal length', 'sepal width', 'petal length', 'petal width']


#
# HISTOGRAMS
#

# histogram of the petal length
plt.hist(X['petal length'])
plt.show()

# histogram with 20 bins
plt.hist(X['petal length'], 20)
plt.show()


#
# BOXPLOTS
#

# box plot of the petal length
X.boxplot(column='petal length')
plt.show()

# box plot of the petal length & width
X.boxplot(column=['petal length', 'petal width'])
plt.show()

# box plot of all the features
X.boxplot()
plt.show()

# notched box boxplots
X.boxplot(notch=True)
plt.show()

# describing various statsitics
print(X.describe())
