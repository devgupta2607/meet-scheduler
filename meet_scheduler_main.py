from classes.MeetScheduler import MeetScheduler
from datetime import date, datetime, timedelta
from utils.date_time_chk import check_time

#Meet_Scheduler = MeetScheduler()

init_check = False
print("************ Welcome to Meet Scheduler *****************")
while True:
    print()
    if not init_check:
        print("1 - Initialise the meeting scheduler")
    print("2 - Book a meeting")
    print("3 - Cancel a meeting")
    print("4 - Quit")
    print()
    user_chk = int(input("Enter your Choice: "))

    if (user_chk == 1):
        if init_check:
            print("Scheduler already initialised. Try booking or canceling a meeting")
            continue
        no_of_meet_rooms = int(input("Enter the available number of meeting rooms: "))
        no_of_emp = int(input("Enter the number of employees: "))
        if (no_of_meet_rooms <= 0 or no_of_emp <= 0):
            print("Scheduler cannot be initialised due to invalid inputs. Please Try Again.")
            continue
        Meet_Scheduler = MeetScheduler(no_of_emp, no_of_meet_rooms)
        print("Initialization successful")
        init_check = True

    elif (user_chk == 2):
        emp_id = int(input("Enter your Employee ID: "))
        start_meet_dt = input("Enter the Start Date and Time of Meeting in YYYY/MM/DD HH:MM format: ")
        if (check_time(start_meet_dt) == False):
            continue
        
        end_meet_dt = input("Enter the End Date and Time of Meeting in YYYY/MM/DD HH:MM format: ")
        if (check_time(end_meet_dt) == False):
            continue

        start_meet_dt = datetime.strptime(start_meet_dt, '%Y/%m/%d %H:%M')
        end_meet_dt = datetime.strptime(end_meet_dt, '%Y/%m/%d %H:%M')
        result = Meet_Scheduler.book_meet(emp_id, start_meet_dt, end_meet_dt)

    elif (user_chk == 3):
        emp_id = int(input("Enter your Employee ID: "))
        meet_id = int(input("Enter the Meet ID: "))
        Meet_Scheduler.cancel_meet(emp_id, meet_id)

    elif (user_chk == 4):
        quit()

    else:
        print("Wrong Input. Try Again.")
        continue
