from app import create_app
from app.ext.websocket import socketio

app = application = create_app('config.Config')
