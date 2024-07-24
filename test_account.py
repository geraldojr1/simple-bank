import unittest
from account import Account
from account import Conta1

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(initial_balance=100)
    
    def test_withdraw_success(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)
    
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150)
    
    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

    def test_deposito_valor_negativo(self):
        with self.assertRaises(ValueError):
            self.account.deposito(-10)

    def test_deposito_success(self):
        self.account.deposito(50)
        self.assertEqual(self.account.balance, 50)       

  
             


if __name__ == '__main__':
    unittest.main()
