import os
import csv

vote_count = []
county = []
candppl = []
cand_list = ["Khan", "Correy", "O'Tooley", "Li"]
khan_vote = 0
correy_vote = 0
tooley_vote = 0
li_vote = 0

csvpath = os.path.join(".", "Resources", "election_data.csv")
    

with open(csvpath) as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_reader)

    for row in csv_reader:
        vote_count.append(row[0])
        county.append(row[1])
        candppl.append(row[2])

    total_vote = len(vote_count)
    
    
    for name in candppl:
        if name == cand_list.index("Khan"):
            khan_vote += 1
        elif name == cand_list.index("Correy"):
            correy_vote += 1
        elif name == cand_list.index("O'Tooley"):
            tooley_vote += 1
        elif name == cand_list.index("Li"):
            li_vote += 1
        else:
            cand_list.append(name)

print(str(khan_vote) + str(correy_vote) + str(tooley_vote) + str(li_vote))
    


print("Election Results")
print("----------------------------------")
print("Total Votes: " + str(total_vote))
print("----------------------------------")
print("----------------------------------")
print("----------------------------------")


