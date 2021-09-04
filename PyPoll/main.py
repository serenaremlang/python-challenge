# Dependencies
import os
import csv

#initalize variables
candidate = []
percent_votes = []
total_votes = 0
candidate1_votes = 0
candidate2_votes = 0
candidate3_votes = 0
candidate4_votes = 0
candidate_vote_count = []
election = {}

#Define filepath
csvpath = os.path.join('Resources', 'election_data.csv')

#Read in the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#Loop through csv to count votes and add candidates to list
    for row in csvreader:
        # set conditional to make sure each candidate is only added once to list
        if row[2] in candidate:
            total_votes += 1
        else:
            candidate.append(row[2])
            total_votes += 1
    #reset pointer to beginning of csvfile
    csvfile.seek(0)

    #Loop through csv to assign votes to each candidate
    for row in csvreader:
        #if candidate for vote is first candidate in list add to counter (repeat for each candidate)
        if row[2] == candidate[0]:
            candidate1_votes += 1
        elif row[2] == candidate[1]:
            candidate2_votes += 1
        elif row[2] == candidate[2]:
            candidate3_votes += 1
        elif row[2] == candidate[3]:
            candidate4_votes += 1

    #Add each candidates votes to candidates vote list
    candidate_vote_count = [candidate1_votes, candidate2_votes, candidate3_votes, candidate4_votes]

    #Divide each candidates votes total by total votes, convert to % and add to list
    percent_votes = [((x / total_votes)*100) for x in candidate_vote_count]

#Find the max number of votes
winner_votes = max(candidate_vote_count)
#Find the index for the max votes
winner_index = candidate_vote_count.index(winner_votes)


#Set output path
output_path = os.path.join("Analysis", "analysis.txt")
#open text file to write to
f = open(output_path, 'w', newline='')
#write to file
f.write('Election Results\n')
f.write('-'*30)
f.write(f'\nTotal Votes: {total_votes}\n')
f.write('-'*30)
f.write('\n')
#using length of candidates list to determine length of loop, use that iteration value as an index in
#candidate list, percent_votes list and candidate vote count list
for i in range(len(candidate)):
    f.write(f'{candidate[i]}: {round(percent_votes[i],3)}00% ({candidate_vote_count[i]})\n')
f.write('-'*30)
f.write(f'\nWinner: {candidate[winner_index]}\n')
f.write('-'*30)
#clost file
f.close()

#Print analysis to Terminal
print('Election Results')
print('-'*30)
print(f'Total Votes: {total_votes}')
print('-'*30)
for i in range(len(candidate)):
    print(f'{candidate[i]}: {round(percent_votes[i],3)}00% ({candidate_vote_count[i]})')
print('-'*30)
print(f'Winner: {candidate[winner_index]}')
print('-'*30)
