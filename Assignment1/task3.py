from datetime import datetime
today = datetime.today()
print("Today's date:", today)
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)