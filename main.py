import numpy as np
import pandas as pd

u = np.array(['Cam', 'Quyt', 'Mit', 'Dua']) # Array
v = {'USA':'New York','VietNam' : 'Ho Chi Minh','Korea' :'Seoul'} # Dictionary

s1 = pd.Series(u)
s2 = pd.Series(v)

print(u,type(u))
print(v,type(v))
print(s1,type(s1),s1[0], len(s1))
