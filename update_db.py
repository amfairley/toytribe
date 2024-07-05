from toy_tribe import db, app
with app.app_context():
    db.create_all()