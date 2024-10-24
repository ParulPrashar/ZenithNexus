from flask import Flask

app = Flask(__name__)

@app.route("/")
def contact_us():
    return "<p>Hello, World!</p>"

@app.route("/")
def login_page():
    return "<p>Hello, World!</p>"
    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)