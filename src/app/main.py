import time
from fastapi import FastAPI, HTTPException
from mangum import Mangum

from src.app.errors.controller_errors import ForbiddenAction
from src.app.repo.transaction_repository_interface import ITransactionRepository

from .environments import Environments

from .repo.account_repository_interface import IAccountRepository

from .errors.entity_errors import ParamNotValidated

from .enums.transactions_type_enum import TransationsType

from .entities.account import Account


app = FastAPI()

account_repo: IAccountRepository = Environments.get_account_repo()() 
transaction_repo: ITransactionRepository = Environments.get_transaction_repo()()

@app.get("/")
def get_account():
    account = account_repo.get_account(1)
    return account.to_dict()

@app.post("/deposit")
def post_deposit(request: dict):
    total = 0

    for (bill, qty) in request.items(): total += int(bill) * qty

    total = float(total)

    account = account_repo.get_account(1)
    account = account_repo.make_deposit(account, total)
    transaction = transaction_repo.create_transaction(TransationsType.DEPOSIT, total, time.time(),account.current_balance)

    return {
        "current_balance": transaction.curr_balance,
        "timestamp": transaction.timestamp
    }

@app.post("/withdraw")
def post_withdraw(request: dict):
    total = 0

    for (bill, qty) in request.items(): total += int(bill) * qty

    account = account_repo.get_account(1)
    
    if account.current_balance < total: raise HTTPException(403, "Saldo insuficiente")

    total = float(total)

    account = account_repo.make_withdraw(account, total)
    transaction = transaction_repo.create_transaction(TransationsType.WITHDRAW, total, time.time(), account.current_balance)

    return {
        "current_balance": transaction.curr_balance,
        "timestamp": transaction.timestamp
    }

@app.post("/history")
def get_transactions():
    return transaction_repo.get_all_transactions()


handler = Mangum(app, lifespan="off")
