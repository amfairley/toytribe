import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from toy_tribe import routes

# Import events and Review model to ensure event listeners work
from .models import event
from .models import Review

# Register event listeners
event.listen(Review, 'after_insert', Review.after_insert)
event.listen(Review, 'after_update', Review.after_update)
event.listen(Review, 'after_delete', Review.after_delete)
