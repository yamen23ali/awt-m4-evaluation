import numpy as np
import pandas as pd


df = pd.read_csv('results/M4/Smyl/lower.csv', header=None)
df.drop(df.columns[0], axis=1, inplace=True)
df.to_csv('results/M4/Smyl/lower.csv', header=None, sep=',', index=False)
