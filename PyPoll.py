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

# Open the election results and read the file.
with open(file_to_load) as election_data:

     # To do: read and analyze the data here.
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)

     # # Print each row in the CSV file
     # for row in file_reader:
     #      print(row)
     
     # Read and print the header row
     headers = next(file_reader)
     print(headers)

   