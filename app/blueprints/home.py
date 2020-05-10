from flask import Blueprint, render_template, g, Response, request
from datetime import datetime
import time
from app.models.tables import CountDown
from app.ext.websocket import socketio
from flask_socketio import emit, send
import eventlet


eventlet.monkey_patch()
app_home  = Blueprint('home', __name__)

def generate(id):
    date = CountDown.query.filter_by(id=id).first()
    if date:
        while date.time >= datetime.utcnow():
            time_remaining = date.time - datetime.utcnow()
            emit('client response', {'data': str(time_remaining).split(".")[0]})
            time.sleep(0.4)

@app_home.route('/<int:id>')
def home(id):
    return render_template('index.html', timeid=id)

@socketio.on('server response')
def response(msg):
    generate(msg)
    emit('client response', {'data': 'Expirado'})
    

def configure(app):
    app.register_blueprint(app_home)