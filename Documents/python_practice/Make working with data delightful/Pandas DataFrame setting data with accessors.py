

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

# df.loc[:13, 'py-score'] = [40, 50, 60, 70]
# modifies rows 10-13 in the column "py-score" with the values
# from the supplied list

# df.loc[14:, 'py-score'] = 0
# sets the remaining values in the column to 0

# df['py-score']

# df.iloc[:, -1] = np.array([88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0])
# accesses the last column (-1) and alters the value of those rows with the
# corresponding value in the list/array


