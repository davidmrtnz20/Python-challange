import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

net = []
avrg = []

total = 0
net_total = 0
average_change = 0

with open(budget_data) as csv_file:

    read_budget = csv.reader(csv_file, delimiter=",")
    csv_header = next(read_budget)

    for row in read_budget:

        total += 1

        net.append(row[1])
        net_total = net_total + float(row[1])

        avrg.append(row[1])
        average_change = (average_change + float(row[1])) / total

print("Financial Analysis")
print(" ----------------------------")       
print(f"Total Months: {total}")
print(f"Net Total: $ {net_total}")
print(f"Average Change: $ {average_change}")
# print(f"Greatest Increase in Profits: $ {}")
print(" ----------------------------") 


