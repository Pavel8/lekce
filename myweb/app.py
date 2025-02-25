from flask import Flask, render_template
from fake_db import users


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("pages/home.html")

@app.route('/strana2')
def page2():
    return render_template("pages/strana2.html")

@app.route('/strana3')
def page3():
    return render_template("pages/strana3.html")

@app.route('/users_list')
def users_list():
    return render_template("pages/users_list.html", users=users)

@app.route('/profile')
def fake_profile():
    user = {
        "name": "John",
        "age": 23
    }
    return render_template("pages/fake_profile.html", **user)

@app.route('/profile/<int:id>')
def profile(id):
    # pozadam z db o konkretneho uzivatela
    return render_template("pages/profile.html", **users[id - 1])

if __name__ == "__main__":
    app.run(debug=True)