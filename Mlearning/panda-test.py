import pandas as pd
import numpy as np

# np.nan创建一个空值NaN
# s = pd.Series([1,3,5,np.nan,6,9])
#print(s)
dates = pd.date_range('2018-01-01',periods=7)
df = pd.DataFrame(np.random.randn(7,4),index=dates,columns=list('ABCD'))
# print(df.head())
# print('--'*16)
# print(df.tail(3))
# df = pd.DataFrame({'Apples': 30,'Bananas': 21 })

# print('index is:')
# print(df.index)
# print('columns is:')
# print(df.columns)
# print('values is: ')
# print(df.values)
# print(df.describe())
# print(df.T)

# print(df.sort_index(axis=1,ascending=False))
# print(df.sort_index(axis=0,ascending=False))

# print(df.sort_values(by='B'))
# data = np.array(['a','b','c','d'])
# s = pd.Series(data)
# print(s)


# data2 = {'a':0.,'c':2.,'b':1.}

# s1 = pd.Series(data2,index=['b','c','d','a'])
# print(s1)

def adder(ele1,ele2):
    return ele1+ele2

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print(df)

df1 = df.pipe(adder,2)
print(df1)

