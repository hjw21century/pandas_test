import pandas as pd
ndim = pd.Series([[1, 2, 3], [4, 5, 6], [4, 5, 6]], ['a','b','c']).ndim
print(f'ndim={ndim}')
