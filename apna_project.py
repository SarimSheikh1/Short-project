import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("path_to_your_credentials.json", scope)

# Authenticate and connect to Google Sheets
client = gspread.authorize(creds)

# Open the Google Sheet by its name
sheet = client.open("Your Google Sheet Name").sheet1  # Open the first sheet

# Log a transaction (appending to the sheet)
def log_transaction(data):
    sheet.append_row(data)

# Example usage: log a new transaction (date, description, amount)
log_transaction(["2024-10-23", "Sample Transaction", 250.00])
