

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
# Inserts a new column in location 4 (5th row)

del df['total-score']
# deletes the column 'total-score' 

df['total'] =\
            0.4 * df['py-score'] + 0.3 * df['django-score'] + 0.3 * df['js-score']
# adds a new column 'total' and fills it with values of the following equation

###

score = df.iloc[:, 3:6]
# variable 'score' now refers to the DataFrame with Python, Django and
# JavaScript scores. 0 value columns 3 to 6 in our DataFrame


del df['total']
# deletes the column 'total'

df['total'] = np.average(df.iloc[:, 3:6], axis=1,
                         weights=[0.4, 0.3, 0.3])
# creates a new column titles 'total' with the averages of the 0 value columns
# 3-6 weighted as specified.


df_ = pd.DataFrame({'x': [1, 2, np.nan, 4]})

temp_c = [ 8.0,  7.1,  6.8,  6.4,  6.0,  5.4,  4.8,  5.0,
           9.1, 12.8, 15.3, 19.1, 21.2, 22.1, 22.4, 23.1,
           21.0, 17.9, 15.5, 14.4, 11.9, 11.0, 10.2,  9.1]
# created the variable temp_c which refers to a list of temperature values

dt = pd.date_range(start='2019-10-27 00:00:00.0', periods=24,
                   freq='H')
# date_range() accepts the arguments that you use to specify the start or end of
# the range, number of periods, frequency, time zone and more

temp = pd.DataFrame(data={'temp_c': temp_c}, index=dt)
# Creates a dataframe with the values from 'temp_c' as the data and the sequence
# of dates and times from 'dt' as the index




