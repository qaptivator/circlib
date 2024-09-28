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
    ''' Base abstract class for all objects. 
    id: int - used to identify object when linking objects during parsing. should not be modified outside of the library.
    ingame_code: str - used to detect the matching object from level code (e.g. 'fixed circle' object would have this set to 'c')'''

    id: int = 0,
    ingame_code: str = '',

    def __init__(self, level: Level, *args):
        self.level = level
        self.create(args)

    def whoami(self):
        ''' Returns class name '''
        return type(self).__name__

    @abstractmethod
    def create(self, *args):
        ''' Called on object initialization. '''
        pass

    @abstractmethod
    def serialize(self) -> str:
        ''' Export the object into level code.
        This would be called on each object during level.stringify() 
        You need to return valid level code, which will then get appended to the rest of the level. '''
        pass