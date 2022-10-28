#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period


import os
import csv

# Set path for file
filepath = os.path.join('.', 'Resources', 'budget_data.csv')

# Creating list to store data 
budget_data = []

# Opening the CSV
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)

    # Looping through the data to store in a dictionary
    for row in reader:
        budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]),"change": 0})

# Calculating the total months
total_months = len(budget_data)

# Looping through the dictionary in order to calculate changes between months
previous_amount = budget_data[0]["amount"]
for i in range(total_months):
    budget_data[i]["change"] = budget_data[i]["amount"] - previous_amount
    prev_amount = budget_data[i]["amount"]

# Calculating the total amount
total_amount = sum(row['amount'] for row in budget_data) 

# Calculating the average of amount changes
total_change = sum(row['change'] for row in budget_data)
average = round(total_change / (total_months-1), 2)

# Getting the  Greatest Increase and Decrease from the changes
max_increase = max(budget_data, key=lambda x:x['change'])
max_decrease = min(budget_data, key=lambda x:x['change'])


# Printting the Final Analysis
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {max_increase["month"]} (${max_increase["change"]})')
print(f'Greatest Decrease in Profits: {max_decrease["month"]} (${max_decrease["change"]})')


# Exporting to a text file 
exportpath = ("Results.txt")
with open(exportpath, "w") as textfile:
        textfile.write(f"Total Months: {total_months}")
        textfile.write(f"Total: ${total_amount}")
        textfile.write(f"Average Change: ${average}")
        textfile.write(f"Greatest Increase in Revenues: ${max_increase}")
        textfile.write(f"Greasest Decrease in Revenues:  ${max_decrease}")