from .base import PhysicalObject, PhysicsType
from ..level import Level

class PlayerObject(PhysicalObject):
    ingame_type: str = 'y'
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