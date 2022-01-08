# Analysis of Election Audit
## Overview of Election Audit
I am assisting a Colorado Board of Elections employee, Tom, in performing an election audit of the tabulated results for a US congressional precinct in Colorado. While the election results can easily be found through Excel, Tom wants to automate the analysis so that it may be used for other congressional districts as well.
### Purpose
The purpose of this analysis is to write a [Python script](PyPoll_Challenge.py) that will access the [Election Results document](Resources/election_results.csv) and loop through the data to determine who the candidates where, how many votes each candidate had, and who won the election by having the largest vote percentage. The script also determined which counties participated in the election and how many votes were cast in each county.
## Election-Audit Results
The full analysis of the election results are as follows: [Election Analysis](Analysis/election_analysis.txt)
- **How many votes were cast in this congressional election?**
  - There were 369,711 votes cast in this congressional election. This was found by creating a variable set to zero, `total_votes = 0` and looping through the election results while increasing the value of the variable: 
```
  # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1
```
        
- **Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct**
  - Three counties participated in the election. Jefferson County had 38,855 votes cast, which was 10.5% of the total. Denver County had 306,055 votes cast, which was 82.8% of the total. Arapahoe County had 24,801 votes, which was 6.7% of the total. This information was found using the following script:
```
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:
       # 3: Extract the county name from each row.
        county_name = row[1]
       # county does not match any existing county in the county list.
        if county_name not in counties:

            # 4b: Add the existing county to the list of counties.
            counties.append(county_name)

            # 4c: Begin tracking the county's vote count.
            counties_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        counties_votes[county_name] += 1
```
- **Which county had the largest number of votes**
  - Denver County had the most votes cast.
- **Provide a breakdown of the number of votes and the percentage of the total votes each candidate received**
  - Charles Casper Stockham had 85,213 votes (23.0%), Diana DeGette had 272,892 votes (73.8%), and Raymon Anthony Doane had 11,606 votes (3.1%). This information was found using the same script as before, but with different variables to determine candidate information.
- **Which candidate won the election, what was their vote count, and what was their percentage of the total votes?**
  - Diana DeGette won the election with 272,892 votes and 73.8% of the total votes.
## Election-Audit Summary
As can be seen, this script is an effective and automated way to easily analyze election results. By simply updating the `file_to_load` path to open a similarly formatted CSV document, any election results can be analyzed. Also, the script is easy to modify to fit the needs of a given election. Sometimes election ballots allow voters to vote on multiple candidates for diffenent possitions. To accomidate this, new lists and dictionaries `secondary_candidate_options = [], secondary_candidate_votes = {}` could be inserted before the `with open(file_to_load) as election_data`statement, and within the `for` loop, the variable `secondary_candidate_name = row[3]` could be created. Then, an `if` statement would be created using the new variables and lists with the same format as the original candidate `if` statment, and an output variable would be created. This could be repeated for each additional candidate bracket on the ballot.
```
if secondary_candidate_name not in secondary_candidate_options:

            # Add the candidate name to the candidate list.
            secondary_candidate_options.append(secondary_candidate_name)

            # And begin tracking that candidate's voter count.
            secondary_candidate_votes[secondary_candidate_name] = 0

        # Add a vote to that candidate's count
        secondary_candidate_votes[secondary_candidate_name] += 1
 ```
 Another modification that could be made to the script is the addition of a means to collect votes on ammendement changes. In some elections, ballots will include a section that allows voters to show support for proposed ammendments, often in the form of a "yes" or "no" question. These results can also be analysed by creating a new variable before the `with open(file_to_load) as election_data` statement: `question_yes = 0`. Then, after the `with open(file_to_load) as election_data` statement and within the `for` loop, create an `if` statement:
```
if row[4] == "YES"
  question_yes += 1
```
Then, within the `with open(file_to_save, "w") as txt_file` statement, an output variable that finds the percentage of "YES" votes out of the total votes in order to show the percentage of voters who voted for the ammendment.
