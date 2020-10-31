import pandas as pd
s = pd.Series(range(32))
print(f'memory_usage={s.memory_usage()}')
