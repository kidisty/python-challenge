#import modules
import os
import csv

#Create a path for the CSV file
election_data = os.path.join("election_data.csv")


# create variables to hold lists
candidates = []
num_votes = []
percent_votes = []

# Set initial value
total_votes = 0

#Read the CSV file
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to our vote-counter
        total_votes=total_votes+ 1

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

    # append to percent votes list
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

    # Find the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Print results on tderminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Export file
with open("Analysis_roll.txt", "w") as text:
    text.write("Election Results"+"\n")
    text.write("--------------------------\n")
    text.write(f"Total Votes: {str(total_votes)}"+"\n")
    text.write("--------------------------\n")
    for i in range(len(candidates)):
        text.write(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})"+"\n")
        text.write( "--------------------------\n")
        text.write(f"Winner: {winning_candidate}"+"\n")
        text.write( "--------------------------\n")
