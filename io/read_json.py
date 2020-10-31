import pandas as pd
df = pd.DataFrame([['a', 'b'], ['c', 'd']],
                  index=['row 1', 'row 2'],
                  columns=['col 1', 'col 2'])

dd = df.to_json(orient='split')
print(pd.read_json(dd, orient='split'))


