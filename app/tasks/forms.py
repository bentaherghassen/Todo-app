from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import (
    DataRequired,
    Length,
    ValidationError,
)



class New_task(FlaskForm):
    title = StringField("Task Title", validators=[DataRequired(), Length(max=50)])
    description = TextAreaField(
        "Task Description", validators=[DataRequired(), Length(max=150)]
    )
    
    submit = SubmitField("Create")
    