from toy_tribe import db
from datetime import datetime
from sqlalchemy import event


class Users(db.Model):
    """
    Users class model for database.
    Contains id, first_name, last_name, email, password.
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False, index=True)
    # Password length of 255 covers most hashed passwords
    password = db.Column(db.String(255), nullable=False)
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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )
    toy_type_id = db.Column(
        db.Integer,
        db.ForeignKey("toytype.id", ondelete="SET NULL"),
        nullable=True
    )
    name = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=True)
    is_approved = db.Column(db.Boolean, default=True, nullable=False)
    image_url = db.Column(
        db.String(300),
        nullable=False)
    description = db.Column(
        db.Text(),
        nullable=False
    )
    link = db.Column(db.String(300), nullable=True)
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

    def average_rating(self):
        """
        Function to get the average rating for the toy from the reviews.
        """
        # Get all reviews for the toy by the toy_id
        reviews = Review.query.filter_by(toy_id=self.id).all()
        # If there are no reviews, return 0
        if not reviews:
            return 0
        # Calculate the average rating
        total_rating = sum(review.rating for review in reviews)
        return total_rating / len(reviews)

    def __repr__(self):
        """
        Returns a string represenation of the Toy database schema.
        """
        return (
            f"#{self.id} | user_id: {self.user_id} | "
            f"toy_type_id: {self.toy_type_id} | name: {self.name} | "
            f"company: {self.company} | is_approved: {self.is_approved} | "
            f"image_url: {self.image_url} | description: {self.description} | "
            f"link: {self.link} date_of_creation: {self.date_of_creation} | "
            f"average_rating: {self.average_rating:.2f}"
        )


class ToyType(db.Model):
    """
    Toy type model for database.
    Contains id, toy_type.
    """
    __tablename__ = 'toytype'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    toy_type = db.Column(db.String(100), nullable=False)
    toys = db.relationship("Toy", backref="toytype", lazy=True)

    def __repr__(self):
        """
        Returns a string represenation of the Toy Type database schema.
        """
        return f"#{self.id} | toy_type: {self.toy_type}"


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
    about_me = db.Column(
        db.Text,
        default="Hi, I'm yet to fill this out!",
        nullable=False)
    # The longest country name in the world has 56 characters:
    # The United Kingdom of Great Britain and Northern Ireland
    country = db.Column(db.String(56), nullable=True)
    is_parent = db.Column(db.Boolean, default=False, nullable=False)
    user_image = db.Column(
        db.String(300),
        default='toy_tribe/static/img/default_profile.webp',
        nullable=False
    )

    def __repr__(self):
        """
        Returns a string representation of the Profile database schema.
        """
        return (
            f"#{self.id} | user_id: {self.user_id} | "
            f"about_me: {self.about_me} | country: {self.country} | "
            f"is_parent: {self.is_parent} | user_image: {self.user_image}"
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
    date_of_creation = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    def __repr__(self):
        return (
            f"#{self.id} | user_id: {self.user_id} | toy_id: {self.toy_id} | "
            f"review_content: {self.review_content} | rating: {self.rating} | "
            f"date_of_creation: {self.date_of_creation}"
        )

    # Methods to update the average toy rating when changes are made
    @staticmethod
    def after_insert(mapper, connection, target):
        target.toy.update_average_rating()

    @staticmethod
    def after_update(mapper, connection, target):
        target.toy.update_average_rating()

    @staticmethod
    def after_delete(mapper, connection, target):
        target.toy.update_average_rating()


# Event listeners for updating average ratings
event.listen(Review, 'after_insert', Review.after_insert)
event.listen(Review, 'after_update', Review.after_update)
event.listen(Review, 'after_delete', Review.after_delete)
