import numpy as np
import pandas as pd

u = np.array(['cam','quyt','mit','dua'])
v = {'USA' : 'NewYork','Viet Nam' : 'Ho Chi Minh','Korea' : 'Seoul'}

s1 = pd.Series(u)
s2 = pd.Series(v)


print(s1, s1[0], len(s1))
