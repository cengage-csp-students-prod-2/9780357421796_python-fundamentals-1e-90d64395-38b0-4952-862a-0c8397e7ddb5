# Write your class here

class TimeEnteredNotValidError(Exception):
    def __init__(self):
        self.message = "The time is not valid"


time_entered = 8

try:
    if time_entered < 9:
        raise TimeEnteredNotValidError
except TimeEnteredNotValidError as e:
    print(e.message)

# Test you custom exception class below

