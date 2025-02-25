from flask import Flask
from .views import book_api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_api)
    return app
