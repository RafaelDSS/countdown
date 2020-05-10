from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.model import BaseModelView
from app.models.tables import CountDown
from app.ext.db import db
from datetime import datetime, timedelta
from dateutil import tz
import time
from wtforms.validators import DataRequired


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
    column_labels = dict(id='ID', time='Tempo')
    form_args = {
        'time': {
            'validators': [DataRequired()],
            'format': '%H:%M:%S'
        }
    }
    column_formatters = {
        'time': dateFormat
    }
    form_widget_args = {
        'time': {
            'data-date-format': u'HH:mm:ss',
            'data-role': 'timepicker',
            'autocomplete': 'off'
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
