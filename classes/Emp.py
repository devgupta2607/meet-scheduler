class Emp:
    def __init__(self, emp_id):
        self.emp_id = emp_id
        self.emp_meetings = []

    #checking for available slots in employee's meeting schedule
    def is_available_slot(self,start_dt,end_dt):
        self.emp_meetings.sort(key= lambda x:(x.start_time,x.end_time))

        # Meeting limit set to 2 and for checking whether there is any conflict
        if (len(self.emp_meetings) < 2):
            if len(self.emp_meetings) == 0 or (end_dt < self.emp_meetings[0].start_time):
                return True
            i = 0
            while i < (len(self.emp_meetings) - 1):
                prev = self.emp_meetings[i]
                next = self.emp_meetings[i+1]

                if start_dt > prev.end_time and end_dt < next.start_time:
                    return True
                i = i + 1

            if start_dt > self.emp_meetings[i].end_time:
                return True
        else:
            print("Error : You are already the organizer of two scheduled meetings.")
            return False
