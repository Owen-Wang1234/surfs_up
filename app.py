# Import Flask
from flask import Flask

# Create a new Flask instance
app = Flask(__name__)

# Define the root
@app.route('/')
def hello_world():
    return 'Hello world'

# Set up another route
@app.route('/home')
def intro():
    return 'This is my first Flask'