from datetime import datetime, timedelta

from flask import url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from wtforms.validators import DataRequired
from markupsafe import Markup

from app.models.tables import CountDown
from app.extensions.db import db


admin = Admin(name='Count Down')

def dateFormat(view, context, model, name):
    if model.time:
        if model.time >= datetime.utcnow():
            time = model.time - datetime.utcnow()
            return str(time).split(".")[0]
        return 'Expirado'
    return ''

class CustomModelView(ModelView):
    column_display_pk = True
    column_labels = dict(id='ID', time='Tempo (H:M)')
    form_args = {
        'time': {
            'validators': [DataRequired()],
            'format': '%H:%M'
        }
    }
    column_formatters = {
        'time': dateFormat,
        'id': lambda view, context, model, name: Markup(f"<a href='{url_for('home.home', id=model.id)}'>{model.id}<a>")
    }
    form_widget_args = {
        'time': {
            'data-date-format': u'HH:mm',
            'data-role': 'timepicker',
            'autocomplete': 'off',
            'value': '00:00'
        }
    }

    def on_model_change(self, form, model, is_created):
        if is_created:
            date = form.time.data
            utc_time = datetime.utcnow() + timedelta(minutes=date.minute, hours=date.hour)
            model.time = utc_time


def configure(app):
    admin.init_app(app)
    admin.add_view(CustomModelView(CountDown, db.session))
