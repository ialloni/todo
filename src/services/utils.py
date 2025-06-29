from datetime import datetime


def is_valid_date(date_str: str, date_format="%d.%m.%Y.%H.%M") -> bool:
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False
