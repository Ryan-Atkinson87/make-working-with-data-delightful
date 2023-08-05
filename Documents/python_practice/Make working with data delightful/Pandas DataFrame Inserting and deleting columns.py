

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

df['js-score'] = np.array([71.0, 95.0, 88.0, 79.0, 91.0, 91.0, 80.0])
# inserts a new column onto the end of the dataframe titled 'js-score'
# with the values supplied

df['total-score'] = 0.0
# inserst a new column onto the of the dataframe where all the values in that
# column are 0.0

df.insert(loc=4, column='django-score',
          value=np.array([86.0, 81.0, 78.0, 88.0, 74.0, 70.0, 81.0]))
# if you need to insert a column in a certain position .insert() allows
# you to do this.
# Inserts a new column in location 4 (5th row)
# column set the label of the new column and value specifies the data values
# to insert.

# del df['total-score']
# deletes the column 'total-score' 

# df.pop('total-score')
# deletes the column 'total-score' and also returns the deleted values

# df = df.drop(labels='age', axis=1)
# removes the columns of the dataframe as it did with rmoving rows
# axis=1 is required to specify when axis the data is orientated on





