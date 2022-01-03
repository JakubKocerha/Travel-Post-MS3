import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
# wires base.html up with home.html
@app.route("/home")
def home():
    return render_template('home.html')

# gets data from MongoDB; code from CI tutorials
@app.route("/get_posts")
def get_posts():
    posts = list(mongo.db.posts.find())
    return render_template("posts.html", posts=posts)

# adds register functionality; code from CI turorials
# excluding password confirmation validation
@app.route("/register", methods=["GET", "POST"])
def register():
    password = request.form.get("password")
    password_confirmation = request.form.get("password_confirmation")
    # checks for matching passwords
    if password != password_confirmation:
        flash("Oops! Your passwords don't match. Try again.")
        return redirect(url_for("register"))

    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("This username is used! Please, choose a different one.")
            return redirect(url_for("register"))

        login = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get(
                "password_confirmation"))
        }
        mongo.db.users.insert_one(login)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# adds register functionality; code from CI turorials
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        user_account = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_account:
            # ensure hashed password matches user input
            if check_password_hash(
                    user_account["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}!".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# adds profile functionality; code from CI turorials
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# adds log out functionality; code from CI turorials
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# adds posts' functionality; code from CI turorials
@app.route("/add_post", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        post = {
            "category_name": request.form.get("category_name"),
            "title_text": request.form.get("title_text"),
            "summary": request.form.get("summary"),
            "post_body": request.form.get("post_body"),
            "image_link": request.form.get("image_link"),
            "image_title": request.form.get("image_title"),
            "date_post": request.form.get("date_post"),
            "posted_by": session["user"],
            "email": request.form.get("email")
        }
        mongo.db.posts.insert_one(post)
        flash("Your post was successfully added")
        return redirect(url_for("get_posts"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_post.html", categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
