import pandas as pd
from ConnectMySQL import mysql_connect, save_to_mysql

# After dowloading my csv and xlsx files, I read them with pandas
# df1 = pd.read_excel(r"/home/apprenant/PycharmProjects/American_dream/Data/01_raw/2020_Data_Professional_Salary_Survey_Responses.xlsx", skiprows=3)
dfk = pd.read_csv(r"original.csv")

#Create connection with mysqm
connect = mysql_connect()

# Save the table in mysql database
# save_to_mysql(db_connect=connect,df_to_save=df1,df_name='survey_1')
save_to_mysql(db_connect=connect,df_to_save=dfk,df_name='food_fact')