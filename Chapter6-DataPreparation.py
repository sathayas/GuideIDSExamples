import numpy as np
from sklearn.impute import SimpleImputer

#
# MISSING VALUES
#

# Creating toy data sets (numerical)
X_train = np.array([3, 2, 1, 4, 5, np.nan, np.nan, 5]).reshape(-1,1)
X_test = np.array([3, 2, np.nan, 4, np.nan, np.nan, 1, np.nan]).reshape(-1,1)

# Creating toy data sets (categorical)
S_train = np.array(['Hi', 'Med', 'Med', 'Hi', 'Low', 'Med', '', 'Med']).reshape(-1,1)
S_test = np.array(['Hi', '', '', 'Hi', 'Med', '', 'Low']).reshape(-1,1)

# Imputing numerical data with mean
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
X_train_imp = imp_mean.fit_transform(X_train)
X_test_imp = imp_mean.transform(X_test)

# Imputing categorical data with mode
imp_mode = SimpleImputer(missing_values='', strategy='most_frequent')
S_train_imp = imp_mode.fit_transform(S_train)
S_test_imp = imp_mode.transform(S_test)
