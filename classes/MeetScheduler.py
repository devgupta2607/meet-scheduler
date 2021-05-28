from classes.Emp import Emp
from classes.Meet import Meet
from classes.Room import Room
from datetime import datetime, timedelta

class MeetScheduler:
    emps = []  # Employee objects array
    rooms = [] # Room objects array
    meet_ids = set([]) # For available meet ids
    scheduled_meets = {} # Dictionary to keep scheduled meets with meet_id as key
    
    def __init__(self,no_of_emp, no_of_meet_rooms):
        self.no_of_emp = no_of_emp
        self.no_of_meet_rooms = no_of_meet_rooms

        # Creating and storing requried objects
        for i in range(1, no_of_emp+1):
            MeetScheduler.emps.append(Emp(i))

        for i in range(1, no_of_meet_rooms+1):
            MeetScheduler.rooms.append(Room(i))

        for i in range(1, 50000):
            MeetScheduler.meet_ids.add(i)
    
    # Checking validity of given start time and end time
    def is_valid_meet_time(self,emp_id, start_dt, end_dt):
        emp_meets = MeetScheduler.emps[emp_id-1].emp_meetings
        if (len(emp_meets) > 0):
            for meet in emp_meets:
                if (meet.start_time == start_dt and meet.end_time == end_dt):
                    print("Error : You have exceeded the max limit of bookings at a time'")
                    return False
        
        diff_time = start_dt - datetime.now()
        if (diff_time.days > 30):
            print("Error : Cannot book beyond 1 month from today")
            return False
        
        if (diff_time.days < 0):
            print("Error : Cannot book a meet in the past")
            return False

        diff_interval = end_dt - start_dt

        if (timedelta.total_seconds(diff_interval) > 10800):
            print("Error : Cannot book a meeting of more than 3 hrs duration")
            return False
        
        return True

    # For booking meet
    def book_meet(self, emp_id, start_dt, end_dt):
        if emp_id <= 0 or emp_id > self.no_of_emp:
            print("Employee Id invalid, Employee Id in scheduler ranges from 1 to ", self.no_of_emp)
            return
        
        if not self.is_valid_meet_time(emp_id, start_dt, end_dt):
            return

        emp_obj = MeetScheduler.emps[emp_id-1] # Current employee object

        if emp_obj.is_available_slot(start_dt,end_dt):
            for room in range(0,len(MeetScheduler.rooms)):
                room_obj = MeetScheduler.rooms[room]

                if (room_obj.is_available_slot(start_dt,end_dt)):
                    meet_id = self.meet_ids.pop()
                    new_meet = Meet(start_dt,end_dt,meet_id,emp_id,room)
                    emp_obj.emp_meetings.append(new_meet)
                    room_obj.booked_meets.append(new_meet)
                    MeetScheduler.scheduled_meets[meet_id] = new_meet
                    print("Meeting Scheduled successfully")
                    print("Meet Id: ",meet_id, " and Room Id: ",room)
                    return True
            print("Error : All rooms busy for the given time interval.")
            return False
        
        else:
            print("Conflict")
            return False
    
    def cancel_meet(self,emp_id,meet_id):
        if (meet_id not in MeetScheduler.scheduled_meets):
            print("Invalid Meet ID. Enter a valid Meet ID")
            return False
        
        curr_meet = MeetScheduler.scheduled_meets[meet_id] # Current meet object

        if (curr_meet.organiser_id == emp_id):
            emp_obj = MeetScheduler.emps[emp_id-1]
            room_obj = MeetScheduler.rooms[curr_meet.room_id]
            if (len(emp_obj.emp_meetings) > 0):
                emp_obj.emp_meetings.remove(curr_meet)
                room_obj.booked_meets.remove(curr_meet)
            else:
                print("No meeting scheduled. Cancel a valid meet.")
                return
            print("Meeting Cancelled")
            return
        else:
            print("You are not the organiser of the meeting")
            return