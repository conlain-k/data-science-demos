import pandas as pd

import numpy as np
import sklearn.model_selection
import h5py

from matplotlib import pyplot as plt

co2_data = pd.read_csv('../co2_mm_mlo.csv', index_col = False)

num_points = len(co2_data)

[train_inds, test_inds] = sklearn.model_selection.train_test_split(np.arange(num_points), train_size = 0.5, random_state = 7)
# sort them for convenience later
train_inds = sorted(train_inds)
test_inds = sorted(test_inds)

X_train = co2_data['decdate'][train_inds]
y_train = co2_data['average'][train_inds]

X_test = co2_data['decdate'][test_inds]
y_test = co2_data['average'][test_inds]

train_file = h5py.File("interp_train.hdf5", 'w')
train_file.create_dataset("X", data=X_train)
train_file.create_dataset("y", data=y_train)

test_file = h5py.File("interp_test.hdf5", 'w')
test_file.create_dataset("X", data=X_test)
test_file.create_dataset("y", data=y_test)

# plot the training data points
plt.scatter(X_train, y_train, marker='.', label="Training samples")
# plot the testing data points as well
plt.scatter(X_test, y_test, marker='.', label='Testing samples')

# set up the plot to make it look nice
plt.xlabel("Date")
plt.ylabel("CO2 concentration", rotation=0, horizontalalignment='right')
plt.title("Train/test split for CO2 interpolation")
plt.legend()
plt.tight_layout()
# show the plot
plt.show()


