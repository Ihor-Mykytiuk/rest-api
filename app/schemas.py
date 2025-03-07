from marshmallow import Schema, fields, validates, ValidationError, post_load, validate
from app.models import Book
from datetime import datetime

MIN_YEAR = 1000
MAX_YEAR = datetime.now().year


class BookSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    author = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    published_year = fields.Int(required=True)

    @validates('published_year')
    def validate_year(self, value):
        if value < MIN_YEAR or value > MAX_YEAR:
            raise ValidationError(f"Published year must be between {MIN_YEAR} and {MAX_YEAR}.")

    @post_load
    def make_book(self, data, **kwargs):
        return Book(**data)
