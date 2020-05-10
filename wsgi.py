from app import create_app
from app.ext.websocket import socketio


app = application = create_app('config.ProductionConfig')

if __name__ == '__main__':
    app = create_app()
    socketio.run(app)
