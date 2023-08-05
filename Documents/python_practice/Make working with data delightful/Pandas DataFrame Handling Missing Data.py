

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

# Dataframes often contains missing values often referred to as NaN (Not a Number)


df_ = pd.DataFrame({'x': [1, 2, np.nan, 4]})

# Many Pandas methods omit NaN values when performing calculations, unless
# told not to do so.

# df_.mean()
# returns the mean of the dataframe omitting the NaN

# df_.mean(skipna=False)
# returns the mean without omitting the NaN, which creates another NaN
# showing whether there were any missing values

# df_.fillna(value=0)
# .fillna() can be used to fill in NaNs
# adding 'value=0' replaces the NaN with 0

# df_.fillna(method='ffill')
# fills the value with the value above the NaN

# df_.fillna(method='bfill')
# fills the NaN with the value below the missing value

# df_.interpolate()
# fills the missing value with an interpolated value

# df_.dropna()
# removes a row or column with missing data



