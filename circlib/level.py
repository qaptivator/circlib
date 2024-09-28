from .utils import *
from .constants import *
import objects
from objects.base import BaseObject
from dataclasses import dataclass
from enum import Enum

'''
/
/ circloO level
/ Made with circloO Level Editor
totalCircles 7 0
/ EDITOR_TOOL 14 collectcircles
/ EDITOR_VIEW 1500 1500 1
/ EDT 964
/ _SAVE_TIME_1727472569000_END
levelscriptVersion 8
COLORS 229
grav 1 270
y 1516 1584 1 1 1
bullet
< 0
'''

class EditorToolGroupEnum(Enum):
    none = ''
    select = 'select'
    solids = 'solids'
    moveables = 'moveables'
    joints = 'joints'
    collect_circles = 'collectcircles'

@dataclass
class EditorTool:
    group: EditorToolGroupEnum
    name: str
    index: int

class EditorToolEnum(Enum):
    move_view = EditorTool(EditorToolGroupEnum.none, 'move_view', 0)
    select = EditorTool(EditorToolGroupEnum.select, 'select', 1)
    box_select = EditorTool(EditorToolGroupEnum.select, 'box_select', 46),
    delete_object = 13,



@dataclass
class LevelHeaders:
    start_full: bool = False
    level_segments: int = 7
    levelscript_version: int = LATEST_LEVELSCRIPT_VERSION
    color: int = 0 # hsv(color, 210, 255)
    starting_gravity: float = 0
    starting_gravity_dir: float = 270 # 270 is down
    editor_view: Vector2 = Vector2(1500, 1500)
    editor_zoom: float = 1
    editor_tool_group: EditorToolGroupEnum = EditorToolGroupEnum.none


class Level:
    headers: LevelHeaders = LevelHeaders()
    objects: list[BaseObject] = []

    def __init__(self, headers = [], objects = []):
        #DEFAULT_HEADERS
        self.headers = headers
        self.objects = objects

    @staticmethod
    def parse(level_code: str):
        level = Level()

        level_code_strip = level_code.strip().splitlines() # it handles both lf and crlf

        last_object = {} # object[n]
        previous_object = {} # object[n-1]

        # get the objects
        level_code_iter = iter(level_code_strip)
        for raw_line in level_code_iter:
            line = sanitize_line(raw_line)
            code = line.code
            numbers = line.numerics
            strings = line.strings


            if code == 'totalCircles':
                if len(numbers) > 0:
                    if len(numbers) > 1:
                        level.headers.start_full = True if numbers[1] == 1 else False
                    level.headers.level_segments = numbers[0]
            elif code == 'levelscriptVersion':
                if len(numbers) > 0:
                    level.headers.levelscript_version = numbers[0]
            elif code == 'COLORS':
                if len(numbers) > 0:
                    level.headers.color = numbers[0]
            elif code == 'grav':
                if len(numbers) > 0:
                    level.headers.starting_gravity = numbers[0]
                    if len(numbers) > 1:
                        level.headers.starting_gravity_dir = numbers[1]
            elif code == 'EDITOR_VIEW':
                if len(numbers) > 1:
                    level.headers.editor_view = Vector2(numbers[0], numbers[1])
                    if len(numbers) > 2:
                        level.headers.editor_zoom = numbers[2]
            elif code == 'EDITOR_TOOL':


        return level
    
    def stringify(self):
        res = LEVEL_PREFIX

        def _add_line(str, line):
            return str + line + '\n'
        
        for key, value in self.headers.items():
            header = HEADER_TYPES.get_inv(key)
            if header:
                res = _add_line(res, f'{header} {list_to_string(value)}') # f'/ {header} {_list_to_string(value)}'

        for object in self.objects:
            # it was removing the first object because apparently 0 is a falsy value
            if object.id is not None and object.type is not None and object.props is not None:
                object_type = object.get_ingame_type()
                if object_type:
                    if object.is_connection():
                        for connection in object.get_connections():
                            res = _add_line(res, f'> {connection}')
                    
                    # res = _add_line(res, f'{object_type} {list_to_string(object.props)}')
                    res = _add_line(res, f'{object_type} {object.get_ingame_props()}')

                    if object_type == 'y': # specific case just for start
                        res = _add_line(res, 'bullet')

                    res = _add_line(res, f'< {object.id}')

        return res.strip()
    
    # didnt test those yet
    def get_object_by_id(self, id: int) :
        return list(filter(lambda v: v.id == id, self.objects))[0]
    
    def get_objects_by_type(self, type: str):
        return list(filter(lambda v: v.type == type, self.objects))
    
    def create_object(self, type, props, connections = None):
        obj = Object(next_avaiable_id(self.objects), type, props, connections)
        self.objects.append(obj)
        return obj
    
    def remove_object(self, obj):
        self.objects.remove(obj)
    
    def remove_object_by_id(self, id: int):
        self.remove_object(self.get_object_by_id(id))

