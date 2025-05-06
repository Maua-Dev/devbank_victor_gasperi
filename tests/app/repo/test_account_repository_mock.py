import time
from src.app.entities.transaction import Transaction
from src.app.enums.transactions_type_enum import TransationsType
from src.app.repo.account_repository_mock import AccountRepositoryMock


class Test_AccountRepositoryMock:

    def test_get_account(self):

        repo = AccountRepositoryMock()
        account = repo.get_account(account_id=1)
        assert account == repo.accounts.get(1)

    def test_get_account_not_found(self):

        repo = AccountRepositoryMock()
        account = repo.get_account(account_id=10)
        assert account is None

    def test_update_current_balance_deposit(self):

        repo = AccountRepositoryMock()
        curr_timestamp = time.time()
        account = repo.get_account(account_id=1)
        transaction = Transaction(transaction_type=TransationsType.DEPOSIT, value=100.0, timestamp=curr_timestamp)
        response = repo.update_current_balance(account, transaction)
        expected = {
            "name": "Victor Gasperi",
            "agency": "1111",
            "account": "11111-1",
            "current_balance": 1100.0
        }

        assert response.to_dict() == expected
        
    def test_update_current_balance_withdraw(self):

        repo = AccountRepositoryMock()
        curr_timestamp = time.time()
        account = repo.get_account(account_id=1)
        transaction = Transaction(transaction_type=TransationsType.WITHDRAW, value=100.0, timestamp=curr_timestamp)
        response = repo.update_current_balance(account, transaction)
        expected = {
            "name": "Victor Gasperi",
            "agency": "1111",
            "account": "11111-1",
            "current_balance": 900.0
        }

        assert response.to_dict() == expected


