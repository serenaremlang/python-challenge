#import modules
import os
import csv

#read in datafile
csvpath = os.path.join('..', 'Resources', 'budger_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#total number of months in dataset

#net total amount of Profit/Losses over entire period


#Change in Profit/Losses over entire period then find average of those changes


#greatest increase in profits (date and amount) over the entire period


#greatest decrease in profits (date and amount) over entire period

#Export results to text file


#Print analysis
print('Financial Analysis')
print('-'*30)
print(f'Total Months: {}')
print(f'Total: ${}')
print(f'Average Change: ${}')
print(f'Greatest Increase in Profits: {} {}')
print(f'Greatest Decrease in Profits: {} {}')
