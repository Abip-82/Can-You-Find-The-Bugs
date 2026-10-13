from flask import Blueprint , render_template , request
from data import users

views = Blueprint("views" , __name__)

@views.route("/" , methods=["GET","POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()
        user =  users[username]
        if user and user[password] == password:
            redirect(views.profile)
        error = "Invalid username or password"
        return render_template("base.html", error=error)
    return render_template("base.html")