from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.schema import Column, ForeignKey, Table
from sqlalchemy.types import Integer, String


db = SQLAlchemy()

''' 
create an Employee class that inherits from db.Model AND the UserMixin class from flask_login.
'''

class Employee(db.Model, UserMixin):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    employee_number = Column(Integer, nullable=False, unique=True)
    hashed_password = Column(String(100), nullable=False)

    #lines 21 - 30 are methods to handle password management
    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
