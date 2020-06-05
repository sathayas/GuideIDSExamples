import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

# Loading data
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# spliting the data into training and testing data sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=50,
                                                    random_state=2020)


#
# NERAEST NEIGHBOR CLASSIFIER
#

# k nearest neighbor classifier objects, with k=5 neighbors
kNN = KNeighborsClassifier(5, weights='uniform')

# training on the training data
kNN.fit(X_train,y_train)

# Predicted classes
y_pred = kNN.predict(X_test)

# classifier performance
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test, y_pred,
                            target_names=target_names))


#
# NEURAL NETWORK CLASSIFIER
#

from sklearn.neural_network import MLPClassifier

# Multi-layer preceptron classifier object
#     stochastic gradient descent solver
#     a hidden layer with 3 neurons
mlp = MLPClassifier(solver='sgd',
                    hidden_layer_sizes=(3), random_state=2020)

# training on the training data
mlp.fit(X_train,y_train)

# Predicted classes
y_pred = mlp.predict(X_test)

# classifier performance
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test, y_pred,
                            target_names=target_names))
