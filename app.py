from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world!"

@app.route("/contact")
def contact():
    return "Du kan kontakta mig på 0736842961"

if __name__ == "__main__":
    app.run(debug=True)