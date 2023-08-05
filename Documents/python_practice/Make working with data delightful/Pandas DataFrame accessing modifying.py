

import numpy as np
import pandas as pd

data = {
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
             'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}
    

row_labels = [101, 102, 103, 104, 105, 106, 107]
    
df = pd.DataFrame(data=data, index=row_labels)



df.index = np.arange(10, 17)


df_ = df.astype(dtype={'age': np.int32, 'py-score': np.float32})
# changes 'age' column to int32 and 'py_score' to float 32

# df['name']
# list all the values in the column labelled name

# df.loc[10]
# lists all the values in the row labelled 10

# df.iloc[0]
# lists all the values in the first row (row 0)

# df.at[11, 'city']
# returns the value from the row labelled 11 and the column labelled city

# df.iat[0, 0]
# returns the value from the first row and first column

# df.loc[:, 'city']   OR   df.iloc[:, 1]
# returns the value from the full column city or the second column
# ':' is a slice construct

# df.loc[11:15, ['name, 'city']]
# returns the values in rows labelled 11-15 of the columns
# labelled 'name' and 'city'

# df.iloc[1:6, [0, 1]]
# returns the values in rows 2-6* and columns 1 and 2
# the values in index 6 (row 7) are excluded because
# the stop index is not returned

# df.iloc[1:6:2, 0]
# returns the values from rows 2-6 (index 6 excluded),
# but skpping every second row

# df.iloc[slice(1, 6, 2), 0]
# built in python clas for the same function

# df.iloc[np.s_[1:6:2], 0]
# numpy command for the same function

# df.iloc[pd.IndexSlice[1:6:2], 0]
# Pandas command for the same function






