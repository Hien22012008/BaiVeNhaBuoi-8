import datetime

x = datetime.datetime.now()

print('Today is:',x.strftime('%Y-%m-%d'))
print('Time right now:',x.strftime('%H:%M:%S'))