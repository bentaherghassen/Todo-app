from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_login import current_user
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Regexp,
    EqualTo,
    ValidationError,
)
from app.models import User



class RegistrationForm(FlaskForm):
    fname = StringField(
        "Enter your first name !", validators=[DataRequired(), Length(min=2, max=25)]
    )
    lname = StringField("Enter your Last name ! ", validators=[DataRequired(), Length(min=2, max=25)])
    username = StringField(
        "Enter your username ! ", validators=[DataRequired(), Length(min=2, max=25)]
    )
    email = StringField("Enter your Address E-mail !", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Enter your Password !",
        validators=[
            DataRequired(),
            Regexp(
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$"
            ),
        ],
    )
    confirm_password = PasswordField(
        "Re-enter your Password !", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                "Username already exists! Please chosse a different one"
            )

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already exists! Please chosse a different one")


class LoginForm(FlaskForm):
    email = StringField("Enter your Address E-mail !", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Enter your Password !",
        validators=[
            DataRequired(),
        ],
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")



class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send Request ')

class ResetPasswordForm(FlaskForm):
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Regexp(
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$"
            ),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Reset Password")