import operator

NORTH = (0, 1)
SOUTH = (0, -1)
EAST = (1, 0)
WEST = (-1, 0)

directions = [NORTH, EAST, SOUTH, WEST]

class Robot(object):

    def __init__(self, direction=NORTH, coordX=0, coordY=0):
        self.coordinates = (coordX, coordY)
        self.bearing = direction

    def turn_right(self):
        if directions.index(self.bearing) < len(directions) - 1:
            self.bearing = directions[directions.index(self.bearing) + 1]
        else:
            self.bearing = directions[0]

    def turn_left(self):
        if directions.index(self.bearing) > 0:
            self.bearing = directions[directions.index(self.bearing) - 1]
        else:
            self.bearing = directions[len(directions) - 1]

    def advance(self):
        self.coordinates = tuple(map(operator.add, self.coordinates, self.bearing))

    def simulate(self, commands):
        commandMap = {
            "L": "self.turn_left()",
            "R": "self.turn_right()",
            "A": "self.advance()"
        }
        for command in commands:
            eval(commandMap[command])
