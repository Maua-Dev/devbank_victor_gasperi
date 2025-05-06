from abc import ABC, abstractmethod
from typing import Optional

from src.app.entities.account import Account
from src.app.entities.transaction import Transaction


class IAccountRepository(ABC):

    @abstractmethod
    def get_account(self, account_id: int) -> Optional[Account]:
        '''
        Returns the account with the given id.
        '''
        pass

    @abstractmethod
    def update_current_balance(self, account: Account, transaction: Transaction) -> Optional[Account]:
        '''
        Updates the account current balance, given the Account and the Transaction
        ''' 
        pass