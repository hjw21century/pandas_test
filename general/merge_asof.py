import pandas as pd

left = pd.DataFrame({"a": [1, 5, 10], "left_val": ["a", "b", "c"]})
right = pd.DataFrame({"a": [1, 2, 3, 6, 7], "right_val": [1, 2, 3, 6, 7]})
print(pd.merge_asof(left, right, on="a"))