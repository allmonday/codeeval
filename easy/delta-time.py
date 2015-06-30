data = '''14:01:57 12:47:11
13:09:42 22:16:15
08:08:06 08:38:28
23:35:07 02:49:59
14:31:45 14:46:56'''

tests = data.split('\n')
print tests

def to_seconds(date):
    hour, minute, second = date.strip().split(':')
    hour = int(hour)
    minute = int(minute)
    second = int(second)
    return second + 60*minute + 3600*hour

def to_date(seconds):

    s = seconds % 60
    seconds -= s
    m = seconds % 3600
    m /= 60
    seconds -= m
    h = seconds  / 3600
    return "{:02d}:{:02d}:{:02d}".format(h,m,s)

for test in tests:
    t1, t2 = test.split(' ')
    t1 = to_seconds(t1)
    t2 = to_seconds(t2)
    delta = abs(t1 - t2)
    print to_date(delta)
