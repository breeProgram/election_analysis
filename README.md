# election_analysis

## Background
The assignment was to assist Seth and Tom by writing a Python script to run an election audit for the election commission. They needed the script to read in the data from a text document and tally votes casted. I wrote them a script that returned total votes casted for each candidate and the candidate with most votes. Afterward the election commission requested to also tally the votes for each county and find the county with the most votes. The information for the audit is to be outputted to a text document for easy readability.
![Election_Output](https://user-images.githubusercontent.com/56700719/149681575-5bd414d7-961b-4c5e-9bb3-c4953bde38ec.JPG)

## Election Analysis
- There was a total of 369,711 votes casted
- County vote breakdown
  - Jefferson had 10.5% (38,855) of the votes casted
  - Denver had 82.8% (306,055) of the votes casted
  - Arapahoe had 6.7% (24,801) of the votes casted
- Denver had the highest voter turnout of the 3 counties by at least 70%
- Candidate vote breakdown
  - Charles Casper Stockham had 23.0% (85,213) votes casted
  - Diana DeGette had 73.8% (272,892) votes casted
  - Raymon Anthony Doane had 3.1% (11,606) votes casted
- Diana DeGette won the election with the most votes casted for them
## Audit Summary
This script was written to allow adjustments, which helped afterward when the election commission requested analysis on votes per county. The original script was written to allow for easy changes if the election commission are looking to track other information or if the order the data is organized changes
![Election_Data_Order](https://user-images.githubusercontent.com/56700719/149681596-8700c325-d278-4c1e-98c0-18a50fa4f90e.JPG)

In this block pictured above, the script reads in the document by rows. The header of this document read Ballot ID, County, Candidate. If instead another document from a different read in a different order for example Ballot ID, Candidate, County then small changes by switching the row indexing numbers. If the data also included another column of information for example polling station ID, then again updating the script would happen here. The next user would create the variable, polling_ID, then add it to the for block like so, polling_ID = row[3]. The script allows the next user easy of use as well as ability for quick changes when updating.
