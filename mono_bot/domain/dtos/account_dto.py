from __future__ import annotations


class AccountDto:
    id: str
    send_id: str
    balance: int
    credit_limit: int
    type: str
    currency_code: int
    cashback_type: str | None
    masked_pan: list[str]
    iban: str

    def __init__(self, id_: str, send_id: str, balance: int, credit_limit: int, type_: str, currency_code: int,
                 cashback_type: str | None, masked_pan: list[str], iban: str):
        self.id = id_
        self.send_id = send_id
        self.balance = balance
        self.credit_limit = credit_limit
        self.type = type_
        self.currency_code = currency_code
        self.cashback_type = cashback_type
        self.masked_pan = masked_pan
        self.iban = iban

    @staticmethod
    def from_json(data: dict) -> 'AccountDto':
        return AccountDto(
            id_=data['id'],
            send_id=data['sendId'],
            balance=data['balance'],
            credit_limit=data['creditLimit'],
            type_=data['type'],
            currency_code=data['currencyCode'],
            cashback_type=data.get('cashbackType', None),
            masked_pan=data['maskedPan'],
            iban=data['iban']
        )

    def __repr__(self):
        return f'<AccountDto: {self.masked_pan} ({self.float_balance})>'

    @property
    def float_balance(self):
        return self.balance / 100

    @property
    def float_credit_limit(self):
        return self.credit_limit / 100
