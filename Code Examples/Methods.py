class Time(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return str(self.hour) + ":"+str(self.minute)+":"+str(self.second)
    def __add__(self, other):
        return Time(str(self.hour+other.hour) + ":" + str(self.minute+other.minute) + ":" + str(self.second+other.second)

time1 = Time(5, 32, 0)
time2 = Time(23, 11, 11)

print time1
print time2

print time1+time2

print str(time1.hour) + ":" + str(time1.minute) + ":" + str(time1.minute)