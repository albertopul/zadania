from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = TextAreaField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    year = StringField('year', validators=[DataRequired()] )
    pages = StringField('pages', validators=[DataRequired()])



