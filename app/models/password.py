from marshmallow import Schema, fields


class PasswordSchema(Schema):
    password_name = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    url = fields.Url(required=False)


