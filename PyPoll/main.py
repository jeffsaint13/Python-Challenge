import os
import csv

# Path to collect data from the Resources folder
# PyPoll/election_data.csv
election_csv = os.path.join('Resources','election_data.csv').replace('/', '//')

# Creating an empty list by indexing the below:
candidate = []
vote_count = []

#For readability, it can help to assign your values to variables with descriptive names
count = 0


with open(election_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csvreader)
  
    # Script to read through the rows
    for row in csvreader:
        if row[2] not in candidate:
            candidate.append(row[2])
            vote_count.append(int(1))
        else:
            count = candidate.index(row[2])
            vote_count[count] = vote_count[count] + 1
    
    # Calculate the total vote
    overall_votes = sum(vote_count)


    # Max vote should return the winner
    the_winner = vote_count.index(max(vote_count))

    # Print data to terminal
    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {overall_votes}")
    print("-------------------------------")

    #Loop through the data
    # Looking to get the winner
    for i in range(len(candidate)):
        name = candidate[i]
        percentage = vote_count[i]/overall_votes * 100
        print(f"{name}: {percentage: .3f}% ({vote_count[i]})")

    print("-------------------------------")
    print(f"Winner: {candidate[the_winner]}")
    print("-------------------------------")


# Push data into file
# This is the relative path "PyPoll/Analysis"
with open("Analysis/Election_Analysis.txt", 'w') as text:
    text.write("Election Results"+ "\n")
    text.write("-------------------------------\n")
    text.write("Total Votes: " + str(overall_votes) + "\n")
    text.write("-------------------------------\n")
   
    #Loop through the data
    # Looking to get the winner
    for i in range(len(candidate)):
        name = candidate[i]
        percentage = vote_count[i]/overall_votes * 100
        text.write(f"{name}: {percentage: .3f}% ({vote_count[i]})\n")

    text.write("-------------------------------\n")
    text.write(f"Winner: {candidate[the_winner]}\n")
    text.write("-------------------------------\n")

