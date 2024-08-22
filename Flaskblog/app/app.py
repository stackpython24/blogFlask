from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from config import Config
from posts.blueprint import posts

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(posts, url_prefix='/blog')

db = SQLAlchemy(app)