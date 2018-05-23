

import pandas



# colums declaration
columns = ['Work ID', 'name','country','education', 'KEY']

# dataframe declaration
df = pandas.DataFrame([['4480','Thomas', 'US', 'MB', 32], ['6657','June','China','BS', 25],['2219','Samantha','UK','JD', 40]], columns=columns)

df.set_index('KEY',inplace=True)

print(df)

# various DataFrame print
print("Exercice 1, -- df['name'] :", '\n', \
 df['name'])
print("Exercice 2, -- df[['name','education']] : ", '\n', \
 df[['name','education']])
print("Exercice 3, -- df[1:]", '\n', \
 df[1:])
print("Exercice 4, -- df.loc['r1']", '\n', \
 df.loc['r1'])
print("Exercice 5, -- df.loc['r1':'r3']", '\n', \
 df.loc['r1':'r3'])
print("Exercice 6, -- df.loc['r1']['name']", '\n', \
 df.loc['r1']['name'])
print("Exercice 7, -- df.loc['r1','name']", '\n', \
 df.loc['r1','name'])
print("Exercice 8, -- df.iloc[1]", '\n', \
 df.iloc[1])
print("Exercice 9, -- df[df['age']>30]", '\n', \
 df[df['age']>30])
