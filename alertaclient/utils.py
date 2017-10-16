
import datetime

import pytz
import six


class DateTime(object):
    @staticmethod
    def parse(date_str):
        if not isinstance(date_str, six.string_types):
            return
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        except Exception:
            raise ValueError('dates must be ISO 8601 date format YYYY-MM-DDThh:mm:ss.sssZ')

    @staticmethod
    def iso8601(dt):
        return dt.replace(microsecond=0).strftime('%Y-%m-%dT%H:%M:%S') + ".%03dZ" % (dt.microsecond // 1000)

    @staticmethod
    def localtime(dt, timezone='Europe/London'):
        tz = pytz.timezone(timezone)
        try:
            return dt.replace(tzinfo=pytz.UTC).astimezone(tz).strftime('%Y/%m/%d %H:%M:%S')
        except AttributeError:
            return


def build_query(filters):
    return [tuple(f.split('=', 1)) for f in filters if '=' in f]