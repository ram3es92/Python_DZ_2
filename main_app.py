import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data = pd.get_dummies(data['whoAmI'])
data = data.astype(int)

print(data)