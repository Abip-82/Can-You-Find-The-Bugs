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
            session["uid"] = user["uid"]
            session["role"] = user["role"]
            return redirect(url_for("views.profile"))
        error = "Invalid username or password"
        return render_template("base.html", error=error)
    return render_template("base.html")

@views.route("/profile")
def profile():
    username = session.get("username")
    if not username:
        error="You are not logged in yet"
        return render_template("base.html",error=error)
    return render_template("profile.html" , username=username)

@views.route("/logout")
def logout():
    username = session.get("username")
    session.clear()
    return render_template("base.html")

@views.route("/assignments")
def assignments():
    username = session.get("username")
    if not username:
        error="You are not logged in yet"
        return render_template("base.html",error=error)
    return render_template("assignments.html")

@views.route("/courses")
def courses():
    username=session.get("username")
    if not username:
        error="You are not logged in yet"
        return render_template("base.html",error=error)
    return render_template("courses.html")

@views.route("/settings")
def settings():
    username=session.get("username")
    uid = session.get("uid")
    role = session.get("role")
    if not username:
        error="You are not logged in yet"
        return render_template("base.html",error= error)
    return render_template("settings.html", uid=uid , role=role, username=username)