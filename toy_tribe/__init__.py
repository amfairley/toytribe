import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env

# Create db object without app
db = SQLAlchemy()


# Create app function
def create_app():
    # Create an instance of the Flask object
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    # Select the database based on development status
    if os.environ.get("DEVELOPMENT") == "True":
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
    else:
        uri = os.environ.get("DATABASE_URL")
        if uri.startswith("postgres://"):
            uri = uri.replace("postgres://", "postgresql://", 1)
        # This is the database connection showing Flask where to connect
        app.config["SQLALCHEMY_DATABASE_URI"] = uri
        # Enforces ssl connection for heroku
        app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
            "connect_args": {"sslmode": "require"}
        }

    # Define my database
    db.init_app(app)

    with app.app_context():
        from toy_tribe import routes

    return app
