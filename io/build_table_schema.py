import pandas as pd

df = pd.DataFrame(
    {'A': [1, 2, 3],
     'B': ['a', 'b', 'c'],
     'C': pd.date_range('2016-01-01', freq='d', periods=3),
     }, index=pd.Index(range(3), name='idx'))

print(pd.io.json.build_table_schema(df))
