"""
Exercise 8. Create, Read csv file.
"""
from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd 

Names = ['Bob','Jessica','Mary','John','Mel']
Births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(Names,Births))
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])

df.to_csv('births.csv',index=False,header='Some')

Location = r'births.csv'
readfile = pd.read_csv(Location, names=['Names','Births'])

print(readfile['Births'])
print('max year =', max(Births))

plt.plot(Births)
plt.show()
