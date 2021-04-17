# Module 9.4.3 - setting up Flask routes
# import required modules
from flask import Flask

# Create a new Flask instance
app = Flask(__name__)

# Create routes

# Root route
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/alan')
def hello_alan():
    return 'Hello World - love Alan'

