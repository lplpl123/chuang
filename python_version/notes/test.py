import os
import time


day = time.ctime()
print(day)
print(type(day))
print(len(day))
day = day[:11] + day[20:24]
print(day)