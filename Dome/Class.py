class Car:
    say = "Duuuu,Duuuu"
    def __init__(self , speed , name):
        self.speed = speed
        self.name =name
    def let_go(self):
        print(f"{self.name} is going.Speed{self.speed}")
    @classmethod
    def speak(cls):
        print(cls.say)

class StopCar (Car):
    def stop(self):
        print(f"{self.name} is stoped.")
bus = Car(55 , "Bus")
car = StopCar(150 , "Car")
bus.let_go()
car.let_go()
# bus.stop()
car.stop()
# car.say()
bus.speak()