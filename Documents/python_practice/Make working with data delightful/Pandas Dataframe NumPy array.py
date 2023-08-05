

import numpy as np
import pandas as pd

arr = np.array([[1, 2, 100],
                [2, 4, 100],
                [3, 8, 100]])

df_ = pd.DataFrame(arr, columns=['x', 'y', 'z'])

# df_ to show dataframe
# this looks the same as the nested list, except you can edit individual items
# useful for large datasets.

# arr[0, 0] = 1000     edits column 1 row 1 to 1000
# df_     this then shows dataframe with new values


