import time
from ysi_exo.parameter_codes import *

def convert_date_to_epoch(date_value, time_value, date_parameter_code=DATE_YY):
    """Convert date and time to epoch.

    Args:
        date (float): Date, YYMMDD.
        time (float): HHMMSS.

    Returns:
        float: epoch time.
    
    .. _YSI EXO:
        https://www.ysi.com/File%20Library/Documents/Manuals/EXO-User-Manual-Web.pdf
    """

    return int(time.mktime(
        time.strptime(str(int(date_value))+str(int(time_value)), 
        DATE_FORMAT[date_parameter_code]+TIME_FORMAT))) 

def timestamp_available(parameter_codes):
    """Find whether the timestamp is available in the parameters returned.

    Args:
        parameter_codes (list): parameters that are returned by the sonde.

    Returns:
        date_index (int): index in parameter_codes corresponding to date, -1 if not found.
        time_index (int): index in parameter_codes corresponding to time, -1 if not found.
    """

    date_index = -1
    time_index = -1
    for i, p in enumerate(parameter_codes):
        if p in [DATE_YY, DATE_MM, DATE_DD]:
            date_index = i
        elif p == TIME:
            time_index = i

    return date_index, time_index
