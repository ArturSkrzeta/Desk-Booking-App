from application import db # as if from __init__ import db

class Desk(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    floor = db.Column(db.String,nullable=False)
    desk = db.Column(db.String, nullable=False)
    occupied = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'{self.desk} on {self.date}'
