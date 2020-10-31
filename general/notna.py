import pandas as pd
import numpy as np

array = np.array([[1, np.nan, 3], [4, 5, np.nan]])
print(pd.notna(array))