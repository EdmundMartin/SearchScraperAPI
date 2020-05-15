from marshmallow import Schema, fields


class ScrapeItem(Schema):
    keyword = fields.String(required=True)
    number = fields.Int(required=True)
    domain = fields.String(required=False)
    proxy = fields.String(required=False)
    language = fields.String(required=False)
