from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Desk
from application.forms import DeskForm, ChoiceForm


@app.route('/', methods=['GET', 'POST'])
def index():

    choice = ChoiceForm()
    form = DeskForm()

    if form.desk.data:

        _desk = form.desk.data[-3:]
        _date = form.date.data

        desk_db = Desk.query.filter_by(date=_date, desk=_desk).first()
        desk_db.occupied = 'Y'

        db.session.commit()

        return redirect(url_for('confirmation'))

    if choice.date_choice.data:

        _date = choice.date_choice.data
        _floor = choice.floor.data[-1]

        desk_db = Desk.query.filter_by(date=_date, floor=_floor).all()

        return render_template('index.html', desks=desk_db, desk=Desk, form=form, choice=choice, _date=_date)

    return render_template('index.html', desk=Desk, form=form, choice=choice)

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')
