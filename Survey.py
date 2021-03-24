# modules we'll use
import pandas as pd
import numpy as np


# read in all our data
survey = pd.read_csv("Data/2020_Data_Professional_Salary_Survey_Responses.csv")

# set seed for reproducibility
np.random.seed(0) 

# Select Data from CSV
df = pd.DataFrame(survey[['SurveyYear','Timestamp','SalaryUSD','Country','PostalCode',
                                 'YearsWithThisDatabase','JobTitle','ManageStaff','YearsWithThisTypeOfJob',
                                 'HowManyCompanies','OtherPeopleOnYourTeam','Gender','Counter']])

# Print DataFrame
# pd.set_option('display.max_columns', None)
# print(df.head())
print(df.dtypes)


# #Replace - value to 0 in SalaryUSD
df['SalaryUSD'] = df['SalaryUSD'].replace([' -   '],'0')
#
# print(df.loc[df.SalaryUSD == "0"])
# #
# Convert String to number for SalaryUSD
df['SalaryUSD'] = pd.to_numeric(df['SalaryUSD'])
print(df.dtypes)
# print(job_title.dtypes)
#
# Slice text to get a Number from HowManyCompanies Column
df['HowManyCompanies'] = df['HowManyCompanies'].str.slice(stop=1)
print(df.HowManyCompanies.head())
#
# Replace N to 0
df['HowManyCompanies'] = df['HowManyCompanies'].replace(['N'],'0')
df['HowManyCompanies'] = pd.to_numeric((df['HowManyCompanies']))
print(df.HowManyCompanies.head())
#
# Slice text to get a Number from OtherPeopleOnYourTeam Column
df['OtherPeopleOnYourTeam'] = df['OtherPeopleOnYourTeam'].str.slice(start=-1)
print(df.OtherPeopleOnYourTeam.head())


#
# Replace e to 0
df['OtherPeopleOnYourTeam'] = df['OtherPeopleOnYourTeam'].replace(['e','i'],'0')
df['OtherPeopleOnYourTeam'] = pd.to_numeric((df['OtherPeopleOnYourTeam']))
# print(df.OtherPeopleOnYourTeam.head())
print(df.OtherPeopleOnYourTeam.unique())
# #
# # Check Unique
# print(df.OtherPeopleOnYourTeam.unique())
#
df['Timestamp'] = pd.to_datetime(df['Timestamp']).dt.normalize()
print(df.Timestamp.head())
#
pd.set_option('display.max_columns', None)
print(df.head())

# Drop Duplicate
df.drop_duplicates()
#
# print(df.dtypes)
#
job_title = pd.DataFrame(df[['JobTitle','SalaryUSD']])
# print(avg_job_title)
avg_job_title = job_title.groupby('JobTitle').mean()
# avg_job_title = sorted('SalaryUSD')
avg_job_title.sort_values(by='SalaryUSD', ascending=False)
print(avg_job_title)
#
#

