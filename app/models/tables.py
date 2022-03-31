from app.extensions.db import db

class CountDown(db.Model):
    __tablename__ = 'countdown'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime())
