import pandas as pd

df = pd.DataFrame([[1, 1.0, 'a']], columns=['x', 'y', 'z'])
df.to_hdf('./store.h5', 'data')
reread = pd.read_hdf('./store.h5')
print(reread)
