import pandas as pd

#Editing CSV 0
df_0 = pd.read_csv("data/daily_sales_data_0.csv")

df_0.drop(df_0[df_0['product'] != "pink morsel"].index, inplace = True)

df_0['Sales'] = pd.to_numeric((df_0.price).str.strip("$")) * df_0.quantity

df_0 = df_0.drop('product', axis='columns')
df_0 = df_0.drop('price', axis='columns')
df_0 = df_0.drop('quantity', axis='columns')

#Editing CSV 1
df_1 = pd.read_csv("data/daily_sales_data_1.csv")

df_1.drop(df_1[df_1['product'] != "pink morsel"].index, inplace = True)

df_1['Sales'] = pd.to_numeric((df_1.price).str.strip("$")) * df_1.quantity

df_1 = df_1.drop('product', axis='columns')
df_1 = df_1.drop('price', axis='columns')
df_1 = df_1.drop('quantity', axis='columns')

#Editing CSV 2
df_2 = pd.read_csv("data/daily_sales_data_1.csv")

df_2.drop(df_2[df_2['product'] != "pink morsel"].index, inplace = True)

df_2['Sales'] = pd.to_numeric((df_2.price).str.strip("$")) * df_2.quantity

df_2 = df_2.drop('product', axis='columns')
df_2 = df_2.drop('price', axis='columns')
df_2 = df_2.drop('quantity', axis='columns')

frames = [df_0, df_1, df_2]

result = pd.concat(frames)

result.to_csv('daily_sales_data', index=False)