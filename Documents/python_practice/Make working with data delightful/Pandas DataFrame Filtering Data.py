

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

del df['total-score']
# deletes the column 'total-score' 

# df.pop('total-score')
# deletes the column 'total-score' and also returns the deleted values

# df = df.drop(labels='age', axis=1)
# removes the columns of the dataframe as it did with rmoving rows
# axis=1 is required to specify when axis the data is orientated on

# df['py-score'] + df['js-score']
# df['py-score'] / 100
# you can perform basic arithmetic on Pandas Series and DataFrame objects

df['total'] =\
            0.4 * df['py-score'] + 0.3 * df['django-score'] + 0.3 * df['js-score']
# adds a new column 'total' and fills it with values of the following equation

###

score = df.iloc[:, 3:6]
# variable 'score' now refers to the DataFrame with Python, Django and
# JavaScript scores. 0 value columns 3 to 6 in our DataFrame

# np.average(score, axis=1,
#            weights=[0.4, 0.3, 0.3])
# returns the average of the values in the variable 'score' with averages
# weighted as specified

del df['total']
# deletes the column 'total'

df['total'] = np.average(df.iloc[:, 3:6], axis=1,
                         weights=[0.4, 0.3, 0.3])
# creates a new column titles 'total' with the averages of the 0 value columns
# 3-6 weighted as specified.

# filter_ = df['django-score'] >= 80
# df['django-score'] >= 80 returns true for those rows in which the 'django-score
# is equal to or greater than 80 and flase for those less than 80.

# filter_
# returns the filter_ series showing which rows are true and which are false

# df[filter_]
# returns the data frame, only showing the rows which are true for filter_

# NOT (~), AND (&), OR (|), XOR (^) are all operations that can be used to
# filter dataframes

# df[(df['py-score'] >= 80) & (df['js-score'] >= 80)]
# returns the candidates whose py-score and js-score are greater than 80
# (without creating a series

# df['django-score'].where(cond=df['django-score'] >= 80, other=0.0)
# .where() replaces values in the dataframe where the conditions aren't
# satisfied
# In this example it's looking values in django score which are greater than 80
# Where this is true the values will remain the same, where it is false the
# value will be changed to 0.0



