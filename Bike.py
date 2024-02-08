class Bike:
    def __init__(self):
        self.__is_on = False
        self.__speed = 0
        self.__gear = 0

    def bike_is_on(self):
        return self.__is_on

    def is_on(self):
        self.__is_on = True
        pass

    def is_off(self):
        self.__is_on = False
        pass

    def get_gear(self):
        if self.bike_is_on and self.__speed >= 0 and self.__speed < 20:
            self.gear = 1
        elif self.__speed >= 20 and self.__speed <= 30:
            self.gear = 2
        elif self.__speed > 30 and self.__speed < 40:
            self.gear = 3
        elif self.__speed >= 40:
            self.gear = 4
        return self.gear;
        pass

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def accelerate(self):
        self.get_gear()
        if self.bike_is_on and self.gear == 1:
            self.__speed += 1
        elif self.bike_is_on and self.gear == 2:
            self.__speed += 2
        elif self.bike_is_on and self.gear == 3:
            self.__speed += 3
        elif self.bike_is_on and self.gear == 4:
            self.__speed += 4

    def decelerate(self):
        self.get_gear()
        if self.bike_is_on and self.gear == 1:
            self.__speed -= 1
        elif self.bike_is_on and self.gear == 2:
            self.__speed -= 2
        elif self.bike_is_on and self.gear == 3:
            self.__speed -= 3
        elif self.bike_is_on and self.gear == 4:
            self.__speed -= 4
        pass
