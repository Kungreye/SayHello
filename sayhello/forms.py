# _*_ coding: utf-8 _*_

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()
