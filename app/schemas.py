from marshmallow import Schema, fields, validates, ValidationError, post_load
from app.models import Book

class BookSchema(Schema):
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    published_year = fields.Int(required=True)

    @validates('published_year')
    def validate_year(self, value):
        if value < 1000 or value > 2100:
            raise ValidationError("Published year must be between 1000 and 2100.")

    @post_load
    def make_book(self, data, **kwargs):
        return Book(**data)
