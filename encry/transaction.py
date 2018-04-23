from . import serialization


class Script(serialization.JsonSerializable):
    def __init__(self, serialized_script, complexity_score, script_fingerprint):
        self.serialized_script = serialized_script
        self.complexity_score = complexity_score
        self.script_fingerprint = script_fingerprint

    def json(self):
        pass


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


class AssetIssuingDirective(Directive):
    def __init__(self, script, amount, idx, symbol):
        self.script = script
        self.amount = amount
        self.idx = idx
        self.symbol = symbol

    def json(self):
        pass


class Transaction(serialization.JsonSerializable):
    def __init__(self, account_pk, fee, timestamp, unlockers, directives, signature=None):
        self.account_pk = account_pk
        self.fee = fee
        self.timestamp = timestamp
        self.unlockers = unlockers
        self.directives = directives
        self.signature = signature

    def json(self):
        pass

    def message_to_sign(self):
        pass
