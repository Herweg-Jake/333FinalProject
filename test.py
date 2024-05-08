import unittest
from main import create_account, deposit, withdraw, transfer, check_balance

class CreateAccountTests(unittest.TestCase):
    def setUp(self):
        self.accounts = {}

    def test_create_new_account(self):
        account_id = "account1"
        initial_balance = 1000

        result = create_account(self.accounts, account_id, initial_balance)
        expected_result = f"Account {account_id} created successfully with balance {initial_balance}."

        self.assertEqual(result, expected_result)
        self.assertEqual(self.accounts[account_id], initial_balance)

    def test_create_account_with_default_balance(self):
        account_id = "account2"

        result = create_account(self.accounts, account_id)
        expected_result = f"Account {account_id} created successfully with balance 0."

        self.assertEqual(result, expected_result)
        self.assertEqual(self.accounts[account_id], 0)

    def test_create_existing_account(self):
        account_id = "account3"
        initial_balance = 500

        create_account(self.accounts, account_id, initial_balance)
        result = create_account(self.accounts, account_id, initial_balance)
        expected_result = "Account already exists."

        self.assertEqual(result, expected_result)
        self.assertEqual(self.accounts[account_id], initial_balance)

    def test_create_account_with_negative_balance(self):
        account_id = "account4"
        initial_balance = -100

        with self.assertRaises(ValueError):
            create_account(self.accounts, account_id, initial_balance)

    def test_create_account_with_non_numeric_balance(self):
        account_id = "account5"
        initial_balance = "abc"

        with self.assertRaises(TypeError):
            create_account(self.accounts, account_id, initial_balance)

class CheckBalanceTests(unittest.TestCase):
    def setUp(self):
        self.accounts = {}
        create_account(self.accounts, "account1", 1000)
        create_account(self.accounts, "account2", 0)

    def test_check_balance_existing_account(self):
        account_id = "account1"
        expected_result = f"Account {account_id} has balance {self.accounts[account_id]}."

        result = check_balance(self.accounts, account_id)

        self.assertEqual(result, expected_result)

    def test_check_balance_zero_balance(self):
        account_id = "account2"
        expected_result = f"Account {account_id} has balance 0."

        result = check_balance(self.accounts, account_id)

        self.assertEqual(result, expected_result)

    def test_check_balance_non_existing_account(self):
        account_id = "account3"
        expected_result = "Account does not exist."

        result = check_balance(self.accounts, account_id)

        self.assertEqual(result, expected_result)

    def test_check_balance_after_deposit(self):
        account_id = "account1"
        deposit_amount = 500
        deposit(self.accounts, account_id, deposit_amount)
        expected_balance = self.accounts[account_id]
        expected_result = f"Account {account_id} has balance {expected_balance}."

        result = check_balance(self.accounts, account_id)

        self.assertEqual(result, expected_result)

    def test_check_balance_after_withdraw(self):
        account_id = "account1"
        withdraw_amount = 500
        self.accounts[account_id] -= withdraw_amount
        expected_balance = self.accounts[account_id]
        expected_result = f"Account {account_id} has balance {expected_balance}."

        result = check_balance(self.accounts, account_id)

        self.assertEqual(result, expected_result)

class DepositTests(unittest.TestCase):
    def setUp(self):
        self.accounts = {}
        create_account(self.accounts, "account1", 1500)  

    def test_deposit_to_existing_account(self):
        account_id = "account1"
        deposit_amount = 500
        result = deposit(self.accounts, account_id, deposit_amount)
        expected_balance = 2000  
        expected_result = f"Deposited {deposit_amount} to account {account_id}. New balance is {expected_balance}."
        self.assertEqual(result, expected_result)
        self.assertEqual(self.accounts[account_id], expected_balance)

    def test_deposit_zero_amount(self):
        account_id = "account1"
        deposit_amount = 0

        result = deposit(self.accounts, account_id, deposit_amount)
        expected_balance = self.accounts[account_id]
        expected_result = f"Deposited {deposit_amount} to account {account_id}. New balance is {expected_balance}."

        self.assertEqual(result, expected_result)
        self.assertEqual(self.accounts[account_id], expected_balance)

    def test_deposit_to_non_existing_account(self):
        account_id = "account3"
        deposit_amount = 1000

        result = deposit(self.accounts, account_id, deposit_amount)
        expected_result = "Account does not exist."

        self.assertEqual(result, expected_result)

    def test_deposit_negative_amount(self):
        account_id = "account1"
        deposit_amount = -500

        with self.assertRaises(ValueError):
            deposit(self.accounts, account_id, deposit_amount)

    def test_deposit_non_numeric_amount(self):
        account_id = "account1"
        deposit_amount = "abc"

        with self.assertRaises(TypeError):
            deposit(self.accounts, account_id, deposit_amount)

class BankingSystemIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.accounts = {}

    def test_create_account_and_deposit(self):
        account_id = "account1"
        initial_balance = 1000
        deposit_amount = 500

        create_account(self.accounts, account_id, initial_balance)
        deposit(self.accounts, account_id, deposit_amount)

        self.assertEqual(self.accounts[account_id], initial_balance + deposit_amount)

    def test_withdraw_and_check_balance(self):
        account_id = "account2"
        initial_balance = 2000
        withdraw_amount = 500

        create_account(self.accounts, account_id, initial_balance)
        withdraw(self.accounts, account_id, withdraw_amount)
        balance = check_balance(self.accounts, account_id)

        expected_balance = f"Account {account_id} has balance {initial_balance - withdraw_amount}."
        self.assertEqual(balance, expected_balance)

    def test_transfer_between_accounts(self):
        account_id_1 = "account3"
        account_id_2 = "account4"
        initial_balance_1 = 3000
        initial_balance_2 = 1000
        transfer_amount = 1500

        create_account(self.accounts, account_id_1, initial_balance_1)
        create_account(self.accounts, account_id_2, initial_balance_2)
        transfer(self.accounts, account_id_1, account_id_2, transfer_amount)

        self.assertEqual(self.accounts[account_id_1], initial_balance_1 - transfer_amount)
        self.assertEqual(self.accounts[account_id_2], initial_balance_2 + transfer_amount)
    
    def test_deposit_and_gamble(self):
        account_id = "account1"
        initial_balance = 500
        deposit_amount = 300
        bet_amount = 200
        chosen_number = 3

        create_account(self.accounts, account_id, initial_balance)
        deposit(self.accounts, account_id, deposit_amount)
        original_balance = self.accounts[account_id]

        if original_balance >= bet_amount and 1 <= chosen_number <= 6:
            self.accounts[account_id] += bet_amount 

        final_balance = self.accounts[account_id]
        expected_balance = original_balance + bet_amount
        self.assertEqual(final_balance, expected_balance)

    def test_transactions(self):
        account_id_1 = "account1"
        account_id_2 = "account2"
        initial_balance_1 = 1000
        deposit_amount_1 = 500
        transfer_amount = 300
        initial_balance_2 = 200

        create_account(self.accounts, account_id_1, initial_balance_1)
        deposit(self.accounts, account_id_1, deposit_amount_1)
        create_account(self.accounts, account_id_2, initial_balance_2)
        transfer(self.accounts, account_id_1, account_id_2, transfer_amount)

        final_balance_1 = self.accounts[account_id_1]
        final_balance_2 = self.accounts[account_id_2]

        expected_balance_1 = initial_balance_1 + deposit_amount_1 - transfer_amount
        expected_balance_2 = initial_balance_2 + transfer_amount

        self.assertEqual(final_balance_1, expected_balance_1)
        self.assertEqual(final_balance_2, expected_balance_2)

class TransferTests(unittest.TestCase):
    def setUp(self):
        self.accounts = {}
        create_account(self.accounts, "account1", 1000)
        create_account(self.accounts, "account2", 500)

    def test_transfer_between_existing_accounts(self):
        account_id_1 = "account1"
        account_id_2 = "account2"
        transfer_amount = 300
        result = transfer(self.accounts, account_id_1, account_id_2, transfer_amount)
        expected_balance_1 = 700 
        expected_balance_2 = 800  
        expected_result = f"Transferred {transfer_amount} from account {account_id_1} to account {account_id_2}."
        self.assertEqual(result, expected_result)
        self.assertEqual(self.accounts[account_id_1], expected_balance_1)
        self.assertEqual(self.accounts[account_id_2], expected_balance_2)


    def test_transfer_insufficient_balance(self):
        account_id_1 = "account2"
        account_id_2 = "account1"
        transfer_amount = 600

        result = transfer(self.accounts, account_id_1, account_id_2, transfer_amount)
        expected_result = "Insufficient funds in the source account."
        expected_balance_1 = self.accounts[account_id_1]
        expected_balance_2 = self.accounts[account_id_2]

        self.assertEqual(result, expected_result)
        self.assertEqual(self.accounts[account_id_1], expected_balance_1)
        self.assertEqual(self.accounts[account_id_2], expected_balance_2)

    def test_transfer_to_same_account(self):
        account_id_1 = "account1"
        account_id_2 = "account1"
        transfer_amount = 100

        result = transfer(self.accounts, account_id_1, account_id_2, transfer_amount)
        expected_result = "Cannot transfer to the same account."
        expected_balance_1 = self.accounts[account_id_1]

        self.assertEqual(result, expected_result)
        self.assertEqual(self.accounts[account_id_1], expected_balance_1)

    def test_transfer_from_non_existing_account(self):
        account_id_1 = "account3"
        account_id_2 = "account1"
        transfer_amount = 500

        result = transfer(self.accounts, account_id_1, account_id_2, transfer_amount)
        expected_result = "One or both accounts do not exist."

        self.assertEqual(result, expected_result)

    def test_transfer_to_non_existing_account(self):
        account_id_1 = "account1"
        account_id_2 = "account3"
        transfer_amount = 500

        result = transfer(self.accounts, account_id_1, account_id_2, transfer_amount)
        expected_result = "One or both accounts do not exist."

        self.assertEqual(result, expected_result)

    def test_transfer_negative_amount(self):
        account_id_1 = "account1"
        account_id_2 = "account2"
        transfer_amount = -100

        with self.assertRaises(ValueError):
            transfer(self.accounts, account_id_1, account_id_2, transfer_amount)

    def test_transfer_non_numeric_amount(self):
        account_id_1 = "account1"
        account_id_2 = "account2"
        transfer_amount = "abc"

        with self.assertRaises(TypeError):
            transfer(self.accounts, account_id_1, account_id_2, transfer_amount)

class WithdrawTests(unittest.TestCase):
    def setUp(self):
        self.accounts = {}
        create_account(self.accounts, "account1", 1000)
        create_account(self.accounts, "account2", 500) 

    def test_withdraw_entire_balance(self):
        account_id = "account2"
        withdraw_amount = 500
        result = withdraw(self.accounts, account_id, withdraw_amount)
        expected_balance = 0
        expected_result = f"Withdrew {withdraw_amount} from account {account_id}. New balance is {expected_balance}."
        self.assertEqual(result, expected_result)
        self.assertEqual(self.accounts[account_id], expected_balance)


    def test_withdraw_entire_balance(self):
        account_id = "account2"
        withdraw_amount = 500

        result = withdraw(self.accounts, account_id, withdraw_amount)
        expected_balance = 0
        expected_result = f"Withdrew {withdraw_amount} from account {account_id}. New balance is {expected_balance}."

        self.assertEqual(result, expected_result)
        self.assertEqual(self.accounts[account_id], expected_balance)

    def test_withdraw_from_non_existing_account(self):
        account_id = "account3"
        withdraw_amount = 1000

        result = withdraw(self.accounts, account_id, withdraw_amount)
        expected_result = "Account does not exist."

        self.assertEqual(result, expected_result)

    def test_withdraw_insufficient_balance(self):
        account_id = "account1"
        withdraw_amount = 1500

        result = withdraw(self.accounts, account_id, withdraw_amount)
        expected_result = "Insufficient funds."
        expected_balance = self.accounts[account_id]

        self.assertEqual(result, expected_result)
        self.assertEqual(self.accounts[account_id], expected_balance)

    def test_withdraw_negative_amount(self):
        account_id = "account1"
        withdraw_amount = -500

        with self.assertRaises(ValueError):
            withdraw(self.accounts, account_id, withdraw_amount)

    def test_withdraw_non_numeric_amount(self):
        account_id = "account1"
        withdraw_amount = "abc"

        with self.assertRaises(TypeError):
            withdraw(self.accounts, account_id, withdraw_amount)

if __name__ == '__main__':
    unittest.main() 