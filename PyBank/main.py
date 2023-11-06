import os
import csv

#import budget_data.csv
budget_import = os.path.join("Resources", "budget_data.csv")

#create variables to store objects
month_list = []
profit_loss_list = []
change_profit_list = []
total_months = 0
sum_profit_loss = 0
sum_change_profit = 0
average_change = 0
greatest_inc = 0
greatest_dec = 0

#open csv and skip the header
with open(budget_import) as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=",")
    
    #skip header
    next(budget_csv)
    
    #budget_list = list(budget_csv)
    #print(budget_list)
    
    #cycle through csv file and add items to new lists
    for row in budget_csv:
        month_list.append(row[0])
        profit_loss_list.append(row[1])

        #add the value of profit/loss column to the sum
        sum_profit_loss += int(row[1])

    #count months
    total_months = len(month_list)

    #calculate values for change in profit/loss and add to new list. List indecies will be 1 off from month list
    for i in range(total_months-1):
        change_profit_list.append(float(profit_loss_list[i+1])-float(profit_loss_list[i]))


    #calculate average change in profit/loss: total of change_profit_list, divided by total months - 1 (1 less row than month list)
    sum_change_profit = sum(change_profit_list)
    average_change = round(sum_change_profit/(total_months - 1), 2)

    #greatest inc and dec in profits
    greatest_inc = round(max(change_profit_list))
    inc_index = change_profit_list.index(max(change_profit_list))+1

    greatest_dec = round(min(change_profit_list))
    dec_index = change_profit_list.index(min(change_profit_list))+1


#print results in terminal
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(sum_profit_loss))
    print("Average Change: $" + str(average_change))
    print(f"Greatest Increase in Profits: {month_list[inc_index]} (${greatest_inc})")
    print(f"Greatest Decrease in Profits: {month_list[dec_index]} (${greatest_dec})")

#export results to new file
output_path = os.path.join("analysis", "results.txt")
with open(output_path, "w") as results:
    results.write("Financial Analysis"+ "\n")
    results.write("----------------------------" + "\n")
    results.write("Total Months: " + str(total_months)+"\n")
    results.write("Total: $" + str(sum_profit_loss)+ "\n")
    results.write("Average Change: $" + str(average_change) + "\n")
    results.write(f"Greatest Increase in Profits: {month_list[inc_index]} (${greatest_inc})" + "\n")
    results.write(f"Greatest Decrease in Profits: {month_list[dec_index]} (${greatest_dec})")
