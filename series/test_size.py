import pandas as pd
size = pd.Series([1, 2, 3, [4, 5, 6], [4, 5, 6]]).size
print(f'size={size}')
