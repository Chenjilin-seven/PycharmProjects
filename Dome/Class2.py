class People:
    def __init__(self, number , name):
        self.number = number
        self.name = name
    def print_info(self):
        print(f"I'm {self.name},my number is {self.number}")

class PeopleA(People):
    def __init__(self,number , name , moon_dollar):
        super().__init__(number , name)
        self.moon_dollar = moon_dollar
    def get_dollar ( self ):
        return self.moon_dollar

class PeopleB(People):
    def __init__(self ,number , name , day_dollar , days):
        super().__init__(number , name)
        self.day_dollar = day_dollar
        self.days = days
    def get_dollar(self):
        return self.day_dollar * self.days
F = People(0xCCF,"xxs")
FA = PeopleA(0xADB,"xxx's",10000000)
FB = PeopleB(0xBBC,"xxxs",100000,5)
F.print_info()
FA.print_info()
print(FA.get_dollar())
FB.print_info()
print(FB.get_dollar())
"""
@property
@score.setter
"""