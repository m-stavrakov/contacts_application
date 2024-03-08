from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # nullable means it has to have a value it cannot be empty
    # unique is if there can be 2 or more of the same value, like names can have 2 Toms but emails have to be unique
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    # getting all the data from each column and transform them to Python dictionary
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }
