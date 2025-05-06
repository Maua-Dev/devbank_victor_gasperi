from typing import Dict
from src.app.entities.account import Account
from src.app.enums.transactions_type_enum import TransationsType
from src.app.repo.account_repository_interface import IAccountRepository


class AccountRepositoryMock(IAccountRepository):
    accounts: Dict[int, Account]

    def __init__(self):
        self.accounts = {
            1: Account(name="Victor Gasperi", agency="1111", account_number="11111-1", current_balance=1000.0)
        }

    def get_account(self, account_id):
        return self.accounts.get(account_id, None)
    
    def update_current_balance(self, account, transaction):

        if account is not None:

            match transaction.transaction_type:

                case TransationsType.DEPOSIT:
                    account.current_balance += transaction.value

                case TransationsType.WITHDRAW:
                    account.current_balance -= transaction.value

        return account
    
    
