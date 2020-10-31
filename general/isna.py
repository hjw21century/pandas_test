import pandas as pd

df = pd.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])

print(pd.isna(df))