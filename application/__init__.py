import os

from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://fvuwwviyopzxuu:bc06aff70941d844699191d8c0d55a7dc59a09704e25be5f47c5bf5e97b7de2e@ec2-52-207-25-133.compute-1.amazonaws.com:5432/dtchjmlogbfd7'
app.config['SECRET_KEY'] = '72a3e1afe050a6832ca13e17237dcb21'

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from application import routes
