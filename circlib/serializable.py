from abc import ABC, abstractmethod
from .level import Level
from dataclasses import dataclass

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

class Serializable(ABC):
    ''' Base abstract class for all serializable things/all codes in the level code. Used for both objects and headers.
    ingame_code: str - used to detect the matching object from level code (e.g. 'fixed circle' object would have this set to 'c')'''

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