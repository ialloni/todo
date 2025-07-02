from datetime import datetime


def is_valid_date(date_str: str, date_format="%b %d %Y %I:%M%p") -> bool:
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False
