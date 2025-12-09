import pandas as pd 
import numpy as np


d1 =pd.Series(np.arange(5),name='series from array',index=['a','b','c','d','e'])
print(d1)

series_3 = pd.Series([1, 2, 3, 4, 5]) 
print(series_3[4:5])