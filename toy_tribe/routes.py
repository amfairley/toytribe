from flask import render_template
from toy_tribe import app, db
from toy_tribe.models import User, Toy, Profile, Review


@app.route("/")
def home():
    return render_template("base.html")