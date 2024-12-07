from flask import Blueprint
from flask import render_template
from app.models import Todo
from app import  bcrypt, db
from flask_login import current_user


main = Blueprint("main", __name__)


@main.route("/")

@main.route("/home")
def home():
    if current_user.is_authenticated:
        tasks = Todo.query.filter_by(user_id=current_user.id).all()
        
    return render_template("home.html", tasks=tasks or [])  # Use empty list if tasks is None

@main.route("/about")
def about():
    return render_template("about.html", title="About")

