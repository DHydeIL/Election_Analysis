# from typing import cast


# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of votes each candidate won
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes

# Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# 1. initialize votes variable to zero prior to opening the file
total_votes = 0

candidate_options = []
# Declare an empty dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

     # To do: read and analyze the data here.
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)

     # Read and print the header row
     headers = next(file_reader)

     # Print each row in the CSV file
     for row in file_reader:
          # 2. Add ot the total vote count
          total_votes += 1
          # Print the candidate name from each row
          candidate_name = row[2]
          # If the cnadidate does not match any existing candidate . . .
          if candidate_name not in candidate_options:
              # Add candidate name to candidate option list
              candidate_options.append(candidate_name)
              # Begin tracking that candidate's vote count.
              candidate_votes[candidate_name] = 0
          # Add a vote to that candidate's count
          candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

     # Print the final vote count to the terminal
     election_results = (
          f"\nElection Results\n"
          f"---------------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"---------------------------\n"
     )
     print(election_results, end="")
     #save the final vote count to the text file
     txt_file.write(election_results
     )
     # Determine the percentage of votes for each candidate by looping through the counts.
     # 1. Iterate through the candidate list.
     for candidate_name in candidate_votes:
          # 2. Retrieve vote count of a candidate.
          votes = candidate_votes[candidate_name]
          # 3. Calculate the percentage of votes.
          vote_percentage = float(votes) / float(total_votes) * 100
          candidate_results = (
               f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
          )
          print(candidate_results)
          # Save the candidate results
          txt_file.write(candidate_results)
          
          # 1. Determine if the votes are greater than the winning count.
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               # 2. If true then set winning_count = votes and winning_percent =
               # vote_percentage.
               winning_count = votes
               winning_percentage = vote_percentage
               # 3. Set the winning_candidate equal to the candidate's name.
               winning_candidate = candidate_name
     winning_candidate_summary = (
          f"-------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"-------------------------\n")
     print(winning_candidate_summary)
     # Save the winning candidate's results to the text file
     txt_file.write(winning_candidate_summary)
   