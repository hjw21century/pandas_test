import pandas as pd

df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})

print(df)
print('--------------')


print(pd.melt(df, id_vars=['A'], value_vars=['B']))
print('--------------')


print(pd.melt(df, id_vars=['A'], value_vars=['B', 'C']))
print('--------------')

# pd.melt(df, id_vars=['A'], value_vars=['B'],
#         var_name='myVarname', value_name='myValname')
# print(df)
# print('--------------')

# pd.melt(df, id_vars=[('A', 'D')], value_vars=[('B', 'E')])
# print(df)
# print('--------------')