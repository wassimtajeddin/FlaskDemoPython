from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world!"
@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/contact")
def contact():
    return "Du kan kontakta mig på 0736842961"

@app.route ("/about")
def about():
    return "En engagerad Java-utvecklare med en stark drivkraft att ständigt lära sig och utvecklas."

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)