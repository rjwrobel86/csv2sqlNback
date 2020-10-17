#query mysql database and download data into csv file
from sqlalchemy import create_engine
import pymysql
import pandas as pd

sqlEngine = create_engine('mysql+pymysql://USERNAME:PASSWORD@localhost:3306/DATABASE')
dbConnection = sqlEngine.connect()

frame = pd.read_sql("select * from DATABASE.`TABLENAME`", dbConnection);
frame.to_csv("OUTPUT.csv")

dbConnection.close()
