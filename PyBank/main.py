import os
import csv

date = []
revenue = []

csvpath = os.path.join(".", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter = ",")

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

    great_inc = max(revenue)
    great_dec = min(revenue)


    print("Financial Analysis")
    print("-----------------------------------------")
    print("Total Months: " + str(total_month))
    print("Total Revenue: $" + str(total_revenue))
    print("Average Change: $" + str(aver_change))
    print("Greatest Increase in Profits: " + str(great_inc))
    print("Greatest Decrease in Profits: "  + str(great_dec))

        