import time

"""
def sleep(secs: float) -> None
sleep(seconds)
Delay execution for a given number of seconds. 
The argument may be a floating point number for sub second precision.

time.sleep(3)
"""

my_time = int(input("Enter the time in seconds: "))

"""
Return a reverse iterator over the values of the given sequence.
"""

for x in reversed(range(0, my_time)):
    seconds = x % 60
    minute = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minute:02}: {seconds:02}")
    time.sleep(1)

print("Time is up ⏰")
