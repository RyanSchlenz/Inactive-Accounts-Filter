import csv
from datetime import datetime, timedelta

# Define the path to your input and output CSV files
input_file = 'zendesk_agents.csv'
output_file = 'inactive_accounts.csv'

# Define the time delta for 3 months
three_months_ago = datetime.now() - timedelta(days=90)

def parse_date(date_str):
    if not date_str:  # Handle empty date strings
        return None
    try:
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    except ValueError:
        return datetime.strptime(date_str, '%Y-%m-%d')

# Open the input CSV file
with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    # Collect the headers for the output file
    headers = reader.fieldnames

    # Filter and collect the results
    inactive_accounts = []
    
    for row in reader:
        last_sign_in = parse_date(row['Last sign-in'])
        support_role = row['Support role'].strip().lower()
        
        # Check if the last sign-in is more than 3 months ago and the role is not 'Light Agent'
        if (support_role != 'light agent' and (last_sign_in is None or last_sign_in < three_months_ago)):
            inactive_accounts.append(row)

# Write the results to the output CSV file
with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(inactive_accounts)

print(f"Inactive accounts saved to {output_file}")
