
import os
import csv

# Path to collect data from the Resources folder
# PyBank/Resources/budget_data.csv
budget_csv = os.path.join('Resources','budget_data.csv').replace('/', '//')


# Creating an empty list to store the date
initial_profit = []
profit = []
monthly_changes = []
date = []

# Start initializing the variables
# The count would be used to return the number of months
count = 0
total_profit = 0
total_change_profits = 0
overall_monthly_change = 0
overall_profit = 0

# This will open the CSV
with open(budget_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csvreader)
  
    # Script to read through the rows
    for row in csvreader:    
    
    # Apply Append method
      count = count +1
      date.append(row[0])
    
      # index one to look to the value column and not date
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      # Calculate the average change in profits from month over month
      initial_profit = int(row[1])
    
    #Error these two values are the same (initial returns 671099 and overall_profit returns 671099) - final returns is the last value in changes
      # This will built out the monthly changes for min and max
      overall_monthly_change = initial_profit - overall_profit

      # Apply Append method
      monthly_changes.append(overall_monthly_change)

    #Error total_change_profits returns the last value of the month
      total_change_profits = total_change_profits + overall_monthly_change
      overall_profit = initial_profit

      # Accumulate the average change
      total_variance = sum(monthly_changes[1:])
      total_elements = len(monthly_changes[1:])
      if total_elements == 0:
          average_change_profits = 0
      else:
          average_change_profits = total_variance/total_elements
               
      # Identify the min and max
      max_increase_profits = max(monthly_changes)
      minimium_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(max_increase_profits)]
      decrease_date = date[monthly_changes.index(minimium_decrease_profits)]
     
    # Print Budget data to terminal
    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total Months: {count}")
    print(f"Total Profits: {total_profit}")
    print(f"Average Change: {average_change_profits: .2f}")
    print(f"Greatest Increase in Profits: {increase_date} (${max_increase_profits})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${minimium_decrease_profits})")

  # Push data into file
  # This is the relative path "PyBank/Analysis"
with open("Analysis/Financial_Analysis.txt", 'w') as text:
    text.write("         Financial Analysis    "+ "\n")
    text.write("-------------------------------\n\n")
    text.write(f"Total Months:  {count}\n") # Pulling in the dynamic function
    text.write("Total Profits: " + "$" + str(total_profit) +"\n")
    text.write(f"Average Change: ${average_change_profits: .2f}\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(max_increase_profits) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(minimium_decrease_profits) + ")\n")


