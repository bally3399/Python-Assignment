class Television:
    def __init__(self):
        self.__tv_is_on = False
        self.__volume = 0
        self.__channel = 0

    def television_is_on(self):
        return self.__tv_is_on

    def turn_on(self):
        self.__tv_is_on = True

    def turn_off(self):
        self.__tv_is_on = False

    def get_volume(self):
        return self.__volume

    def volume_up(self):
        if self.__tv_is_on and self.__volume < 100:
            self.__volume += 1
        return self.__volume

    def volume_down(self):
        if self.__tv_is_on and self.__volume < 100:
            self.__volume -= 1
        return self.__volume

    def get_channel(self):
        return self.__channel

    def channel(self):
        if self.__tv_is_on and self.__channel < 20:
            self.__channel += 1
            return self.__channel
        pass
