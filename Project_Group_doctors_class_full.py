class Doctors:
    def __init__(self, ID, Name, Specialty, Schedule, Qualifications, RoomNbr):
        self.id = ID
        self.Name = Name
        self.Specialty = Specialty
        self.Schedule = Schedule
        self.Qualifications = Qualifications
        self.RoomNbr = RoomNbr
    
    def formatDrInfo (self):
        return '{}_{}_{}_{}_{}'.format(self.id, self.Name, self.Specialty, self.Schedule, self.Qualifications, self.RoomNbr)

    def __str__(self):
        result = self.formatDrInfo()
        return result

        
 

