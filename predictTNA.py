import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
CLASS_COLUMN = 'class'
TARGET_COLUMN = 'tna'
DATA_COLUMNS = ['c1', 'c2', 'c3', 'm1', 'm2', 'm3', 'n1', 'n2', 'n3', 'p1', 'p2', 'p3']

# Standardise data
def scale_data(X):
    result = {}
    mean = {}
    std = {}
    # Standardisation
    for x in X:
        result[x] = []
        if not (x == CLASS_COLUMN or x == TARGET_COLUMN):
            mean[x] = X[x].mean()
            std[x] = X[x].std()
            for y in X[x]:
                result[x].append((y - mean[x]) / std[x])
        else:
            # Don't standardise class values
            for y in X[x]:
                result[x].append(y)
    return result


# Convert data to the format that the models require
def reformat_data(array, length):
    result = []
    for i in range(length):
        temp_array = []
        for x in DATA_COLUMNS:
            temp_array.append(array[x][i])
            # Add in non-linear data
            for j in range(2, 5, 1):
                temp_array.append(pow(array[x][i], j))
        result.append(temp_array)
    return result


# Train the models and predict target values
def predict(probe_a_data, probe_a_targets, probe_b_data):
    # Create and train the model
    model = Ridge(alpha=10.789).fit(probe_a_data, probe_a_targets)
    # Predict target values
    probe_b_targets = model.predict(probe_b_data)
    # Reformat output
    probe_b_targets_reformat = []
    for i in range(len(probe_b_targets)):
        probe_b_targets_reformat.append(probe_b_targets[i])
    return probe_b_targets_reformat


def main():
    # Read and standardise data
    probe_a = scale_data(pd.read_csv('../probeA.csv', header=0))
    probe_a_targets = probe_a[TARGET_COLUMN]
    # Reformat non-target data
    probe_a_data = reformat_data(probe_a, len(probe_a[CLASS_COLUMN]))
    probe_b = scale_data(pd.read_csv('../probeB.csv', header=0))
    probe_b_data = reformat_data(probe_b, len(probe_b['c1']))
    # Generate predictions
    probe_b_targets = predict(probe_a_data, probe_a_targets, probe_b_data)
    # Save results to file
    np.savetxt("tnaB.csv", probe_b_targets, delimiter=",", fmt='%1.18f')


if __name__ == '__main__':
    main()
