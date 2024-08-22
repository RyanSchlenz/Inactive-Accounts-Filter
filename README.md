Inactive Accounts Filter Script

This Python script identifies inactive accounts from a CSV file of Zendesk agents and outputs a new CSV file containing only those accounts that have been inactive for more than 3 months.

Overview
The script performs the following tasks:

Reads an input CSV file containing Zendesk agent data.
Parses the 'Last sign-in' date and filters out agents who have not signed in for more than 3 months.
Excludes agents with the role 'Light Agent' from the results.
Writes the filtered data to a new CSV file.
Prerequisites
Python 3.x
The input CSV file should have columns: 'Last sign-in' and 'Support role'.
