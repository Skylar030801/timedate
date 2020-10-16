from datetime import date
from datetime import time
from datetime import datetime, timedelta

d=date(2013, 8,22 )
print(d.year)
print(d.month)
print(d.day)
print(d.strftime("%Y %m %d"))

t=time(2, 30, 45)
print(t.hour)
print(t.minute)
print(t.second)
print(t.strftime("%H: %M:%S"))

dt= datetime (2020 , 10 , 16 ,11, 22, 50)
add_dt = dt + timedelta(days=5)
print(add_dt.strftime("%m-%d-%Y %H:%M:%S"))


from datetime import datetime, timedelta

mydate= datetime(2020, 10, 16, 11, 58, 12)

x= 0
while x<10:
    print(mydate)
    mydate=mydate+timedelta (days=14)
    x=x+1

