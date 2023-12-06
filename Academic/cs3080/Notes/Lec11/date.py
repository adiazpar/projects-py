import datetime
import time

print(type(datetime.datetime.now()))
# <class 'datetime.datetime'>
print(datetime.datetime.now())
# 2023-10-31 16:56:37.784882 (your actual time)
dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(dt.year, dt.month, dt.day)
# 2015 10 21
print(dt.hour, dt.minute, dt.second)
# 16 29 0


print(datetime.datetime.fromtimestamp(1000000))
# 1970-01-12 06:46:40
print(datetime.datetime.fromtimestamp(time.time()))
# 2023-10-31 16:56:37.784929


thanksgiving2023 = datetime.datetime(2023, 11, 23, 0, 0, 0)
newyears2024 = datetime.datetime(2024, 1, 1, 0, 0, 0)
nov23_2023 = datetime.datetime(2023, 11, 23, 0, 0, 0)

print(thanksgiving2023 == nov23_2023)	# True
print(thanksgiving2023 > newyears2024)	# False
print(newyears2024 > thanksgiving2023)	# True
print(newyears2024 != nov23_2023)	# True


christmas2023 = datetime.datetime(2023, 12, 25, 0, 0, 0)
while datetime.datetime.now() < christmas2023:
    print(datetime.datetime.now())
    time.sleep(1)

# --code-- do something after that date

