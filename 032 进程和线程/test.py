from datetime import datetime, timezone, timedelta
v1 = datetime.now()
v2 = datetime.utcnow()
tz = timedelta(days=1)
v3 = datetime.now()
# print(3)
v = v2 - tz
print(v)