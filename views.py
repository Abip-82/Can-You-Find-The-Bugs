from flask import Blueprint , render_template , request , url_for , session , redirect
from data import users

views = Blueprint("views" , __name__)

@views.route("/" , methods=["GET","POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()
        user =  users.get(username)
        if user and user["password"] == password:
            session["username"] = username
            return redirect(url_for("views.profile"))
        error = "Invalid username or password"
        return render_template("base.html", error=error)
    return render_template("base.html")

@views.route("/profile")
def profile():
    username = session.get("username")
    return username
