import datetime

date = datetime.date(2026, 6, 12)

today = datetime.datetime.today()


time = datetime.time(8, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%Y")
print(now)