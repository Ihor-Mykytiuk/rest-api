from flask import Blueprint, request, jsonify


book_api = Blueprint('book_api', __name__, url_prefix='/api/v1')

@book_api.route('/books', methods=['GET'])
def get_books():
    pass