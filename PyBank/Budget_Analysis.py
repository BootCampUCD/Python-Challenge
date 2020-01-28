#Budget Data CSV
import os
import operator
import csv

csvpath = os.path.join("budget_data.csv")

rowvalue = 0
Months = 0
Profit = 0
average = 0
highest = 0
lowest = 0
x = 0
currrentmonth = 0
previousmonth = 0
currentmonthchange = 0
monthchange = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        if rowvalue == 0:
            previousmonth = int(row[1])

        currentmonth = int(row[1])
        currentmonthchange = currentmonth - previousmonth
        print(currentmonthchange)
        if rowvalue == 0:
            monthchange = currentmonth

        if currentmonthchange > monthchange:
            monthchange = currentmonthchange
        previousmonth = int(currentmonth)
        
        rowvalue = int(row[1]) + int(rowvalue)
        Months = Months + 1
        currentvalue = int(row[1])
#        print(monthchange)

        if currentvalue > highest:
            highest = currentvalue
        if currentvalue < lowest:
            lowest = currentvalue
    next
x = int(highest) - int(lowest)
print(x)
print( Months)
print(rowvalue)
average = int(rowvalue / Months)
print("Average: ", (average))
print(highest)
print(lowest)