from __future__ import annotations

from datetime import datetime


class StatementItemDto:
    id: str
    time: int
    description: str
    mcc: int
    original_mcc: int
    hold: bool
    amount: int
    operation_amount: int
    currency_code: int
    commission_rate: int
    cashback_amount: int
    balance: int
    comment: str | None
    receipt_id: str | None
    invoice_id: str | None
    counter_edrpou: str | None
    counter_iban: str | None
    counter_name: str | None

    def __init__(self, id_: str, time: int, description: str, mcc: int, original_mcc: int, hold: bool, amount: int,
                 operation_amount: int, currency_code: int, commission_rate: int, cashback_amount: int, balance: int,
                 comment: str | None, receipt_id: str | None, invoice_id: str | None, counter_edrpou: str | None,
                 counter_iban: str | None, counter_name: str | None):
        self.id = id_
        self.time = time
        self.description = description
        self.mcc = mcc
        self.original_mcc = original_mcc
        self.hold = hold
        self.amount = amount
        self.operation_amount = operation_amount
        self.currency_code = currency_code
        self.commission_rate = commission_rate
        self.cashback_amount = cashback_amount
        self.balance = balance
        self.comment = comment
        self.receipt_id = receipt_id
        self.invoice_id = invoice_id
        self.counter_edrpou = counter_edrpou
        self.counter_iban = counter_iban
        self.counter_name = counter_name

    @staticmethod
    def from_json(data: dict) -> StatementItemDto:
        return StatementItemDto(
            id_=data['id'],
            time=data['time'],
            description=data['description'],
            mcc=data['mcc'],
            original_mcc=data['originalMcc'],
            hold=data['hold'],
            amount=data['amount'],
            operation_amount=data['operationAmount'],
            currency_code=data['currencyCode'],
            commission_rate=data['commissionRate'],
            cashback_amount=data['cashbackAmount'],
            balance=data['balance'],
            comment=data.get('comment', None),
            receipt_id=data.get('receiptId', None),
            invoice_id=data.get('invoiceId', None),
            counter_edrpou=data.get('counterEdrpou', None),
            counter_iban=data.get('counterIban', None),
            counter_name=data.get('counterName', None),
        )

    @property
    def float_balance(self) -> float:
        return self.balance / 100

    @property
    def float_commission_rate(self) -> float:
        return self.commission_rate / 100

    @property
    def float_cashback_amount(self) -> float:
        return self.cashback_amount / 100

    @property
    def float_amount(self) -> float:
        return self.amount / 100

    @property
    def float_operation_amount(self) -> float:
        return self.operation_amount / 100

    @property
    def datetime(self) -> datetime:
        return datetime.fromtimestamp(self.time)

    def __repr__(self):
        return (f'<StatementItemDto(id={self.id}, time={self.datetime}, '
                f'description={self.description}, amount={self.float_amount})>')


"""
id
string
Унікальний id транзакції

time
number <int64>
Час транзакції в секундах в форматі Unix time

description
string
Опис транзакцій

mcc
number <int32>
Код типу транзакції (Merchant Category Code), відповідно ISO 18245

originalMcc
number <int32>
Оригінальний код типу транзакції (Merchant Category Code), відповідно ISO 18245

hold
boolean
Статус блокування суми (детальніше у wiki)

amount
number <int64>
Сума у валюті рахунку в мінімальних одиницях валюти (копійках, центах)

operationAmount
number <int64>
Сума у валюті транзакції в мінімальних одиницях валюти (копійках, центах)

currencyCode
number <int32>
Код валюти рахунку відповідно ISO 4217

commissionRate
number <int64>
Розмір комісії в мінімальних одиницях валюти (копійках, центах)

cashbackAmount
number <int64>
Розмір кешбеку в мінімальних одиницях валюти (копійках, центах)

balance
number <int64>
Баланс рахунку в мінімальних одиницях валюти (копійках, центах)

comment
string
Коментар до переказу, уведений користувачем. Якщо не вказаний, поле буде відсутнім

receiptId
string
Номер квитанції для check.gov.ua. Поле може бути відсутнім

invoiceId
string
Номер квитанції ФОПа, приходить у випадку якщо це операція із зарахуванням коштів

counterEdrpou
string
ЄДРПОУ контрагента, присутній лише для елементів виписки рахунків ФОП

counterIban
string
IBAN контрагента, присутній лише для елементів виписки рахунків ФОП

counterName
string
Найменування контрагента
"""
