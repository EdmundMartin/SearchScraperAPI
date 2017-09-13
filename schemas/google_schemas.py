from marshmallow import Schema, fields


class GoogleSingleItem(Schema):
    keyword = fields.String(required=True)
    geo = fields.String(required=False)
    proxy = fields.String(required=False)
    number = fields.Int(required=False)
