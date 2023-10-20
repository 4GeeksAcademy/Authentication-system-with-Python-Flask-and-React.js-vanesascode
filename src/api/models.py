from flask_sqlalchemy import SQLAlchemy 
# from SQLAlchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    __tablename__= "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        # return '<User %r>' % self.id
        return f'<User {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
            "name": self.name, 
        }
    
class Favs(db.Model):
    __tablename__= "favs"
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(80))
    pet = db.Column(db.String(80))
    meal = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user_id_relationship = db.relationship(User)


    def __repr__(self):
        # return '<Favs %r>' % self.id
        return f'<Favs {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "color": self.color,
            "pet" : self.pet,
            "meal": self.meal, 
            "user_id": self.user_id,
        }
