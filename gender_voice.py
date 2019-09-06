
"""
Gender Voice
"""

import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd


print(os.listdir())

csv_file = pd.read_csv('gender_voice.csv')
raw_df = csv_file.iloc[:, 0:20]

df = raw_df.values

raw_labels = csv_file.iloc[:, 20]
lables = raw_labels.values

idx = np.arange(df.shape[0])

np.random.shuffle(idx)
df = df[idx, :]
lables = lables[idx]

print('End!')
