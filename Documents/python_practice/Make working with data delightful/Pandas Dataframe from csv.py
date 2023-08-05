

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

df.to_csv('data.csv')

# df.to_csv('data.csv')    creates a csv file named "data"

# to read a csv file:
# "pd.read_csv('data.csv', index_col=0)"
# "index_col=0" specifies that the row labels are located in the first column

# df.index - returns the row labels
# df.columns - returns the column labels
# df.columns[1] - returns the label for column 2

# df.index = np.arange(10, 17)
# and then
# df.index - uses numpy.arange() to give the row labels a new sequence between
# specified valued


