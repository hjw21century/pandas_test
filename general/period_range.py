import pandas as pd

print(pd.period_range(start=pd.Period('2017Q1', freq='Q'),
                end=pd.Period('2017Q2', freq='Q'), freq='M'))