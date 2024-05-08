import random

def create_account(accounts, account_id, initial_balance=0):
    if account_id in accounts:
        return "Account already exists."
    elif initial_balance < 0:
        raise ValueError("Initial balance cannot be negative.")
    elif not isinstance(initial_balance, (int, float)):
        raise TypeError("Initial balance must be a number.")
    else:
        accounts[account_id] = initial_balance
        return f"Account {account_id} created successfully with balance {initial_balance}."


def deposit(accounts, account_id, amount):
    if account_id not in accounts:
        return "Account does not exist."
    elif amount < 0:
        raise ValueError("Deposit amount cannot be negative.")
    elif not isinstance(amount, (int, float)):
        raise TypeError("Deposit amount must be a number.")
    else:
        accounts[account_id] += amount
        return f"Deposited {amount} to account {account_id}. New balance is {accounts[account_id]}."


def withdraw(accounts, account_id, amount):
    if account_id not in accounts:
        return "Account does not exist."
    elif amount < 0:
        raise ValueError("Withdrawal amount cannot be negative.")
    elif not isinstance(amount, (int, float)):
        raise TypeError("Withdrawal amount must be a number.")
    elif accounts[account_id] < amount:
        return "Insufficient funds."
    else:
        accounts[account_id] -= amount
        return f"Withdrew {amount} from account {account_id}. New balance is {accounts[account_id]}."

def check_balance(accounts, account_id):
    if account_id in accounts:
        return f"Account {account_id} has balance {accounts[account_id]}."
    else:
        return "Account does not exist."

def transfer(accounts, from_account, to_account, amount):
    if from_account == to_account:
        return "Cannot transfer to the same account."
    elif from_account not in accounts or to_account not in accounts:
        return "One or both accounts do not exist."
    elif amount < 0:
        raise ValueError("Transfer amount cannot be negative.")
    elif not isinstance(amount, (int, float)):
        raise TypeError("Transfer amount must be a number.")
    elif accounts[from_account] < amount:
        return "Insufficient funds in the source account."
    else:
        accounts[from_account] -= amount
        accounts[to_account] += amount
        return f"Transferred {amount} from account {from_account} to account {to_account}."

def gamble(accounts, account_id):
    if account_id in accounts:
        current_balance = accounts[account_id]
        if current_balance > 0:
            bet_amount = float(input(f"Enter the amount you want to bet (current balance: {current_balance}): "))
            if bet_amount > current_balance:
                print("You don't have enough balance to place that bet.")
            else:
                chosen_number = int(input("Choose a number between 1 and 6: "))
                if chosen_number < 1 or chosen_number > 6:
                    print("Invalid number. Please choose a number between 1 and 6.")
                else:
                    roll = random.randint(1, 6)
                    print(f"You rolled: {roll}")
                    if roll == chosen_number:
                        accounts[account_id] += bet_amount
                        print(f"Congratulations! You won {bet_amount}. Your new balance is {accounts[account_id]}.")
                    elif abs(roll - chosen_number) == 1:
                        print(f"You were close! Your balance is still {accounts[account_id]}.")
                    else:
                        accounts[account_id] -= bet_amount
                        print(f"Sorry, you lost {bet_amount}. Your new balance is {accounts[account_id]}.")
        else:
            print("You don't have any balance to gamble with.")
    else:
        print("Account does not exist.")

def main():
    accounts = {}

    while True:
        print("\nOptions:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Gamble")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            acc_id = input("Enter account ID: ")
            initial_balance = float(input("Enter initial balance: "))
            print(create_account(accounts, acc_id, initial_balance))

        elif choice == '2':
            acc_id = input("Enter account ID: ")
            amount = float(input("Enter amount to deposit: "))
            print(deposit(accounts, acc_id, amount))

        elif choice == '3':
            acc_id = input("Enter account ID: ")
            amount = float(input("Enter amount to withdraw: "))
            print(withdraw(accounts, acc_id, amount))

        elif choice == '4':
            acc_id = input("Enter account ID: ")
            print(check_balance(accounts, acc_id))

        elif choice == '5':
            from_acc = input("Enter from account ID: ")
            to_acc = input("Enter to account ID: ")
            amount = float(input("Enter amount to transfer: "))
            print(transfer(accounts, from_acc, to_acc, amount))

        elif choice == '6':
            acc_id = input("Enter account ID: ")
            gamble(accounts, acc_id)

        elif choice == '7':
            print("Exiting program.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()