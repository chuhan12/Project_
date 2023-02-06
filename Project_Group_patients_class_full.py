class Patients:

    def __init__(self, ID, Name, Diagnosis, Gender, Age):
        self.ID = ID
        self.Name = Name
        self.Diagnosis = Diagnosis
        self.Gender = Gender
        self.Age = Age
    
    def formatPatientInfo (self):
        return '{}_{}_{}_{}_{}'.format(self.ID, self.Name, self.Diagnosis, self.Gender, self.Age)

    def __str__(self):
        result = self.formatPatientInfo()
        return result
