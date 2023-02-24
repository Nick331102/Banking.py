class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
        
    def get_balance(self):
        return self.balance
    
# instance of BankAccount with an initial balance of $1000 and display the current balance.
bank_account = BankAccount(123456, 1000)

#Use a while loop to prompt the user to choose an action to perform: deposit, withdraw, or exit the program.
running = True
while running:
    user_support = input("What action would you like to take? Deposit, Withdraw, Balance Inquiry? or Exit? ")
    if user_support == "Withdraw":
        withdraw_amount = int(input("How much would you like to withdraw? "))
        bank_account.withdraw(withdraw_amount)
# display the current balance.
        print(f"Your balance after the withdrawal is: {bank_account.get_balance()} dollars")
    elif user_support == "Deposit":
        deposit_amount = int(input("How much would you like to deposit? "))
        bank_account.deposit(deposit_amount)
# display the current balance.
        print(f"Your balance after the depsit is: {bank_account.get_balance()} dollars")
    elif user_support == "Balance Inquiry":
        print(f"Your balance is: {bank_account.get_balance()} dollars")
    else:
        print("Thank you for banking with us!")
        running = False
        
    
    