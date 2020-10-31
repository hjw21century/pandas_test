import pandas as pd

values = pd.Series([1, 2, 3]).values
values_category = pd.Series(list('aabc')).astype('category').values
print(f'values={values} len={len(values)}')
print(f'values_category={values_category} len={len(values_category)}')
