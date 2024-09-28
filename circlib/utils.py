import json
import re
from dataclasses import dataclass

def print_dict(d):
    print(json.dumps(d, sort_keys=True, indent=4))

def get_props(line: str) -> list[str]: # get props from line
    #line = line.strip()
    #if not header: 
    #    continue
    #if line.startswith('/'):
    #    line = line[2:]
    res = list(filter(None, line.split(' ')))
    if res[0] == '/':
        new_prefix = '/ ' + res[1] # create new prefix ['/', 'EDT', '123'] -> '/ EDT'
        res[1] = new_prefix # change second element ['/', 'EDT', '123'] -> ['/', '/ EDT', '123']
        res = res[1:] # remove first element ['/', '/ EDT', '123'] -> ['/ EDT', '123']
    return res

def skip_iters(iter: iter, n: int = 1):
    for _ in range(n):
        next(iter)

def inv_map(m: dict[any, any]) -> dict[any, any]:
    return {v: k for k, v in m.items()}

#def is_numeric(v):
#    return re.match(r'^-?\d+\.?\d*$', v) is not None

#def is_string(v):
#    return not is_numeric(v)

@dataclass
class LineOptions:
    code: str # the code (first string)
    numerics: list[int | float] # numeric arguments of the line
    strings: list[str] # string arguments of the line, doesnt include the code and the comment
    raw: list[str | int | float] # raw, separated by space, arguments of the line
    is_comment: bool = False # does this line start with a '/'

def to_numeric(v):
    try:
        return int(v)
    except ValueError:
        try:
            return float(v)
        except ValueError:
            return v
        
def is_numeric(v):
    return isinstance(to_numeric(v), (int, float))

def is_string(v):
    return not is_numeric(v)

def sanitize_line(line: str) -> LineOptions:
        numerics = []
        strings = []
        code = ""
        is_comment = False
        raw = ""
    
        args = line.strip().split()
        for arg in args:
            if is_string(arg):
                strings.append(arg)
            elif is_numeric(arg):
                numerics.append(to_numeric(arg))

        raw = args

        if len(strings) >= 1:
            if strings[0] == '/':
                is_comment = True
                strings = strings[1:]
            if len(strings) >= 1:
                code = strings[0]

        return LineOptions(code, numerics, strings, raw, is_comment)

class Vector2:
    x: float = 0
    y: float = 0
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y


def string_to_value(v):
    v = str(v)
    try:
        num = int(v)
        return num
    except ValueError:
        try:
            num = float(v)
            return num
        except ValueError:
            if v.startswith("'") and v.endswith("'"):
                return v[1:-1]
            else:
                return v

def value_to_string(v):
    v = string_to_value(v)
    if isinstance(v, int) or isinstance(v, float):
        return str(v)
    else:
        if (v.startswith("'") and v.endswith("'")) or v.startswith("\n"):
            return v
        else:
            return f"'{v}'"

def list_to_string(list):
    #return ' '.join(list)
    res = ''
    for el in list:
        res += value_to_string(el) + ' '
    return res.strip()

def string_to_list(props):
    return list(map(lambda el: string_to_value(el), props))

def ingame_to_level_x(x):
    return x - 820

def ingame_to_level_y(y):
    return y - 384

def next_avaiable_id(m):
    max_id = -1 # if the starting index is 0
    for v in m:
        if v.id > max_id:
            max_id = v.id
    return max_id + 1

class Lookup:
    table = {}
    table_inv = {}
    def __init__(self, m: dict[any, any]):
        self.table = m
        self.table_inv = inv_map(m)
    def get(self, key: any, default: any = None) -> any:
        return self.table.get(key, default)
    def get_inv(self, key: any, default: any = None) -> any:
        return self.table_inv.get(key, default)
