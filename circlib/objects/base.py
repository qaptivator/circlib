from enum import Enum
from ..level import Level
from abc import ABC, abstractmethod
from dataclasses import dataclass

class ObjectCategory(Enum):
    unknown = 0
    fixed = 1 # fixed circle, triangle, line
    movable = 2 # movable circle, movable triangle
    growing = 3 # growing circle, growing rectangle
    connection = 4 # rope, superglue, special
    rotatable = 5 # rotatable circle, rotatable rectangle
    springy = 6 # springy rectangle
    generator = 7 # ball geneator, box generator
    special = 8 # portal, start, collectable

class BaseObject(ABC):
    ''' Base abstract class for all objects. '''

    ingame_type: str

    def __init__(self, level: Level):
        self.level = level

    def whoami(self):
        ''' Returns class name '''
        return type(self).__name__

    @abstractmethod
    def serialize(self) -> str:
        ''' Export the object into level code.
        This would be called on each object during level.stringify() 
        You need to return valid level code, which will then get appended to the rest of the level. '''
        pass

class PhysicsType(Enum):
    none = -1 # y, ic
    solid = 0 # c, b, LE_ARC_DESCRIPTION, curve
    moveable = 1 # mb, mc, mcG
    rotateable = 2 # rr, rc
    growing = 3 # gc, rGr
    springy = 5 # wr
    generator = 6 # tmc, tmb
    unknown = 7 # partR

class PhysicalObject(BaseObject):
    ''' Abstract class for objects, which exist physically (have XY coordinates). '''

    physics_type: PhysicsType

    def __init__(self, level: Level, x: float = 0, y: float = 0, physics_type: PhysicsType = PhysicsType.none):
        super().__init__(level)
        self.x = x
        self.y = y
        self.physics_type = physics_type