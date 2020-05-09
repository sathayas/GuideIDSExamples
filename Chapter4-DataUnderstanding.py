import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

# loading the iris data set
iris = datasets.load_iris()
X = pd.DataFrame(iris.data)   # features data frame
X.columns = ['sepal length', 'sepal width', 'petal length', 'petal width']
y = pd.DataFrame(iris.target)  # target data frame
y.columns = ['species']
target_names = iris.target_names

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


#
# SCATTER PLOTS
#

# plotting petal width vs length (as a method)
X.plot.scatter(x='petal width', y='petal length')
plt.show()

# plotting petal width vs length (as a function)
plt.scatter(X['petal width'], X['petal length'])
plt.show()

# scatter plot matrix
pd.plotting.scatter_matrix(X)
plt.show()

# scatter plot matrix with different colors for species
pd.plotting.scatter_matrix(X, c=y['species'])
plt.show()
