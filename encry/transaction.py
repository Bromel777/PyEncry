from . import serialization


class Directive(serialization.JsonSerializable):
    """Base class for directives"""


class TransferDirective(Directive):
    def __init__(self, address, amount, idx, token_id=None):
        self.address = address
        self.amount = amount
        self.idx = idx
        self.token_id = token_id

    def json(self):
        pass


class Transaction(serialization.JsonSerializable):
    def __init__(self, account_pk, fee, timestamp, signature, unlockers, directives):
        self.account_pk = account_pk
        self.fee = fee
        self.timestamp = timestamp
        self.signature = signature
        self.unlockers = unlockers
        self.directives = directives

    def json(self):
        pass

    def message_to_sign(self):
        pass
