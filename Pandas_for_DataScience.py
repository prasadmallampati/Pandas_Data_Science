# -*- coding: utf-8 -*-
"""Pandas_For_Data_Science.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Nh2SXEdQW7y5kShpifdqCxPbxyrFrnDC

# Pandas for Data Science

importing  package's
"""

import pandas as pd

"""creating data frame using pandas"""

df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])

"""printing data frame have diffrent approach's"""

# using df name
df

"""head () return the first 5 rows of DataFrame"""

df.head()

"""with columns name"""

df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['A','B','C'])

# head
df.head()

"""with columns and index names"""

df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['A','B','C'],index=['x','y','z'])

"""head ()"""

df.head()

"""if u want specified number row"""

df.head(1) # 1 row number

"""if u want specified number row"""

# head(2)
df.head(2)

"""i want last elements use tail function"""

df.tail(1) # last element 1

"""for last 2 rows"""

df.tail(2)

"""for knowing columns  names"""

df.columns

"""for knowing indexs"""

df.index

"""for knowing information about data frame  use info()"""

df.info()

"""describe  return count mean std min 25 50 75 % max"""

# describe  return count mean std min 25 50 75 % max
df.describe()

"""for spcific column"""

# for spcific column
df['A']

# for specific column
df['B']

# for specific column

df['C']

""" unique values"""

#
df["A"].unique()

"""for shape  of data frame (row,col)"""

# for shape  of data frame (row,col)
df.shape

"""size"""

# size 3*3
df.size



"""Loading in DataFrame from files"""

# loading csv file
df1=pd.read_csv('california_housing_test.csv')

"""reading xlsx file

"""

# reading xlsx file

df2=pd.read_csv('mnist_test.csv')



# head()
df1.head()

"""Accessing Data with Pandas"""

# using varible of dataframe
df

# df1

df1

# df2
#df2

print(df1)

# using display
display(df)

# accessing

df1.head()

# head for df2
#df2.head()

# using loc with one value
df.iloc[:,[0]]

# usingiloc with mutiple

df.iloc[:,[0,1,2]]

# # usingiloc with mutiple
# iloc[start:stop,[index]]
df.iloc[0:2,[0,1,2]]

# dataframe using also will get ouput

df.index=df['A']

df

# now cheeck


df.loc[0:4]

#
df.loc[1:3,'C']

import pandas as pd

df_c=pd.read_csv('/content/coffee.csv')

df_c

# sort_values
df_c.sort_values('Units Sold')

# sort_values and with parameter
df_c.sort_values('Units Sold',ascending=False)

df_c.sort_values(['Units Sold','Coffee Type'])

# using for and iterrows()

for index ,row in df_c.iterrows():
  print(index)

  print(row['Units Sold'])

"""Filtering Data"""

# condition of df_c

df_c[df_c['Units Sold'] >20]

# filter
df_c[(df_c['Units Sold']) & (df_c['Coffee Type']=='Latte')]

# contain function
df_c[df_c['Day'].str.contains('Monday')]

# contain function with paramter case means u can give any case like upper or lower
df_c[df_c['Coffee Type'].str.contains('Espresso',case=False)]

# or condition
df_c[df_c['Coffee Type'].str.contains('monday|espresso|latte',case=False)]

#  isin()

df_c[df_c['Day'].isin(['Monday'])]

# query function


df_c.query('Day=="Sunday"')

"""Adding/Removeing Columns"""

df_c['Price']=5.00

df_c

# head()
df_c.head()

import numpy as np

df_c['new_price']=np.where(df_c['Coffee Type']=='Espresso',3.9,5.0)

df_c

df_c.info()

"""Handling Null Values"""

df_c.loc[[0,1],'Units Sold']=np.nan

df_c

df_c.info()

"""for knowing null is_null()"""

df_c.isnull()



"""for suming null"""

df_c.isnull().sum()



"""for filling null values"""

df_c.fillna(df_c['Units Sold'].mean())

# Interpolation return null valuees
df_c.fillna(df_c['Units Sold'].interpolate())

# filling null forl all unit sold column
df_c['Units Sold']=np.nan

df_c

# out of 14  12 is nan 2 is 15.0
df_c.loc[[1,2],'Units Sold']=15

df_c

df_c.loc[[2,3],'Units Sold']=np.nan

df_c['Units Sold'].interpolate()

# loading df
df_c=pd.read_csv('/content/coffee.csv')

"""for droping null use dropna() function"""

df_c.dropna()



df_c.dropna(subset=['Units Sold'],inplace=True)

df_c



"""Aggregating Data"""

df_c.head()

# calculating count of each type of tea
df_c['Coffee Type'].value_counts()

df_c['Units Sold']=df_c['Units Sold'].interpolate()

df_c

# groupby


df_c.groupby(['Coffee Type','Units Sold']).sum()

# group by
df_c.groupby(['Day'])['Units Sold'].sum()

df_c.mode()

# groupby sum()
df_c.groupby(['Coffee Type'])['Units Sold'].sum()

# mean()

df_c.groupby(['Coffee Type'])['Units Sold'].mean()

df_c

#df_c.groupby(['Coffee Type']).agg({'Units Sold':'sum','price':'mean'})

df_c.groupby(['Coffee Type']).agg({'Units Sold':'sum'})

# pivot

pivot=df_c.pivot(columns='Coffee Type',index='Day')

pivot

# pivot
pivot.loc['Monday']

#
pivot.loc['Monday']

# sum
pivot.sum()

# axis =1
pivot.sum(axis=1)

# df_head()
df_c.head()

df_c['Units Sold'].cumsum()
