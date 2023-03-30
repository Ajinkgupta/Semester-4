import pandas as pd

s1 = pd.Series([[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]])

s2 = pd.Series([val for sublist in s1 for val in sublist])
print(s2)
