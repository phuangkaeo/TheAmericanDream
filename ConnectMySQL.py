import sqlalchemy
import mysql.connector



def mysql_connect():
    # from conf.conf import mysql_pseudo, mysql_mdp
    mysql_username = "phuangkaeo"
    mysql_password = "simplon59"
    database_name = 'food_fact'
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@localhost/{2}'.format(mysql_username, mysql_password, database_name), pool_recycle=1, pool_timeout=57600).connect()
    return database_connection

def save_to_mysql(db_connect,df_to_save,df_name):
    df_to_save.to_sql(con=db_connect, name=df_name, if_exists='replace')