##### Talk Better Sorting Algorithm #####

# Helpful tutorial for pandas in-group sorting: 
# https://arccoder.medium.com/pandas-sort-within-groups-e1f3b6a10a3f

import pandas as pd
from funcs import *


# Read data in. Must have column names already cleaned
df = pd.read_csv("NeatSampleData.csv")
df = preprocess(df)

df = makeGroups(df, 5)
df.to_csv("groups.csv")





