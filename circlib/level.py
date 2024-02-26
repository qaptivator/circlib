from .utils import *
from .constants import *
from .object import Object

class Level:
    headers: dict[str, list[str]] = {}
    objects: list[Object] = []

    def __init__(self, headers, objects):
        self.headers = headers
        self.objects = objects

    @staticmethod
    def parse(s):
        headers: dict[str, list[str]] = {}
        objects: list[Object] = []

        lines = s.strip().split("\n")[3:] # first 3 lines are useless
        #temp_object = None
        temp_object = {}
        # {
        #    "type": '',
        #    "props": [],
        #    "connections": [], # only present in connections
        #    "id": 0
        # }

        # get the headers (first 8 lines)
        for header in lines[:HEADER_LINES]:
            props = get_props(header)
            header_type = HEADER_TYPES.get(props[0])
            if header_type:
                header_name = header_type  # HEADER_TYPE_LOOKUP[props[0]] if HEADER_TYPE_LOOKUP[props[0]] else props[0]
                headers[header_name] = props[1:]

        lines = lines[HEADER_LINES:] # we dont need those headers anymore

        # get the objects
        lines_iter = iter(lines)
        for object in lines_iter:
            props = get_props(object)
            object_type = OBJECT_TYPES.get(props[0])
            if props[0] == '<':
                if temp_object.get("type"): # temp_object is not None
                    temp_object["id"] = int(props[1])

                    objects.append(Object.from_object(temp_object))
                    #objects.append(temp_object)

                    temp_object = {}
                    #temp_object = None
            elif props[0] == '>':
                if not temp_object.get("connections"):
                    temp_object["connections"] = []
                temp_object["connections"].append(int(props[1]))
            elif props[0] == 'SKIP':
                skip_iters(lines_iter, int(props[1]))
            elif object_type is not None:
                temp_object["type"] = object_type
                temp_object["props"] = props[1:]
                #temp_object = {
                #    "type": object_type, # OBJECT_TYPE_LOOKUP[props[0]],
                #    "props": props[1:],
                #}

        return Level(headers, objects)
    
    def stringify(self):
        res = LEVEL_PREFIX

        def _add_line(str, line):
            return str + line + '\n'
        
        for key, value in self.headers.items():
            header = HEADER_TYPES.get_inv(key)
            if header:
                res = _add_line(res, f'{header} {list_to_string(value)}') # f'/ {header} {_list_to_string(value)}'

        for object in self.objects:
            if object.id and object.type and object.props:
                object_type = object.get_ingame_type()
                if object_type:
                    if object.is_connection():
                        for connection in object.get_connections():
                            res = _add_line(res, f'> {connection}')
                    
                    res = _add_line(res, f'{object_type} {list_to_string(object.props)}')

                    if object_type == 'y': # specific case just for start
                        res = _add_line(res, 'bullet')

                    res = _add_line(res, f'< {object.id}')

        return res.strip()
    
    # TODO: object manipulation from the level class

"""/
/ circloO level
/ Made with circloO Level Editor v1.3
totalCircles 4 0
/ EDITOR_TOOL 1 
/ EDITOR_VIEW 2156.50 1833 0.80
/ EDT 4964
/ _SAVE_TIME_1708642659000_END
levelscriptVersion 5
COLORS 213
grav 1 270
y 1425 1560  1 1 1
bullet
< 0
ic 'i' 1655 1557 1 
< 1
l_at 1271 1721 1494 1911 2
< 2
ic 'i' 1294 1798 1 
< 3
c 1273.50 1726 11.945219039916992
< 4
/ LE_ARC_DESCRIPTION 1275.55 1892.66 45.76 236.31 118.18 2164 2373 2 2
/ SKIP 7
* 1
+ -224.45 392.66
repeatchp 45.76 81.82 84 -2
+* 0
chp 236.31 81.82
chmake_arc 0 2
=
< 5
mc 1273.50 1990.50 10.124228477478027 1 0
< 6
ic 'io' 1385 2063 1 
< 7
t 1719 2182 1400 2307 1677 2312
< 8
c 1772.50 2246.50 54.268043518066406
< 9
c 1861.50 2225 40.115459442138672
< 10
ic 'i' 1901 2146 1 
< 11
c 1109 1324 148.600128173828125
< 12
b 1640.50 1110 258.50 72 0
< 13
tmb 1908 1366 179 58 1 -1 0 -1 300 60 0
< 14"""


'''
indexes are actualy minus one
1 fixed circle -> c
2 fixed rectangle -> b
3 triangle -> t
4 line -> l_at
5 arc around center -> LE_ARC_DESCRIPTION
6 arc through 3 points -> LE_ARC_DESCRIPTION
7 bezier curve -> curve
8 growing circle -> gc
9 growing rectangle -> rGr
 
11 moveable circle -> mcG
10 moveable rectangle -> mb
12 moveable triangle -> mtG
13 superglue connection for movables (11>12) -> / GLUE a b

14 create a rope connection (2>11) -> r
15 create a pulley connection (12>10) -> p + / p_description
16 create a hinge connection (2>1) -> hinge
17 create a prismatic/slider connection (11>2) -> pr
18 create a rotatable rectangle -> rr
19 create a rotatable circle -> rc
20 create a springy rectangle -> wr (/ SKIP 3  c  mb  w *wr*)
21 create a ball generator -> tmc
22 create a box generator -> tmb
23 create a portal -> portal

24 start -> y + \n bullet
25 collectable -> ic 'i'
26 collectable on collision with other -> ic 'io'
27 collectable that changes gravity -> ic 'ig'
28 collectable on collision with other + change gravity -> ic 'im'
29 collectable that changes size of the player circle -> ic 'is'
30 collectable on collision + changes player circle size -> ic 'iso'
31 collectable that disconnects player connections -> ic 'irb'
32 collectable on collision + disconnects player connections -> ic 'irbo'
33 collectable that changes player circle speed -> ic 'ips'
34 collectable on collision + changes player circle speed -> ic 'ipso'
35 collectable special -> ic 'isp'
36 collectable on collision with other special -> ic 'ispo'
'''
'''
class OldLevel:
    headers = {}
    objects = []

    def __init__(self, headers, objects):
        self.headers = headers
        self.objects = objects

    @staticmethod
    def parse(s):
        # TODO: parse and stringify connections
        headers = {}
        objects = []

        lines = s.strip().split("\n")[3:] # first 3 lines are useless
        #temp_object = None
        temp_object = {}
        # {
        #    "type": '',
        #    "props": [],
        #    "connections": [], # only present in connections
        #    "id": 0
        # }

        # get the headers (first 8 lines)
        for header in lines[:8]:
            props = get_props(header)
            header_type = HEADER_TYPES.get(props[0])
            if header_type:
                header_name = header_type  # HEADER_TYPE_LOOKUP[props[0]] if HEADER_TYPE_LOOKUP[props[0]] else props[0]
                headers[header_name] = props[1:]

        lines = lines[HEADER_LINES:] # we dont need those headers anymore

        # get the objects
        lines_iter = iter(lines)
        for object in lines_iter:
            props = get_props(object)
            object_type = OBJECT_TYPES.get(props[0])
            if props[0] == '<':
                if temp_object is not None:
                    temp_object["id"] = int(props[1])
                    objects.append(temp_object)
                    temp_object = {}
                    #temp_object = None
            elif props[0] == '>':
                if not temp_object.get("connections"):
                    temp_object["connections"] = []
                temp_object["connections"].append(int(props[1]))
            elif props[0] == 'SKIP':
                skip_iters(lines_iter, int(props[1]))
            elif object_type is not None:
                temp_object["type"] = object_type
                temp_object["props"] = props[1:]
                #temp_object = {
                #    "type": object_type, # OBJECT_TYPE_LOOKUP[props[0]],
                #    "props": props[1:],
                #}

        return Level(headers, objects)
    
    def stringify(self):
        res = LEVEL_PREFIX

        def _add_line(str, line):
            return str + line + '\n'
        
        for key, value in self.headers.items():
            header = HEADER_TYPES.get_inv(key)
            if header:
                res = _add_line(res, f'{header} {list_to_string(value)}') # f'/ {header} {_list_to_string(value)}'

        for object in self.objects:
            if object.get("id") and object.get("type") and object.get("props"):
                object_type = OBJECT_TYPES.get_inv(object["type"]) # should add a check for a slash here
                if object_type:
                    if object.get("connections"):
                        for connection in object["connections"]:
                            res = _add_line(res, f'> {connection}')
                    
                    res = _add_line(res, f'{object_type} {list_to_string(object["props"])}')

                    if object_type == 'y': # specific case just for start
                        res = _add_line(res, 'bullet')

                    res = _add_line(res, f'< {object["id"]}')

        return res.strip()
'''