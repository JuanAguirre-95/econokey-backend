from marshmallow import Schema, fields


class NoteSchema(Schema):
    note_name = fields.Str(required=True)
    text = fields.Str(required=True)