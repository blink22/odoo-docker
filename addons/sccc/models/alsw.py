
from odoo import models
from datetime import datetime, time
from odoo.tools.misc import DEFAULT_SERVER_TIME_FORMAT
import pytz
class Time(models.Field):
    type = 'time'
    column_type = ('time', 'time')
    column_cast_from = ('datetime',)

    def convert_to_cache(self, value, record, validate=True):
        if not value:
            return False
        # if not isinstance(value, time):
            # raise TypeError("%s (field %s) must be time." % (value, self))
        return value

    @staticmethod
    def to_string(value):
        time_format = "%m/%d/%Y %I:%M %p"
        return value.strftime(time_format).astimezone(pytz.utc) if value else False

    @staticmethod
    def to_time(value):
        time_format = "%m/%d/%Y %I:%M %p"
        return datetime.strptime(value, time_format).astimezone(pytz.utc).time() if value else False