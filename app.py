from errno import EFAULT
from flask import Flask
from logging.handlers import RotatingFileHandler
import logging
from flask.logging import default_handler
import os

app = Flask(__name__)

# Configure the flask application
config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
app.config.from_object(config_type)

# Secret key for cookie sessions.
# Secret value generated using python secrets module - secrets.token_bytes(32)
# app.secret_key = b'\x80\t\xb3Y\x94Q\xb1\xab\\Q\x89\xd3\xd4\xddAV\xbf\x02\xe30\x0c\xa2)\x01\xac\x0b\x1b\xc6\xc0H\xb0*';

# Logging Configuration
# Remove the default logger configured by Flask
app.logger.removeHandler(default_handler)

# Creating FileHandler logger, creating new handler
file_handler = RotatingFileHandler('instance/flask-stock-portfolio.log',
                                   maxBytes=16384,
                                   backupCount=20)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
# Setting logger level
file_handler.setLevel(logging.INFO) 
app.logger.addHandler(file_handler)

# Logging that the application is starting 
app.logger.info('Starting the Flask application...')

# Import the blueprints
from project.stocks import stocks_blueprint
from project.users import users_blueprint

# Registering the blueprints
app.register_blueprint(stocks_blueprint)
app.register_blueprint(users_blueprint, url_prefix='/users')

# @app.route('/blog_posts/<int:post_id>')
# def display_blog_post(post_id):
#     return f'<h1>Blog Post #{post_id}...</h1>'