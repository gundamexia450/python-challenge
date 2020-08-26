import os
import csv

date = []
revenue = []
profit_loss = []
last_profit = 0

csvpath = os.path.join(".", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_reader)

    total_month = 0
    for row in csv_reader:
        date.append(row[0])
        revenue.append(row[1])
        pl_diff = int(row[1]) - int(last_profit)
        last_profit = row[1]
        profit_loss.append(pl_diff)
        total_month += 1

    total_revenue = 0
    for rev_row in revenue:
        total_revenue += int(rev_row)
    
    total_profit = 0
    for pro_row in profit_loss:
        total_profit += int(pro_row)
    
    aver_change = round(total_profit/total_month, 2)

    great_inc = max(profit_loss)

    great_dec = min(profit_loss)


    print("Financial Analysis")
    print("-----------------------------------------")
    print("Total Months: " + str(total_month))
    print("Total Revenue: $" + str(total_revenue))
    print("Total Profit: $" + str(total_profit))
    print("Average Change: $" + str(aver_change))
    print("Greatest Increase in Profits: " + str(great_inc))
    print("Greatest Decrease in Profits: " + str(great_dec))
        