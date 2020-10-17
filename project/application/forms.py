from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

dates = [
    '19/10/2020',
    '20/10/2020',
    '21/10/2020',
    '22/10/2020',
    '23/10/2020',
    '24/10/2020',
    '25/10/2020'
]

class ChoiceForm(FlaskForm):

    date_choice = SelectField('DateChoice', validators=[DataRequired()], choices=dates)
    floor = SelectField('Floor', validators=[DataRequired()], choices=['Floor 1','Floor 2','Floor 3','Floor 4'])
    search = SubmitField('Search')


class DeskForm(FlaskForm):

    date = StringField('Date', validators=[DataRequired()])
    desk = StringField('Desk', validators=[DataRequired()])
    submit = SubmitField('Book')
