import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="phuangkaeo",
    password="simplon59",
    database="american"
)

cur = mydb.cursor()

file = open('test.csv')
csv_data = csv.reader(file)

skipHeader = True
for row in csv_data:
    if skipHeader:
        skipHeader = False
        continue
    cur.execute('INSERT INTO SurveyYear(SurveyYear, '
                'Timestamp,'
                'SalaryUSD,'
                'Country,'
                'PostalCode,'
                'YearsWithThisDatabase,'
                'JobTitle,'
                'ManageStaff,'
                'YearsWithThisTypeOfJob,'
                'HowManyCompanies,'
                'OtherPeopleOnYourTeam,'
                'Counter) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)
mydb.commit()
mydb.close()