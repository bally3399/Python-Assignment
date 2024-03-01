class SevenSegment:
    def __init__(self):
        self.segments = [''] * 7
        self.is_on = True
        self.switch_value = 0

    def is_on(self):
        return self.is_on

    def turn_on(self):
        if self.switch_value == 1:
            self.is_on = True

    def splitting_into_array(self, binary):
        if len(binary) != 7 or not all(bit in '01' for bit in binary):
            raise ValueError("Invalid binary input")
        for index in range(len(self.segments)):
            if binary[index] != '0' and binary[index] != '1':
                raise ValueError("Invalid binary")
            self.segments[index] = binary[index]
        self.display_seven()

    def display_seven(self):
        if len(self.segments) != 7:
            raise ValueError("Input array length must be exactly 7")
        self.display_1(self.segments[0])
        self.display_2(self.segments[5], self.segments[1])
        self.display_1(self.segments[6])
        self.display_2(self.segments[4], self.segments[2])
        self.display_1(self.segments[3])

    @staticmethod
    def display_1(segment):
        if segment != "0" and segment != "1":
            raise ValueError("Invalid segment")
        if segment == "1":
            print("* * * * *")
        else:
            print("     ")

    @staticmethod
    def display_2(segment, segment2):
        if segment != "0" and segment != "1":
            raise ValueError("Invalid segment")
        if segment2 != "0" and segment2 != "1":
            raise ValueError("Invalid segment")
        if segment == "1" and segment2 == "1":
            for idx in range(4):
                print("*       *")
        elif segment == "1" and segment2 != "1":
            for idx in range(4):
                print("*       ")
        elif segment != "1" and segment2 == "1":
            for idx in range(4):
                print("       *")


def main():
    seven_segment = SevenSegment()
    segments = "1111111"
    seven_segment.splitting_into_array(segments)


if __name__ == '__main__':
    main()
