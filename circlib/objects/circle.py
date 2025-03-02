from .base import PhysicalObject, PhysicsType
from ..level import Level

# TODO: make deserialization for each object
# TODO: find out the defautl values for radiuses, densities etc
# TODO: make a variable for default radius

class obj_FixedCircle(PhysicalObject):
    ingame_type: str = 'c'
    physics_type: PhysicsType = PhysicsType.solid

    radius: float = 5

class obj_MoveableCircle(PhysicalObject):
    ingame_type: str = 'mcG'
    physics_type: PhysicsType = PhysicsType.moveable

    radius: float = 5
    density: float = 1
    damping: float = 0

# TODO: find out what this object even is
class obj_MoveableCircleStatic(PhysicalObject):
    ingame_type: str = 'mc'
    physics_type: PhysicsType = PhysicsType.moveable

    radius: float = 5
    density: float = 1
    damping: float = 0

class obj_GrowingCircle(PhysicalObject):
    ingame_type: str = 'gc'
    physics_type: PhysicsType = PhysicsType.moveable

    radius: float = 5

    def __init__(self, level: Level, x: float = 0, y: float = 0, radius: float = 0):
        super().__init__(level, x, y, PhysicsType.growing)
        self.radius = radius

class obj_GeneratorCircle(PhysicalObject):
    ingame_type: str = 'tmc'
    physics_type: PhysicsType = PhysicsType.generator

    radius: float = 5
    density: float = 1
    damping: float = 0
    alive_time: float = 5 # n / 60
    inbetween_time: float = 1 # n / 60
    delay_time: float = 0 # n / 60