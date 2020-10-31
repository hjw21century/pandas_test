import pandas as pd

s = pd.Series(['1.0', '2', -3])

print(pd.to_numeric(s))