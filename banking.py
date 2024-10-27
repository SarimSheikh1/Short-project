import streamlit as st

# Account classes
class Account:
    def __init__(self, account_number, account_holder, bank_name, personal_name):
        self.account_number = account_number
        self.account_holder = account_holder
        self.bank_name = bank_name
        self.personal_name = personal_name
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        return f"{amount} deposited successfully."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
            return f"{amount} withdrawn successfully."

    def get_balance(self):
        return f"Current balance: {self.balance}"

    def show_transactions(self):
        return "\n".join(self.transactions)

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, bank_name, personal_name, interest_rate):
        super().__init__(account_number, account_holder, bank_name, personal_name)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)
        return f"Interest added: {interest}"

# Streamlit app setup
st.title("Bank Account Management System")

# Initialize session state for account
if "account" not in st.session_state:
    st.session_state.account = None

# Account creation form
st.subheader("Create Account")
account_number = st.text_input("Account Number")
account_holder = st.text_input("Account Holder")
bank_name = st.text_input("Bank Name")
personal_name = st.text_input("Personal Name")
interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, step=0.1)
initial_deposit = st.number_input("Initial Deposit Amount", min_value=0.0)

if st.button("Create Account"):
    try:
        st.session_state.account = SavingsAccount(account_number, account_holder, bank_name, personal_name, interest_rate)
        st.session_state.account.deposit(initial_deposit)
        st.success(f"Account created successfully at {bank_name} for {personal_name} ({account_holder}) with an initial deposit of {initial_deposit}.")
    except ValueError:
        st.error("Please enter valid values for interest rate and initial deposit.")

# Banking operations
if st.session_state.account:
    st.subheader("Operations")
    
    # Deposit
    deposit_amount = st.number_input("Deposit Amount", min_value=0.0, key="deposit")
    if st.button("Deposit"):
        message = st.session_state.account.deposit(deposit_amount)
        st.success(message)

    # Withdraw
    withdraw_amount = st.number_input("Withdraw Amount", min_value=0.0, key="withdraw")
    if st.button("Withdraw"):
        message = st.session_state.account.withdraw(withdraw_amount)
        st.success(message)

    # Show Balance
    if st.button("Show Balance"):
        balance = st.session_state.account.get_balance()
        st.info(balance)

    # Add Interest
    if st.button("Add Interest"):
        message = st.session_state.account.add_interest()
        st.success(message)

    # Show Transactions
    if st.button("Transaction History"):
        transactions = st.session_state.account.show_transactions()
        st.text_area("Transaction History", transactions, height=200)

else:
    st.warning("Please create an account first.")
