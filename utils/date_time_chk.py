import datetime

def check_time(timing):
    time = timing.split()[1]
    hour,mins = map(int,time.split(':'))

    if (hour < 0 or hour >= 24 or mins < 0 or mins >= 60):
        print("Invalid Time")
        return False
    else:
        return True


