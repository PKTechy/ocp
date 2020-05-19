import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome! 1111111"

@app.route('/how are you')
def hello():
    return 'I am good, how about you? 1111111111111'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
