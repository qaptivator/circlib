from enum import Enum

class ObjectType(Enum):
    unknown = 0
    fixed = 1 # fixed circle, triangle, line
    movable = 2 # movable circle, movable triangle
    growing = 3 # growing circle, growing rectangle
    connection = 4 # rope, superglue, special
    rotatable = 5 # rotatable circle, rotatable rectangle
    springy = 6 # springy rectangle
    generator = 7 # ball geneator, box generator
    special = 8 # portal, start, collectable

class BaseObject:
    id: int = 0,
    type: ObjectType = ObjectType.unknown,
    ingame_type: str = '',

    def __init__(self, id=0, type=''):
        self.id = id
        self.type = type

    @staticmethod
    def from_object(obj):
        return BaseObject(
            obj.get("id"),
            obj.get("type"),
        )

    def is_connection(self):
        return self.connections and len(self.connections) > 0
    
    def get_ingame_type(self):
        return OBJECT_TYPES.get_inv(self.type)

    def get_ingame_props(self):
        return list_to_string(self.props)
        
    def get_connections(self):
        if self.is_connection():
            return self.connections
        else:
            raise TypeError("This object is not a connection")