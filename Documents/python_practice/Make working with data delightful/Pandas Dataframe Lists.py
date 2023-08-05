


import numpy as np
import pandas as pd

l = [{'x': 1, 'y': 2, 'z': 100},
     {'x': 2, 'y': 4, 'z': 100},
     {'x': 3, 'y': 8, 'z': 100}]

# DataFrame made from a list of dictionaries
# dictionary keys are the column labels
# pd.DataFrame(l)       to show dataframe

ls = [[1, 2, 100],
      [2, 4, 100],
      [3, 8, 100]]

# Dataframe made as a nested list
# Make sure to specify the labels of the columns as below
# pd.DataFrame(ls, columns=['x', 'y', 'z']) to show dataframe
