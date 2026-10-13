from flask import Blueprint , render_template , request

views = Blueprint("views" , __name__)

@views.route("/" , methods=["GET","POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        return f"{username} + {password}"
    return render_template("base.html")