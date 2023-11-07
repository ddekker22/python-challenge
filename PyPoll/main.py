import os
import csv

#import budget_data.csv
election_import = os.path.join("Resources", "election_data.csv")

#create variables
total_votes = 0
candidates_all = []
#store votes in a dictionary
candidate_vote_count = {}
candidate_votes = 0
percent_vote = 0
highest_vote = 0
votes = []

#open csv and skip the header
with open(election_import) as csvfile:
    election_csv = csv.reader(csvfile, delimiter=",")
    
    #skip header
    next(election_csv)

    for row in election_csv:
        #count total votes. Note: first column in data set is ballot Id, not vote count
        total_votes += 1
        
        candidate = row[2]


        #I need to get the unique values for the different candidates
        #I need to get the individual votes for each candidate
        #How do I know how many candidates there are without looking at the results?
        #How do I ensure votes go to each unique candidate? - create a new list for each candidate 

        #determine if unique candidate has already been added to the list of candidates
        if candidate in candidates_all:
            #if candidate is in the list, add a vote
            candidate_vote_count[candidate] = candidate_vote_count[candidate] +1

        else:
            #if candidate is not in the list of all candidates, add their name and give them a vote
            candidates_all.append(candidate)
            candidate_vote_count[candidate] = 0
            candidate_vote_count[candidate] = candidate_vote_count[candidate]+1

    #print output for currently known values in terminal and in txt file
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    #export results to new file
    output_path = os.path.join("analysis", "results.txt")
    with open(output_path, "w") as results:

    #Write lines into file    
        results.write("Election Results"+ "\n")
        results.write(f"-------------------------"+ "\n")
        results.write(f"Total Votes: {total_votes}"+ "\n")
        results.write("-------------------------"+ "\n")

    #List the candidate name, percentage of vote, and vote count for each unique candidate
    for person in candidates_all:
        candidate_votes = int(candidate_vote_count[person])
        vote_percent = round((candidate_votes/total_votes)*100,3)

        #print results to terminal
        print(f"{person}: {vote_percent}% ({candidate_votes})")
        #add results to text file
        output_path = os.path.join("analysis", "results.txt")
        with open(output_path, "a") as results:
            results.write(f"{person}: {vote_percent}% ({candidate_votes})"+"\n")

        #create a list of vote counts to determine the max/winner. Use that index to print winner's name
        votes.append(candidate_vote_count[person])
    
    #Find index of winner and insert in final printout
    winner = votes.index(max(votes))
    

    #Determine winner and print results
    #winner = (max(candidate_vote_count[]))
    print("-------------------------")
    print(f"Winner: {candidates_all[winner]}")
    print("-------------------------")

    output_path = os.path.join("analysis", "results.txt")
    with open(output_path, "a") as results:
        results.write("-------------------------"+ "\n")
        results.write(f"Winner: {candidates_all[winner]}"+ "\n")
        results.write("-------------------------"+ "\n")



