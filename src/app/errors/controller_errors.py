from src.app.errors.base_error import BaseError


class ForbiddenAction(BaseError): 
    def __init__(self, message):
        super().__init__(message)