from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world!"

@app.route("/contact")
def contact():
    return "Du kan kontakta mig på 0736842961"

@app.reoute ("/about")
def about():
    return "En engagerad Java-utvecklare med en stark drivkraft att ständigt lära sig och utvecklas."

if __name__ == "__main__":
    app.run(debug=True)