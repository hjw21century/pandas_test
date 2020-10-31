import pandas as pd
import os

original_df = pd.DataFrame({"foo": range(5), "bar": range(5, 10)})
pd.to_pickle(original_df, "./dummy.pkl")
unpickled_df = pd.read_pickle("./dummy.pkl")
print(unpickled_df)
os.remove("./dummy.pkl")
