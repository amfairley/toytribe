from toy_tribe import db
from datetime import datetime


class Users(db.Model):
    """
    Users class model for database.
    Contains id, first_name, last_name, email, password.
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    toys = db.relationship("Toy", backref="users", lazy=True)
    profile = db.relationship(
        "Profile",
        backref="users",
        cascade="all, delete",
        lazy=True
    )
    reviews = db.relationship("Review", backref="users", lazy=True)

    def __repr__(self):
        """
        Returns a string represenation of the Users database schema.
        """
        return (
            f"#{self.id} | first_name: {self.first_name} | "
            f"last_name: {self.last_name} | email: {self.email} | "
            f"password: {self.password}"
        )


class Toy(db.Model):
    """
    Toy class model for database.
    Contains id, user_id, name, company, type, is_approved, image_url,
    date_of_creation.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )
    name = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=True)
    type = db.Column(db.String(50), nullable=True)
    is_approved = db.Column(db.Boolean, default=False, nullable=False)
    image_url = db.Column(db.String(300), nullable=True)
    date_of_creation = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )
    review = db.relationship(
        "Review",
        backref="toy",
        cascade="all, delete",
        lazy=True
    )

    def __repr__(self):
        """
        Returns a string represenation of the Toy database schema.
        """
        return (
            f"#{self.id} | user_id: {self.user_id} | name: {self.name} | "
            f"company: {self.company} | type: {self.type} | "
            f"is_approved: {self.is_approved} | "
            f"date_of_creation: {self.date_of_creation} | "
            f"image_url: {self.image_url}"
        )


class Profile(db.Model):
    """
    Profile class model for database.
    Contains id, user_id, about_me, country, is_parent.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    about_me = db.Column(db.Text, nullable=False)
    # The longest country name in the world has 56 characters:
    # The United Kingdom of Great Britain and Northern Ireland
    country = db.Column(db.String(56), nullable=True)
    is_parent = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the Profile database schema.
        """
        return (
            f"#{self.id} | user_id: {self.user_id} | "
            f"about_me: {self.about_me} | country: {self.country} | "
            f"is_parent: {self.is_parent}"
        )


class Review(db.Model):
    """
    Review class model for database.
    Contains id, user_id, toy_id, review_content, rating, date_of_creation.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )
    toy_id = db.Column(
        db.Integer,
        db.ForeignKey("toy.id", ondelete="CASCADE"),
        nullable=False
    )
    review_content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, primary_key=False, nullable=False)
    date_of_creation = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return (
            f"#{self.id} | user_id: {self.user_id} | toy_id: {self.toy_id} | "
            f"review_content: {self.review_content} | rating: {self.rating} | "
            f"date_of_creation: {self.date_of_creation}"
        )
