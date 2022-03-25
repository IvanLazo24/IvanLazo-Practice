class Car:
    def __init__(self, name, price, hasmotor, usegas):
        self.name = name
        self.price = price
        self.hasmotor = hasmotor
        self.usegas = usegas

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_hasMotor(self):
        return self.hasmotor

    def get_usegas(self):
        return self.usegas

    def motor(self):
        print(self.name + " cost= " + str(self.price) + " have a motor: " + str(self.hasmotor) + " use gas:" + str(self.usegas))