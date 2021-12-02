from datetime import datetime


def str_to_date(date: str) -> datetime.date:
    return datetime.strptime(date, '%Y-%m-%d').date()
