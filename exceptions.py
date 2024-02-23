class InvalidAmountException(Exception):

    def __init__(self, message="Invalid amount. Amount must be positive."):
        self.message = message
        super().__init__(self.message)


class InsufficientFundsException(Exception):
    
    def __init__(self, message="Insufficient funds."):
        self.message = message
        super().__init__(self.message)


class InvalidPinException(Exception):

    def __init__(self, message="Invalid pin. Incorrect PIN"):
        self.message = message
        super().__init__(self.message)


class AccountNotFoundException(Exception):

    def __init__(self, message="Account not found."):
        self.message = message
        super().__init__(self.message)


