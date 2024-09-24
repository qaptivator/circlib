from .utils import *
from .constants import *

class Object:
    id = 0,
    type = '',
    props = [],
    connections = [],

    def __init__(self, id=0, type='', props=[], connections=[]):
        self.id = id
        self.type = type
        self.props = string_to_list(props)
        self.connections = connections

    @staticmethod
    def from_object(obj):
        return Object(
            obj.get("id"),
            obj.get("type"),
            obj.get("props"),
            obj.get("connections")
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

    
    
