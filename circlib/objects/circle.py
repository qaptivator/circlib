from .base import PhysicalObject, PhysicsType
from ..level import Level

# TODO: make deserialization

class CircleObject(PhysicalObject):
    ingame_type: str = 'c'
    radius: float

    def __init__(self, level: Level, x: float = 0, y: float = 0, radius: float = 0):
        super().__init__(level, x, y, PhysicsType.solid)
        self.radius = radius

class MoveableCircleObject(PhysicalObject):
    ingame_type: str = 'mcG'
    radius: float
    density: float
    damping: float

    def __init__(
            self, 
            level: Level, 
            x: float = 0, 
            y: float = 0, 
            radius: float = 0, 
            density: float = 1, 
            damping: float = 0
        ):
        super().__init__(level, x, y, PhysicsType.moveable)
        self.radius = radius
        self.density = density
        self.damping = damping

# TODO: find out what this object even is
class MoveableCircleStaticObject(PhysicalObject):
    ingame_type: str = 'mc'
    radius: float
    density: float
    damping: float

    def __init__(
            self, 
            level: Level, 
            x: float = 0, 
            y: float = 0, 
            radius: float = 0, 
            density: float = 1, 
            damping: float = 0
        ):
        super().__init__(level, x, y, PhysicsType.moveable)
        self.radius = radius
        self.density = density
        self.damping = damping

class GrowingCircleObject(PhysicalObject):
    ingame_type: str = 'gc'
    radius: float

    def __init__(self, level: Level, x: float = 0, y: float = 0, radius: float = 0):
        super().__init__(level, x, y, PhysicsType.growing)
        self.radius = radius

class GeneratorCircleStaticObject(PhysicalObject):
    ingame_type: str = 'tmc'
    radius: float
    density: float
    #damping: float
    alive_time: float # n / 60
    inbetween_time: float # n / 60
    delay_time: float # n / 60

    def __init__(
            self, 
            level: Level,
            x: float = 0,
            y: float = 0,
            radius: float = 0,
            density: float = 1,
            #damping: float = 0,
            alive_time: float = 0, # TODO: find out the default parameters
            inbetween_time: float = 0,
            delay_time: float = 0
        ):
        super().__init__(level, x, y, PhysicsType.generator)
        self.radius = radius
        self.density = density
        #self.damping = damping
        self.alive_time = alive_time
        self.inbetween_time = inbetween_time
        self.delay_time = delay_time