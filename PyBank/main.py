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
    inc_index = profit_loss.index(great_inc)
    month_inc = date[inc_index]

    great_dec = min(profit_loss)
    dec_index = profit_loss.index(great_dec)
    month_dec = date[dec_index]


    print("Financial Analysis")
    print("-----------------------------------------")
    print("Total Months: " + str(total_month))
    print("Total Revenue: $" + str(total_revenue))
    print("Total Profit: $" + str(total_profit))
    print("Average Change: $" + str(aver_change))
    print("Greatest Increase in Profits: " + str(month_inc) + " " + str(great_inc))
    print("Greatest Decrease in Profits: " + str(month_dec) + " " + str(great_dec))

output_result = os.path.join(".", "analysis", "result.txt")

with open(output_result, "w") as txt_file:
    txt_file.write("Financial Analysis" + "\n") 
    txt_file.write("-----------------------------------------\n")
    txt_file.write("Total Months: " + str(total_month) + "\n")
    txt_file.write("Total Revenue: $" + str(total_revenue) + "\n")
    txt_file.write("Total Profit: $" + str(total_profit) + "\n")
    txt_file.write("Average Change: $" + str(aver_change) + "\n")
    txt_file.write("Greatest Increase in Profits: " + str(month_inc) + " " + str(great_inc) + "\n")
    txt_file.write("Greatest Decrease in Profits: " + str(month_dec) + " " + str(great_dec) + "\n")
        