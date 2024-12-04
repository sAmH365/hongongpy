import datetime

import pytz


seoul = pytz.timezone("Asia/Seoul")
now = datetime.datetime.now(seoul)

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
  now.year,
  now.month,
  now.day,
  now.hour,
  now.minute,
  now.second,
  )
)
