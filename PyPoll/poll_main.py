import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

total_num_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
o_tooley_votes = 0

with open(election_data) as csv_file:

    read_election = csv.reader(csv_file, delimiter=",")
    csv_header = next(read_election)

    for row in read_election:

        total_num_votes += 1

        if row[2] == "Khan":

            khan_votes += 1
            votes_for_khan = khan_votes/total_num_votes
        
        elif row[2] == "Correy":

            correy_votes += 1
            votes_for_correy = correy_votes/total_num_votes
        
        elif row[2] == "Li":

            li_votes += 1
            votes_for_li = li_votes/total_num_votes
        
        else:

            o_tooley_votes += 1
            votes_for_tooley = o_tooley_votes/total_num_votes
    
            if (khan_votes > correy_votes) and (khan_votes > li_votes) and (khan_votes > o_tooley_votes):

                candidate_winner = "Kahn"
            
            elif (correy_votes > khan_votes) and (correy_votes > li_votes) and (correy_votes > o_tooley_votes):

                candidate_winner = "Correy"

            elif (li_votes > khan_votes) and (li_votes > correy_votes) and (li_votes > o_tooley_votes):

                candidate_winner = "Li"

            else:

                candidate_winner = "O'Tooley"

print("")
print("Election Results")
print("-------------------------")
print(f"Total number of votes cast: {total_num_votes}")
print("-------------------------")
print("Khan: " "{0:.0%}".format(votes_for_khan) + " " + str(khan_votes))
print("Correy: " "{0:.0%}".format(votes_for_correy) + " " + str(correy_votes))
print("Li: " "{0:.0%}".format(votes_for_li) + " " + str(li_votes))
print("O'Tooley: " "{0:.0%}".format(votes_for_tooley) + " " + str(o_tooley_votes))
print("-------------------------")
print(f"Winner: {candidate_winner}")
print("-------------------------")

import sys
sys.stdout = open("Analysis/Election Results.txt", "w")
print("Election Results")
print("-------------------------")
print(f"Total number of votes cast: {total_num_votes}")
print("-------------------------")
print("Khan: " "{0:.0%}".format(votes_for_khan) + " " + str(khan_votes))
print("Correy: " "{0:.0%}".format(votes_for_correy) + " " + str(correy_votes))
print("Li: " "{0:.0%}".format(votes_for_li) + " " + str(li_votes))
print("O'Tooley: " "{0:.0%}".format(votes_for_tooley) + " " + str(o_tooley_votes))
print("-------------------------")
print(f"Winner: {candidate_winner}")
print("-------------------------")