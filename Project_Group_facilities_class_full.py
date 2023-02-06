class Facilities:

    def __init__(self, Name):
        self.Name = Name
    
    def formatFacilityInfo (self):
        return '{}'.format(self.Name)

    def __str__(self):
        result = self.formatFacilityInfo()
        return result

