from mono_bot.domain.dtos.statement_item_dto import StatementItemDto


class WebhookDto:
    type: str
    account_id: str
    statement_item: StatementItemDto

    def __init__(self, type_: str, account_id: str, statement_item: StatementItemDto):
        self.type = type_
        self.account_id = account_id
        self.statement_item = statement_item

    @staticmethod
    def from_json(data: dict) -> 'WebhookDto':
        inner_data = data['data']

        return WebhookDto(
            type_=data['type'],
            account_id=inner_data['account'],
            statement_item=StatementItemDto.from_json(inner_data['statementItem']),
        )

    def __repr__(self):
        return f'<Webhook type={self.type} account_id={self.account_id} item=\n\t{self.statement_item}\n>'
