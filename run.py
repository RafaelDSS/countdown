from app import create_app
from app.extensions.websocket import socketio

app = create_app()

socketio.run(app)
