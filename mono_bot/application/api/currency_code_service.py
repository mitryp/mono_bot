_CODES_TO_CURRENCY = {
    980: ('UAH', '₴'),
    840: ('USD', '$'),
    978: ('EUR', '€'),
    826: ('EUR', '£'),
}


class CurrencyCodeService:
    def represent_currency(self, currency_code: int) -> str:
        _repr = _CODES_TO_CURRENCY.get(currency_code, None)

        return _repr[0] if _repr else 'unknown currency'
