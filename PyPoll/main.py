# Dependencies
import os
import csv

#Define filepath
csvpath = os.path.join('Resources', 'election_data.csv')

#Read in the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#Analysis
    for row in csvreader:
        #The total number of votes cast
        total_votes += 1

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.


#Export results to text file
output_path = os.path.join("Analysis", "analysis.txt")
f = open(output_path, 'w', newline='')
f.write('Election Results\n')
f.write('-'*30)
f.write(f'\nTotal Votes: {vote_count}\n')
f.write('-'*30)
f.write('\n')
for i in candidate:
    f.write(f'{cadidate[i]}: {percent_votes[i]}% ({candidate_vote_count[i]})\n')
f.write('-'*30)
f.write(f'\nWinner: {cadidate[0]}\n')
f.write('-'*30)
f.close()

#Print analysis to Terminal
print('Election Results\n')
print('-'*30)
print(f'\nTotal Votes: {vote_count}\n')
print('-'*30)
print('\n')
for i in candidate:
    print(f'{cadidate[i]}: {percent_votes[i]}% ({candidate_vote_count[i]})\n')
print('-'*30)
print(f'\nWinner: {cadidate[0]}\n')
print('-'*30)
