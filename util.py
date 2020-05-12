import datetime as dt
import re
from datetime import date


def is_valid_email(email: str) -> bool:
    return re.match(r'^[^@]+@[^@]+\.[^@]+$', email) is not None


def date_to_str(d: date) -> str:
    return d.strftime('%m/%d/%Y')


def str_to_date(s: str) -> date:
    return dt.datetime.strptime(s, '%m/%d/%Y').date()
