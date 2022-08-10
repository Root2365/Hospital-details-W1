# Enter date

class dateType:
    def __init__(self,date):
        date = str(date).split("/")
        self.day = date[0]
        self.month = date[1]
        self.year = date[2]

    def display(self):
        print(self.day+"/"+ self.month+"/"+self.year)