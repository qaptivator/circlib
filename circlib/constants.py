from .utils import Lookup

# ingame name to library name, just so fields would be more understandable
HEADER_TYPES = Lookup({
    "totalCircles": "totalCircles",
    "/ EDITOR_TOOL": "editorTool",
    "/ EDITOR_VIEW": "editorView",
    "/ EDT": "edit",
    "grav": "gravity",
    "levelscriptVersion": "levelscriptVersion",
    "COLORS": "colors"
})

# ingame type to library type, also acts as a whitelist for prefixes, like ignoring properties of an arc
OBJECT_TYPES = Lookup({
    "c": "fixed_circle",
    "b": "fixed_rectangle",
    "t": "triangle",
    "l_at": "line",
    "/ LE_ARC_DESCRIPTION": "arc",
    "curve": "bezier_curve",
    "gc": "growing_circle",
    "rGr": "growing_rectangle",

    "mcG": "movable_circle",
    "mb": "movable_rectangle",
    "mtG": "movable_triangle",
    "GLUE": "superglue_connection",

    "r": "rope_connection",
    "p": "pulley_connection",
    "hinge": "hinge_connection",
    "pr": "prismatic_connection",
    "rr": "rotatable_rectangle",
    "rc": "rotatable_circle",
    "wr": "springy_rectangle",
    "tmc": "ball_generator",
    "tmb": "box_generator", # is it supposed to be rectangle?
    "portal": "portal",

    "y": "start",
    "ic": "collectable", # there is actually a ton of types of collectables
    "spc": "special_connection"
})

COLLECTABLE_TYPES = Lookup({
    "i": "regular",
    "io": "regular_collision",
    "ig": "gravity",
    "im": "gravity_collision",
    "is": "size",
    "iso": "size_collision",
    "irb": "disconnect",
    "irbo": "disconnect_collision",
    "ips": "speed",
    "ipso": "speed_collision",
    "isp": "special",
    "ispo": "special_collision"
})

CONNECTIONS = [
    "superglue_connection",
    "rope_connection",
    "hinge_connection",
    "prismatic_connection",
    "special_connection"
]

#SLASH_LOOKUP = Lookup({
#    "LE_ARC_DESCRIPTION": "/ LE_ARC_DESCRIPTION",
#    "p_description": "/ p_description",
#    "EDITOR_TOOL": "/ EDITOR_TOOL"
#})

LEVEL_PREFIX = '''/
/ circloO level
/ Made with circloO Level Editor v1.3
'''

DEFAULT_HEADERS = {
    "totalCircles": ["7", "0"],
    "editorTool": ["0"],
    "editorView": ["2320", "1884", "1"],
    "edit": ["252"],
    "levelscriptVersion": ["5"],
    "colors": ["166"], # these are random
    "gravity": ["1", "270"]
}

# default level
'''/
/ circloO level
/ Made with circloO Level Editor v1.3
totalCircles 7 0
/ EDITOR_TOOL 0 
/ EDITOR_VIEW 2320 1884 1
/ EDT 252
/ _SAVE_TIME_1709037038000_END
levelscriptVersion 5
COLORS 166
grav 1 270'''

# amount of header lines
HEADER_LINES = 8