import os
import csv

# Set path for file
csvpath = os.path.join('.', "Resources", "election_data.csv")

with open(csvpath, newline="") as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=",")
    csv_headers = next(csv_reader, None)


    # Print Heading 
    print ("Election Results")
    print ("-----------------------")

    # Creating list to store data
    candidate_list = []

    # Declare variables
    total_votes = 0
    stockham_votes = 0
    degette_votes = 0
    doane_votes = 0
        
    # Loop through csv_reader
    for row in csv_reader: 

            total_votes +=1

            # Three candidates; If the name is found, count appearances and list
            if row[2] == "Charles Casper Stockham": 
                stockham_votes +=1
            elif row[2] == "Diana DeGette":
                degette_votes +=1
            elif row[2] == "Raymon Anthony Doane": 
                doane_votes +=1

    # Make dictionary out of lists
    candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
    votes = [stockham_votes, degette_votes,doane_votes]

    # Zip together with list of candidate
    dict_candidates_and_votes = dict(zip(candidates,votes))
    key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

    # Print a the summary of the analysis
    stockham_percent = (stockham_votes/total_votes) *100
    degette_percent = (degette_votes/total_votes) * 100
    doane_percent = (doane_votes/total_votes)* 100

    # Print the summary table
    print(f"Election Results")
    print(f"----------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"----------------------------")
    print(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
    print(f"Diana DeGette: {degette_percent:.3f}% ({degette_votes})")
    print(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
    print(f"----------------------------")
    print(f"Winner: {key}")
    print(f"----------------------------")

# Output files
# Assign output file location and with the pathlib library
exportpath = ("Results.txt")
with open(exportpath, "w") as textfile:

# Write methods to print to Elections_Results_Summary 
    textfile.write(f"Election Results")
    textfile.write("\n")
    textfile.write(f"----------------------------")
    textfile.write("\n")
    textfile.write(f"Total Votes: {total_votes}")
    textfile.write("\n")
    textfile.write(f"----------------------------")
    textfile.write("\n")
    textfile.write(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
    textfile.write("\n")
    textfile.write(f"Diana DeGette: {degette_percent:.3f}% ({degette_votes})")
    textfile.write("\n")
    textfile.write(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
    textfile.write("\n")
    textfile.write(f"----------------------------")
    textfile.write("\n")
    textfile.write(f"Winner: {key}")
    textfile.write("\n")
    textfile.write(f"----------------------------")
