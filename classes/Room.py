class Room:
    def __init__(self, meet_id):
        self.meet_id = meet_id
        self.booked_meets = []
    
    def is_available_slot(self,start_dt,end_dt):
        self.booked_meets.sort(key= lambda x:(x.start_time,x.end_time))
        if len(self.booked_meets) == 0 or (end_dt < self.booked_meets[0].start_time):
            return True
        
        i = 0

        while i < (len(self.booked_meets) - 1):
            prev = self.booked_meets[i]
            next = self.booked_meets[i+1]

            if start_dt > prev.end_time and end_dt < next.start_time:
                return True
            i = i + 1

        if start_dt > self.booked_meets[i].end_time:
            return True

        
