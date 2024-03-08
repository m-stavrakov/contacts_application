from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# last one removes any CORS errors that can occur 

app = Flask(__name__)
CORS(app)

# specifying the location of the local sql db on out device
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

# not tracking all the modifications that are made in the db
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# creating an instance of the db
db = SQLAlchemy(app)
