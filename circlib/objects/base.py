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

@dataclass
class LineOptions:
    code: str # the code (first string)
    numerics: list[int | float] # numeric arguments of the line
    strings: list[str] # string arguments of the line, doesnt include the code
    raw: list[str | int | float] # raw, separated by space, arguments of the line
    is_comment: bool = False # does this line start with a '/'

@dataclass
class DeserializeOptions:
    level: Level # the level which is currently being processed
    object_index: int # index of code occurence in level code
    target_line: LineOptions # the line where the code was detected
    lines: list[LineOptions] # all lines between the end of previous object and the end of this object (between last '>' and this '>'), includes target_line.

class BaseObject(ABC):
    ''' Base abstract class for all objects. 
    ingame_code: str - used to detect the matching object from level code (e.g. 'fixed circle' object would have this set to 'c')'''

    id: int = 0,
    ingame_code: str = '',

    category: ObjectCategory = ObjectCategory.unknown,

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
    def deserialize(self, options: DeserializeOptions):
        ''' Extract object's properties from level code.
        This would be called on each object during level.parse() '''
        pass

    @abstractmethod
    def serialize(self) -> str:
        ''' Export the object into level code.
        This would be called on each object during level.stringify() 
        You need to return valid level code, which will then get appended to the rest of the level. '''
        pass