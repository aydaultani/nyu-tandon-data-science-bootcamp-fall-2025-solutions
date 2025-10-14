import numpy as np
import pandas as pd

A = np.array([1, 2, 3])
B = np.array([3, 4, 5])

print("="*100)
print(A)
print("="*100)
print(B)

A_B_vstack = np.vstack((A, B))
A_B_hstack = np.hstack((A, B))

print("="*100)
print(A_B_vstack)
print("="*100)
print(A_B_hstack)
print("="*100)

intersection = np.intersect1d(A,B)
print(intersection)
print("="*100)

mask = (A < 3)
A_extracted = A[mask]
print(A_extracted)
print("="*100)

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
mask = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)
filtered = iris_2d[mask]
print(filtered)
print("="*100)

df1 = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df1 = df1.loc[::20, ['Manufacturer', 'Model', 'Type']]
print(df1)
print("="*100)

df2 = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df2['Min.Price'] = df2['Min.Price'].fillna(df2['Min.Price'].mean())
df2['Max.Price'] = df2['Max.Price'].fillna(df2['Max.Price'].mean())
print(df2.loc[:, ['Min.Price', 'Max.Price']].head(5))
print("="*100)

df3 = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
mask = df3.sum(axis=1) > 100
df3 = df3.loc[mask]
print(df3)
print("="*100)
