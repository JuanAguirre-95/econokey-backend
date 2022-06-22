from marshmallow import Schema, fields


class WalletSchema(Schema):
    wallet_name = fields.Str(required=True)
    cryptocurrency = fields.Str(required=True)
    public_key = fields.Str(required=True)
    private_key = fields.Str(required=True)
    passphrase = fields.Str(required=False)