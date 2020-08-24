import os
import csv

vote = []
county = []
candppl = []
votepercent = []

csvpath = os.path.join(".", "Resources", "election_data.csv")

with open(csvpath) as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_reader)

    total_vote = 0
    for row in csv_reader:
        vote.append(row[0])
        county.append(row[1])
        candppl.append(row[2])
        total_vote += 1
    
    cand_vote = 0
    cand_list = zip(cand, votepercent, vote)




print("Election Results")
print("----------------------------------")
print("Total Votes: " + str(total_vote))
print("----------------------------------")
print("----------------------------------")
print("----------------------------------")