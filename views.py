from flask import Blueprint , render_template , request , url_for , session , redirect
from data import users , student_records

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
            if user["role"] == "teacher":
                response = redirect(url_for("views.teacher_profile"))
            else:
                response = redirect(url_for("views.profile"))
            response.set_cookie("lab_id", str(user["uid"]))
            return response
        error = "Invalid username or password"
        return render_template("base.html", error=error)
    return render_template("base.html")

@views.route("/student/profile")
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

@views.route("/student/assignments")
def assignments():
    username = session.get("username")
    if not username:
        error="You are not logged in yet"
        return render_template("base.html",error=error)
    return render_template("assignments.html")

@views.route("/student/courses")
def courses():
    username=session.get("username")
    if not username:
        error="You are not logged in yet"
        return render_template("base.html",error=error)
    return render_template("courses.html")

@views.route("/student/settings")
def settings():
    username=session.get("username")
    uid = session.get("uid")
    role = session.get("role")
    if not username:
        error="You are not logged in yet"
        return render_template("base.html",error= error)
    return render_template("settings.html", uid=uid , role=role, username=username)

@views.route("/teacher/profile")
def teacher_profile():
    username = session.get("username")
    role = session.get("role")
    if not username:
        error = "You are not logged in yet"
        return render_template("base.html", error=error)
    if role != "teacher":
        error = "You are not a teacher bozo"
        return render_template("base.html", error=error)
    return f"Hello {username}"
    
@views.route("/student/records")
def records():
    uid = request.cookies.get("lab_id")
    username = session.get("username")
    if not username:
        error = "You are not logged in yet"
        return render_template("base.html" , error=error)
    record = student_records.get(uid)
    if not records:
        return "Record not found", 404
    return render_template("records.html", course=record["course"], gpa=record["gpa"] , feedback=record["feedback"])
