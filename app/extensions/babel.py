from flask_babelex import Babel


babel = Babel()

def configure(app):
    babel.init_app(app)
