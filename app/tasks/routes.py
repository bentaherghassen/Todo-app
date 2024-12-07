from flask import Blueprint
from flask import render_template, url_for, flash, redirect, request

from app import  bcrypt, db
from flask_login import (
    login_required,
    login_user,
    current_user,
    logout_user,
    )
from app.tasks.forms import New_task
from app.models import User,Todo


tasks = Blueprint("tasks", __name__)

@tasks.route("/new_task", methods=["GET", "POST"])
@login_required
def new_task():
    form = New_task()
    if form.validate_on_submit():
        task = Todo(
            title=form.title.data,
            description=form.description.data,
            #due_date=form.due_date.data,
            #is_completed=form.is_completed.data,
            user_id=current_user.id,  # Associate task with current user
        )
        db.session.add(task)
        db.session.commit()
        flash("Task added successfully , Go to Home page to see your Tasks!", "success")
        return redirect(url_for("tasks.new_task"))  
    return render_template("new_task.html", title="Add Task", form=form)





@tasks.route("/task/<int:task_id>/delete", methods=['POST'])
@login_required
def delete_task(task_id):
    task = Todo.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        abort(403)
    db.session.delete(task)
    db.session.commit()
    flash('Your task has been deleted!', 'success')
    return redirect(url_for('main.home'))