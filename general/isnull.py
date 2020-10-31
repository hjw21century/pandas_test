import pandas as pd

index = pd.DatetimeIndex(["2017-07-05", "2017-07-06", None,
                          "2017-07-08"])

print(pd.isna(index))