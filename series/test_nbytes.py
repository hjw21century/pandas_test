import pandas as pd
nbytes = pd.Series([[1, 2, 3], [4, 5, 6], [4, 5, 6]]).nbytes
print(f'nbytes={nbytes}')
