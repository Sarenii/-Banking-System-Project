import unittest
from src.banking_system import deposit, withdraw

class TestBankingSystem(unittest.TestCase):

    def test_deposit_positive_amount(self):
        """Test depositing a positive amount."""
        balance = 1000
        new_balance = deposit(balance, 500)
        self.assertEqual(new_balance, 1500)

    def test_deposit_negative_amount(self):
        """Test depositing a negative amount (should not change balance)."""
        balance = 1000
        new_balance = deposit(balance, -200)
        self.assertEqual(new_balance, 1000)

    def test_withdraw_valid_amount(self):
        """Test withdrawing a valid amount within balance."""
        balance = 1000
        new_balance = withdraw(balance, 300)
        self.assertEqual(new_balance, 700)

    def test_withdraw_exceeding_balance(self):
        """Test withdrawing an amount exceeding the balance (should not change balance)."""
        balance = 1000
        new_balance = withdraw(balance, 1500)
        self.assertEqual(new_balance, 1000)

    def test_withdraw_negative_amount(self):
        """Test withdrawing a negative amount (should not change balance)."""
        balance = 1000
        new_balance = withdraw(balance, -100)
        self.assertEqual(new_balance, 1000)

if __name__ == "__main__":
    unittest.main()
