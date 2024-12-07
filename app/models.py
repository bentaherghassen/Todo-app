from flask import current_app
from itsdangerous import URLSafeTimedSerializer as Serializer
from app import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def get_reset_token(self):
        s = Serializer(current_app.config["SECRET_KEY"], salt="pw-reset")
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token, age=3600):
        s = Serializer(current_app.config['SECRET_KEY'], salt='pw-reset')
        try:
            user_id = s.loads(token, max_age=age)['user_id']
        except:
            return None
        return User.query.get(user_id)

    

    def __repr__(self):
        return f"User('{self.fname}', '{self.lname}', '{self.username}', '{self.email}', '{self.password}')"



class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.Date)
    is_completed = db.Column(db.Boolean, default=False)
    is_important = db.Column(db.Boolean, default=False)
    is_urgent = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Define the relationship
    user = db.relationship('User', backref='todos')

    def __repr__(self):
        return f"Todo('{self.title}', '{self.description}', '{self.due_date}', {self.is_completed})"