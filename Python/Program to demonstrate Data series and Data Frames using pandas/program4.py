import pandas as pd
import numpy as np

# create the initial DataFrame
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

# create the DataFrame
df = pd.DataFrame(exam_data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

# add a new row to the DataFrame
new_row = pd.Series(data={'name': 'Suresh', 'score': 15.5, 'attempts': 1, 'qualify': 'yes'}, name='k')
df = df.append(new_row)

# sort the DataFrame by 'name' in descending order, then by 'score' in ascending order
df = df.sort_values(by=['name', 'score'], ascending=[False, True])

print(df)
