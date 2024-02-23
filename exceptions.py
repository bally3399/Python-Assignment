class InvalidAmountException(Exception):
    """Exception raised for invalid deposit/withdrawal amounts."""

    def __init__(self, message="Invalid amount. Amount must be positive."):
        self.message = message
        super().__init__(self.message)


class InsufficientFundsException(Exception):
    """Exception raised for insufficient funds during a withdrawal."""

    def __init__(self, message="Insufficient funds."):
        self.message = message
        super().__init__(self.message)


class InvalidPinException(Exception):
    """Exception raised for invalid pin"""

    def __init__(self, message="Invalid pin. Incorrect PIN"):
        self.message = message
        super().__init__(self.message)


class AccountNotFoundException(Exception):
    """Exception raised for account not found"""

    def __init__(self, message="Account not found."):
        self.message = message
        super().__init__(self.message)


