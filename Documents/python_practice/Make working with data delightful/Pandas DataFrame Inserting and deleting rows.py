

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

# john = pd.Series(data=['John', 'Boston', 34, 79],
#                  index=df.columns, name=17)
# Creates a new series object with labels corresponding to the column labels
# from df, hence 'index=df.columns'

# df = df.append(john)
# adds john as john as a new row to the dataframe

# df = df.drop(labels=[17])
# .drop removes the row specified

