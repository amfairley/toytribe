from toy_tribe import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(200), unique = True, nullable = False)
    password = db.Column(db.String(), nullable = False)
    toys = db.relationship("Toy", backref="users", lazy = True)
    profile = db.relationship("Profile", backref = "users", cascade = "all, delete", lazy = True)
    reviews = db.relationship("Review", backref = "users", lazy = True )
    
    def __repr__(self):
        return "#{0} - first_name: {1} | last_name: {2} | email: {3} | password: {4}".format(
            self.id, self.first_name, self.last_name, self.email, self.password
        )


class Toy(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"), nullable = True)
    name = db.Column(db.String(200), nullable = False)
    company = db.Column(db.String(200), nullable = True)
    type = db.Column(db.String(50), nullable = True)
    is_approved = db.Column(db.Boolean, default = False, nullable = False)
    date_of_creation = db.Column(db.Date, nullable = False)
    image_url = db.Column(db.String(300), nullable = False)
    review = db.relationship("Review", backref = "toy", cascade = "all, delete", lazy = True)


    def __repr__(self):
        return "#{0} - user_id: {1} | name: {2} | company: {3} | type: {4} | is_approved: {5}| date_of_creation: {5} | image_url: {6}".format(
            self.id, self.user_id, self.name, self.company, self.type, self.is_approved, self.date_of_creation, self.image_url
        )
    

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)
    about_me = db.Column(db.Text, nullable = False)
    # The longest country name in the world has 56 characters: The United Kingdom of Great Britain and Northern Ireland
    country = db.Column(db.String(56), nullable = True)
    is_parent = db.Column(db.Boolean, default = False, nullable = False)

    def __repr__(self):
        return "#{0} - user_id: {1} | about_me: {3} | country: {4} | is_parent: {5}".format(
            self.id, self.user_id, self.about_me, self.country, self.is_parent
        )   

class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"), nullable = True)
    toy_id = db.Column(db.Integer, db.ForeignKey("toy.id", ondelete="CASCADE"), nullable = False)
    review_content = db.Column(db.Text, nullable = False)
    rating = db.Column(db.Integer, primary_key = False, nullable = False)
    date_of_creation = db.Column(db.Date, nullable = False)
    def __repr__(self):
        return "#{0} - user_id: {1} | toy_id: {2} | review_content: {3} | rating: {4} | date_of_creation: {5}".format(
            self.id, self.user_id, self.toy_id, self.review_content, self.rating, self.date_of_creation
        )