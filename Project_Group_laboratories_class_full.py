class Laboratories:

    def __init__(self, Name, Cost):
        self.Name = Name
        self.Cost = Cost
    
    def formatLabInfo (self):
        return '{}_{}'.format(self.Name, self.Cost)

    def __str__(self):
        result = self.formatLabInfo()
        return result
