import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

net = []
month_to_month_changes = []
dates = []

total = 0
net_total = 0
previous_change = 0
total_change = 0

with open(budget_data) as csv_file:

    read_budget = csv.reader(csv_file, delimiter=",")
    csv_header = next(read_budget)

    for row in read_budget:

        total += 1

        net.append(row[1])
        net_total = net_total + float(row[1])

        change = int(row[1])
        monthly_change = change - previous_change

        dates.append(row[0])
        month_to_month_changes.append(monthly_change)

        total_change = total_change + monthly_change
        previous_change = change
        average_change = (total_change/total)

        great_increase = max(month_to_month_changes)
        increase_date = dates[month_to_month_changes.index(great_increase)]
        great_decrease = min(month_to_month_changes)
        decrease_date = dates[month_to_month_changes.index(great_decrease)]

print("")
print("Financial Analysis")
print("----------------------------")       
print(f"Total Months: {total}")
print(f"Total: $ {net_total}")
print(f"Average Change: $ {round(average_change,2)}")
print(f"Greatest Increase in Profits: $ {increase_date} {great_increase}")
print(f"Greatest Decrease in Profits: $ {decrease_date} {great_decrease}")
print("----------------------------")

import sys
sys.stdout = open("Analysis/Financial Analysis", "w")
print("Financial Analysis")
print("----------------------------")       
print(f"Total Months: {total}")
print(f"Total: $ {net_total}")
print(f"Average Change: $ {round(average_change,2)}")
print(f"Greatest Increase in Profits: $ {increase_date} {great_increase}")
print(f"Greatest Decrease in Profits: $ {decrease_date} {great_decrease}")
print("----------------------------")


