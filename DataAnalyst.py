# modules we'll use
import pandas as pd
import numpy as np


# read in all our data
data = pd.read_csv("Data/DataAnalyst.csv")

# set seed for reproducibility
np.random.seed(0)

# Drop Duplicate
drop_dup = data.drop_duplicates()

# Check Null Value
print(drop_dup.isnull().value_counts())

# Select Data from CSV
# df = pd.DataFrame(drop_dup[['Job Title','Salary Estimate','Rating','Location','Industry',
#                                  'Sector']])
# print(df)