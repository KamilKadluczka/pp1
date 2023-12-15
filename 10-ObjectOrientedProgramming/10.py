class Class_name_here():
    def __init__(self, att1,att2,att3,att4):
        self.att1 = att1
        self.att2 = att2
        self.att3 = att3
        self.att4 = att4
    def __str__(self):
        print(f"Performer: {self.att1}")
        print(f"Song: {self.att2}")
        print(f"Album: {self.att3}")
        print(f"Year: {self.att4}")


var1 = Class_name_here("Name Here", "Title here", "Album here", 1111)
