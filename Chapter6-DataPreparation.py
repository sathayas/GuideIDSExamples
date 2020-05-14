import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

#
# MISSING VALUES
#

# Creating toy data sets (numerical)
X_train = pd.DataFrame()
X_train['X'] = [3, 2, 1, 4, 5, np.nan, np.nan, 5]
X_test = pd.DataFrame()
X_test['X'] = [3, 2, np.nan, 4, np.nan, np.nan, 1, np.nan]

# Creating toy data sets (categorical)
S_train = pd.DataFrame()
S_train['S'] = ['Hi', 'Med', 'Med', 'Hi', 'Low', 'Med', np.nan, 'Med']
S_test = pd.DataFrame()
S_test['S'] = ['Hi', np.nan, np.nan, 'Hi', 'Med', np.nan, 'Low']

# Imputing numerical data with mean
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
X_train_imp = imp_mean.fit_transform(X_train)
X_test_imp = imp_mean.transform(X_test)

# Imputing categorical data with mode
imp_mode = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
S_train_imp = imp_mode.fit_transform(S_train)
S_test_imp = imp_mode.transform(S_test)
