class Bycicle:
    def __init__(self, name, price, hasmotor, exerciseBike):
        self.name = name
        self.price = price
        self.hasmotor = hasmotor
        self.exerciseBike = exerciseBike

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_hasMotor(self):
        return self.hasmotor

    def get_exerciseBike(self):
        return self.exerciseBike

    def motor(self):
        print(self.name + " cost= " + str(self.price) + " have a motor: " + str(self.hasmotor) + " exerciseBike:" + str(self.exerciseBike))