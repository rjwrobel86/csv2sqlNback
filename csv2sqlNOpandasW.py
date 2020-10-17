###reads a csv file into mysql by turning it into a list of lists and using "executemany"
import mysql.connector
import csv

cnx = mysql.connector.connect(user='USERNAME', password='PASSWORD',
                              host='127.0.0.1',
                              database='DATABASE')

cursor = cnx.cursor()
listofrows = []

with open('EXAMPLE.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    metalist = list(csv_reader)

#can variables list be subbed into the query below?
#variables = "a, b, c, d"
#print(variables)

cursor.executemany("INSERT INTO table(a, b, c, d) VALUES (%s, %s, %s, %s)", metalist)

cnx.commit()
cursor.close()
cnx.close()
print('done')


#from csv import reader
#import pandas not needed? - uses csv and list of lists
