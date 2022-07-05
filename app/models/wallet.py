from dataclasses import field
from marshmallow import Schema, fields


class WalletSchema(Schema):
    wallet_name = fields.Str(required=True)
    cryptocurrency = fields.Str(required=True)
    public_key = fields.Str(required=True)
    private_key = fields.Str(required=True)
    passphrase = fields.Str(required=False)
    icon = fields.Str(required=True)
    description = fields.Str(required=False)
    notes = fields.Str(required=False)
