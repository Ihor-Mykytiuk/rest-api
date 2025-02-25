from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.models import Book, books
from app.schemas import BookSchema


book_api = Blueprint('book_api', __name__, url_prefix='/api/v1')

@book_api.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@book_api.post('/books')
def add_book():
    data = request.get_json()
    try:
        book = BookSchema().load(data)
    except ValidationError as e:
        return jsonify({'message': e.messages}), 400
    books.append(book)
    return jsonify(book), 201
ч