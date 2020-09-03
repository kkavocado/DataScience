# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd


# %%
pd.isnull(np.nan)


# %%
pd.isnull(None)


# %%
pd.isna(np.nan)


# %%
pd.isna(None)


# %%
pd.notnull(None)


# %%
pd.isnull(pd.Series([1,np.nan, 7]))


# %%
pd.isnull(pd.DataFrame({
    'Column A': [1,np.nan,7],
    'Column B': [np.nan, 2, 3],
    'Column C': [np.nan, 2, np.nan]
}))


# %%
pd.Series([1,2, np.nan]).count()


# %%
s=pd.Series([1,2,3,np.nan, np.nan,4])


# %%
pd.notnull(s)


# %%
pd.isnull(s)


# %%
pd.notnull(s).sum()


# %%
pd.isnull(s).sum()


# %%
s[pd.notnull(s)]


# %%
s


# %%
s.dropna()


# %%
df = pd.DataFrame({
    'Column A': [1, np.nan, 30, np.nan],
    'Column B': [2, 8, 31, np.nan],
    'Column C': [np.nan, 9, 32, 100],
    'Column D': [5, 8, 34, 110],
})


# %%
df


# %%
df.shape


# %%
df.info()


# %%
df.dropna()


# %%
df.dropna(axis=1)


# %%
df2 = pd.DataFrame({
    'Column A': [1, np.nan, 30],
    'Column B': [2, np.nan, 31],
    'Column C': [np.nan, np.nan, 100]
})


# %%
df2


# %%
df2.dropna(how='all')


# %%
df2.dropna(how='any')


# %%
df.dropna(thresh=3)


# %%
df2.dropna(thresh=3, axis=0)


# %%
s


# %%
s.fillna(0)


# %%
s.fillna(s.mean())


# %%
s


# %%
s.fillna(method='ffill')


# %%
s.fillna(method= 'bfill')


# %%
df


# %%
df.fillna({'Column A': 0, 'Column B': 99, 'Column C': df['Column C'].mean()})


# %%
s.dropna().count()


# %%
missing_values = len(s.dropna()) != len(s)
missing_values


# %%
df3= pd.DataFrame({
    'Sex': ['M', 'F', 'F', 'D', "?"],
    'Age': [29, 30, 24, 290, 25]
})

df3


# %%
df3['Sex'].unique()


# %%
df3['Sex'].value_counts()


# %%
df3['Sex'].replace('D','F')


# %%
df3.replace({
    'Sex': {
        'D': 'F',
        'N': 'M'
    },
    'Age': {
        290:29
    }
})


# %%
df3[df3['Age']>100]


# %%
df3.loc[df3['Age']>100, 'Age']= df3.loc[df3['Age']>100, 'Age']/10


# %%
df3


# %%
ambassadors = pd.Series([
    'France',
    'United Kingdom',
    'United Kingdom',
    'Italy',
    'Germany',
    'Germany',
    'Germany',
], index=[
    'Gérard Araud',
    'Kim Darroch',
    'Peter Westmacott',
    'Armando Varricchio',
    'Peter Wittig',
    'Peter Ammon',
    'Klaus Scharioth '
])


# %%
ambassadors


# %%
ambassadors.duplicated()


# %%
ambassadors.duplicated(keep='last')


# %%
ambassadors.duplicated(keep=False)


# %%
ambassadors.drop_duplicates()


# %%
ambassadors.drop_duplicates(keep='last')


# %%
ambassadors.drop_duplicates(keep=False)


# %%
players = pd.DataFrame({
    'Name': [
        'Kobe Bryant',
        'LeBron James',
        'Kobe Bryant',
        'Carmelo Anthony',
        'Kobe Bryant',
    ],
    'Pos': [
        'SG',
        'SF',
        'SG',
        'SF',
        'SF'
    ]
})


# %%
players


# %%
players.duplicated()


# %%
players.duplicated(subset=['Name'])

# %% [markdown]
# ## Text Handling
# 
# 
# 

# %%
df4 = pd.DataFrame({
    'Data': [
        '1987_M_US _1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I  T_2'
]})


# %%
df4


# %%
df4['Data'].str.split('_')


# %%
df4['Data'].str.split('_', expand=True)


# %%
df4=df4['Data'].str.split('_', expand=True)


# %%
df4.columns= ['Year', 'Sex', 'Country', 'No Children']


# %%
df4


# %%
df4['Year'].str.contains('\?')


# %%
df4['Country'].str.strip()


# %%
df4['Country'].str.replace(' ', '')


# %%



