#1
from datetime import date, timedelta

current_date = date.today()
result_date = current_date - timedelta(days=5)

print("current date:", current_date)
print("date 5 days ago:", result_date)

#2
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("yesterday:", yesterday)
print("today:", today)
print("tomorrow", tomorrow)

#3

from datetime import datetime

dt = datetime.now()
dt_no_ms = dt.replace(microsecond=0)

print("with microseconds:", dt)
print("without microseconds: ", dt_no_ms)

#4
from datetime import datetime

date1 = datetime(2023, 10, 1, 12, 0, 0)
date2 = datetime.now()

difference = date2 - date1
seconds_diff = difference.total_seconds()

print(f"difference between {date1} and {date2}:")
print(f"{seconds_diff} seconds")



