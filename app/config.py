import os

''' 
create a Configuration class that has a static variable named SECRET_KEY. 
Then, set it to the value from the environment variable of the same name.
'''

class Configuration:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "postgresql://order_up:9uCxydbt@localhost/order_up_dev"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
