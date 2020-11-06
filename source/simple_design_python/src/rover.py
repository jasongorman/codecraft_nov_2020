import logging

RIGHT = "R"


class Rover(object):
    def __init__(self, x, y, facing):
        self.facing = facing
        self.position = (x, y)

    def go(self, instructions):


        for instruction in list(instructions):
            self.execute(instruction)

    def execute(self, instruction):
        if instruction == RIGHT:
            return self.right()

        if instruction == "L":
            return self.left()

        if instruction == "F":
            if self.facing == "N":
                self.position = (self.position[0], self.position[1] + 1)

            if self.facing == "E":
                self.position = (self.position[0] + 1, self.position[1])

            if self.facing == "S":
                self.position = (self.position[0], self.position[1] - 1)

            if self.facing == "W":
                self.position = (self.position[0] - 1, self.position[1])

        if instruction == "B":
            if self.facing == "N":
                self.position = (self.position[0], self.position[1] - 1)

            if self.facing == "E":
                self.position = (self.position[0] - 1, self.position[1])

            if self.facing == "S":
                self.position = (self.position[0], self.position[1] + 1)

            if self.facing == "W":
                self.position = (self.position[0] + 1, self.position[1])

    def left(self):
        anti_clockwise = ["N", "W", "S", "E"]
        self.turn(anti_clockwise)

    def right(self):
        clockwise = ["N", "E", "S", "W"]
        self.turn(clockwise)

    def turn(self, compass):
        current = compass.index(self.facing)
        self.facing = compass[(current + 1) % 4]
