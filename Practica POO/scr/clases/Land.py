from scr.clases.Car import Car
from scr.clases.Bycicle import Bycicle
class Land:
    def __init__(self, name, price, hasmotor):
        self.name = name
        self.price = price
        self.hasmotor = hasmotor

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_hasMotor(self):
        return self.hasmotor

    def tipo(self):
        if self.hasmotor:
            car = Car(self.name, self.price, self.hasmotor, True)
            return car.motor()
        else:
            bike = Bycicle(self.name, self.price, self.hasmotor, True)
            return  bike.motor()
#    def tipo (self):
#        print(self.name + " cost= " + str(self.price) + " have a motor: " + str(self.hasmotor))
