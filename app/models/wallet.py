from marshmallow import Schema, fields


class WalletSchema(Schema):
    wallet_name = fields.Str(required=True)
    token = fields.Str(required=True)
    wallet_address = fields.Str(required=True)
    wallet_key = fields.Str(required=True)
    wallet_passphrase = fields.Str(required=False)