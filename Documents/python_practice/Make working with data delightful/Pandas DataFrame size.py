

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

# df.types - shows the data types
# .astype() - use to change the data type of one or more columns

df_ = df.astype(dtype={'age': np.int32, 'py-score': np.float32})
# changes 'age' column to int32 and 'py_score' to float 32

# df_.dtypes
# to show the new data types

# df_.ndim
# shows the dimensions of the dataframe

# df_.shape
# shows the shape of the dataframe

# df_.size
# shows the total number of data values


# df.memory_usage()
# shows the amount of memory used


