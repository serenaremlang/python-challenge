#import modules
import os
import csv

#initalize variables
change_profloss = []
change_profloss_date = []
previous_row = 0
current_row = 0
month_count = 0
net_total = 0

#read in datafile
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#Analysis
    for row in csvreader:
        #total number of months in dataset
        month_count += 1

        #net total amount of Profit/Losses over entire period
        net_total = int(row[1]) + net_total

        #Change in Profit/Losses over entire period then find average of those changes
        #**ask how this would be calculated

        current_row = float(row[1])
        change_profloss.append(current_row-previous_row)
        change_profloss_date.append(row[0])
        previous_row = current_row

    #Average profit/Losses
    average_profloss = 0
    print(sum(change_profloss))
    print(len(change_profloss))

    #greatest increase in profits (date and amount) over the entire period
    greatest_increase = int(max(change_profloss))
    greatest_increase_date = change_profloss_date[change_profloss.index(greatest_increase)]


    #greatest decrease in profits (date and amount) over entire period
    greatest_decrease = int(min(change_profloss))
    greatest_decrease_date = change_profloss_date[change_profloss.index(greatest_decrease)]

#Export results to text file
output_path = os.path.join("Analysis", "analysis.txt")
f = open(output_path, 'w', newline='')
f.write('Financial Analysis\n')
f.write('-'*30)
f.write(f'\nTotal Months: {month_count}\n')
f.write(f'Total: ${net_total}\n')
f.write(f'Average Change: ${average_profloss}\n')
f.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n')
f.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n')

f.close()

#Print analysis
print('Financial Analysis')
print('-'*30)
print(f'Total Months: {month_count}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_profloss}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')
