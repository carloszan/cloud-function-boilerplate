import csv
from functools import wraps
import time
from datetime import datetime


def csv_to_array(file: str):
    dict = {}
    with open(file) as csvfile:
        # Converting the csv data into dictionary
        csv_data = csv.DictReader(csvfile)
        dict["data"] = []
        for rows in csv_data:
            dict["data"].append(rows)

    return dict['data']


def chunk_array(array, chunk_size):
    return [array[i:i+chunk_size] for i in range(0, len(array), chunk_size)]


def retry(ExceptionToCheck, tries=4, delay=5, backoff=2):
    def retry_decorator(func):

        @wraps(func)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except ExceptionToCheck as e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    print(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
                    if mtries == 1:
                        print(f"{func.__name__} failed with: {e}")
                        raise Exception(e)
            return func(*args, **kwargs)

        return f_retry

    return retry_decorator


def convert_to_iso_format(date: str):
    timestamp = datetime.strptime(date, "%Y-%m-%d %H:%M:%S %Z")

    return timestamp.isoformat()
