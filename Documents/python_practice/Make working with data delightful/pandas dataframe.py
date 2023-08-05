

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
    
df

# viewing dataframe type:
# "df" or print(df)

# view first "n" rows:
# df.head(n=2)

# view last "n" rows
# df.tail(n=2)

# view a selected column:
# cities = df['city']
# cities
# OR
# df.city     (use column name)

# view a certain data value, after column "city" is defined as "cities"
# cities[102]

# view all data from a row:
# df.loc[103]


