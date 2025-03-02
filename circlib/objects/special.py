from .base import PhysicalObject, PhysicsType
from ..level import Level

class obj_Dummy(PhysicalObject):
    ingame_type: str = 'dummy'
    physics_type: PhysicsType = PhysicsType.solid

class obj_Player(PhysicalObject):
    ingame_type: str = 'y'
    physics_type: PhysicsType = PhysicsType.moveable
    
    radius: float = 1
    density: float = 1
    damping: float = 0