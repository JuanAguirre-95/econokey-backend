from marshmallow import Schema, fields


class PasswordSchema(Schema):
    password_name = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    url = fields.Str(required=False)
    description = fields.Str(required=False)
    notes = fields.Str(required=False)
    icon = fields.Str(required=False)


