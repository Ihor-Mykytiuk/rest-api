from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.models import books
from app.schemas import BookSchema

book_api = Blueprint('book_api', __name__, url_prefix='/api/v1')


def find_book_by_id(book_id):
    book = next((book for book in books if book.id == book_id), None)
    return book


@book_api.get('/books')
def get_books():
    return jsonify(books), 200


@book_api.get('/books/<string:book_id>')
def get_book(book_id):
    book = find_book_by_id(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify(book), 200


@book_api.post('/books')
def add_book():
    data = request.get_json()
    try:
        book = BookSchema().load(data)
    except ValidationError as e:
        return jsonify({'message': e.messages}), 400
    books.append(book)
    return jsonify(book), 201


@book_api.delete('/books/<string:book_id>')
def delete_book(book_id):
    book = find_book_by_id(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    books.remove(book)
    return '', 204
