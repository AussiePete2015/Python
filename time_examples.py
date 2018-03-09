import time, uuid
from datetime import date, datetime, timedelta
 
current_dt = datetime.now()
week_ago_dt = current_dt - timedelta(days=7)
from_dt = str(week_ago_dt)[0:11] + '00:30'
to_dt = str(current_dt)[0:11] + '23:30'
print from_dt
print to_dt

fromTime = from_dt
fromTime = int(time.mktime(time.strptime(fromTime, '%Y-%m-%d %H:%M'))*1000)
print fromTime

toTime = to_dt
toTime = int(time.mktime(time.strptime(toTime, '%Y-%m-%d %H:%M'))*1000)
print toTime
