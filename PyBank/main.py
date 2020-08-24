import os
import csv

date = []
revenue = []

csvpath = os.path.join(".", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter = ",")

    print(csv_reader)

    csv_header = next(csv_reader)

    total_month = 0
    for row in csv_reader:
        date.append(row[0])
        revenue.append(row[1])
        total_month += 1
    
    total_revenue = 0
    for rev_row in revenue:
        total_revenue += int(rev_row)

    aver_change = round(total_revenue / total_month, 2)

    great_increase = revenue[0]
    great_decrease = revenue[0]
    for great_row in revenue:
        if revenue[int(great_row)] > revenue[int(great_row) + 1]:
            great_increase = revenue[great_row]
        else:
            great_increase = revenue[great_row +1]

    print("Financial Analysis")
    print("-----------------------------------------")
    print("Total Months: " + str(total_month))
    print("Total Revenue: $" + str(total_revenue))
    print("Average Change: $" + str(aver_change)) 

        