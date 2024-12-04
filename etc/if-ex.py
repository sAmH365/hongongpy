import datetime
import pytz

a = input("숫자를 입력해주세요: ")

if int(a) > 100:
  print(f"{a}은 100 보다 큽니다.")
else:
  print(f"{a}은 100보다 작습니다.")

seoul = pytz.timezone("Asia/Seoul")
now = datetime.datetime.now(seoul)

if now.hour < 12:
  print("오전입니다.")

if now.hour >= 12:
  print("오후입니다.")
