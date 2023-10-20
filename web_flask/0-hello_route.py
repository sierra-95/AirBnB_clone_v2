#!/usr/bin/python3
""" Hello world in flask"""


from flask import Flask


app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_world():
    """route index"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
