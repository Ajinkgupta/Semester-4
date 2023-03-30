import pandas as pd

s1 = pd.Series([10, 20, 30, 40, 50])
s2 = pd.Series([5, 10, 15, 20, 25])

# Add s1 and s2
s3 = s1 + s2
print("Addition of two Series:")
print(s3)

# Subtract s2 from s1
s4 = s1 - s2
print("\nSubtraction of two Series:")
print(s4)

# Multiply s1 and s2
s5 = s1 * s2
print("\nMultiplication of two Series:")
print(s5)

# Divide s1 by s2
s6 = s1 / s2
print("\nDivision of two Series:")
print(s6)
