from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

from views import views
app.register_blueprint(views , prefix="/")

if __name__ == "__main__":
    app.run(debug=True)