from abc import ABC, abstractmethod
from typing import List, Optional

from src.app.entities.account import Account
from src.app.entities.transaction import Transaction
from src.app.enums.transactions_type_enum import TransationsType


class ITransactionRepository(ABC):

    @abstractmethod
    def get_all_transactions(self) -> Optional[List[Transaction]]:
        '''
        Returns all the transactions
        '''
        pass

    @abstractmethod
    def create_transaction(self, transaction_type: TransationsType, transaction_value: float, curr_balance: float) -> Optional[Transaction]:
        '''
        Creates a new transaction, given its type and value
        '''
        pass