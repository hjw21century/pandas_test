import pandas as pd


df = pd.DataFrame({"animal": ["dog", "pig"], "age": [10, 20]})
print(pd.eval("double_age = df.age * 2", target=df))