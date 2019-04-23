import numpy
from enum import Enum


class  ObjectType(Enum):
    BALL = 1
    WALL = 2


class PhysicsObject:

    def __init__(self, type, props=None, pos=(0, 0), spd=(0, 0)):
        self.type = type
        self.props = props
        self.pos = pos
        self.spd = spd

    def update_position(self, time_diff_ms):
        self.pos = numpy.add(self.pos, self.spd)

    def collidepoint(self, point):
        if self.type == ObjectType.BALL:
            diff = numpy.subtract(point, self.pos)
            if numpy.linalg.norm(diff) <= self.props[0]:
                return True
            return False
