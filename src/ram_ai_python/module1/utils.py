from datetime import datetime, date, time, timedelta
import time

now = datetime.now()
today = date.today()
print(f"today is {today}")
current_time = datetime.now().time()
print(f"current time is {current_time}")
print(now)
# Specific exceptions
try:
    result = 10 / 10
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("Success!")
finally:
    print("Cleanup code here")