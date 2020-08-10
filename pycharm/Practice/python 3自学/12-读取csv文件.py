# -*-coding:UTF-8 -*-
"""
import csv

with open(r'E:\YZ\data\data1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        #print(row)

        #print(row[0])
        print(row[0], row[1])

"""

import csv

with open(r'E:\YZ\data\data1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    citys = []
    password = []
    days = []
    for row in readCSV:
        city = row[0]
        paword = row[1]
        day = row[2]

        citys.append(city)
        password.append(paword)
        days.append(day)

    print(citys)
    print(password)
    print(days)