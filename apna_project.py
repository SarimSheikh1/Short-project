import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Google Sheets API Integration Class
class Account:
    def __init__(self, bal, acc, sheet_id, credentials_file):
        self.balance = bal
        self.account_no = acc
        self.sheet_id = sheet_id
        
        # Authenticate with Google API
        self.creds = service_account.Credentials.from_service_account_file(credentials_file)
        self.service = build('sheets', 'v4', credentials=self.creds)
        self.sheet = self.service.spreadsheets()

    def debit(self, amount):
        self.balance -= amount
        self.log_transaction("Debit", amount)
        return f"RS. {amount} was debited from your account. Your new balance is: {self.get_balance()}"

    def credit(self, amount):
        self.balance += amount
        self.log_transaction("Credit", amount)
        return f"RS. {amount} was credited to your account. Your new balance is: {self.get_balance()}"

    def get_balance(self):
        return self.balance
    
    def log_transaction(self, transaction_type, amount):
        # Log transaction in Google Sheets
        values = [
            [transaction_type, amount, self.balance]
        ]
        body = {
            'values': values
        }
        result = self.sheet.values().append(
            spreadsheetId=self.sheet_id,
            range="Sheet1!A1",  # Adjust based on your Google Sheet range
            valueInputOption="USER_ENTERED",
            body=body
        ).execute()

# Streamlit app layout
def main():
    st.title("Bank Account Management App")
    
    # Google Sheets details (replace with your own)
    sheet_id = "YOUR_GOOGLE_SHEET_ID"
    credentials_file = "path_to_your_service_account_json_file.json"

    # Create account instance
    acc1 = Account(10000, 66166, sheet_id, credentials_file)

    st.write(f"Account Number: {acc1.account_no}")
    st.write(f"Initial Balance: RS. {acc1.get_balance()}")

    # Debit Section
    st.subheader("Debit Amount")
    debit_amount = st.number_input("Enter amount to debit:", min_value=0, step=1)
    if st.button("Debit"):
        result = acc1.debit(debit_amount)
        st.success(result)

    # Credit Section
    st.subheader("Credit Amount")
    credit_amount = st.number_input("Enter amount to credit:", min_value=0, step=1)
    if st.button("Credit"):
        result = acc1.credit(credit_amount)
        st.success(result)

    # Show final balance
    st.write(f"Final Balance: RS. {acc1.get_balance()}")

if __name__ == "__main__":
    main()
