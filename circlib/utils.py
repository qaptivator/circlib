import json
import re

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

def is_numeric(v):
    return re.match(r'^-?\d+\.?\d*$', v) is not None

def value_to_string(value):
    if is_numeric(value): # isnumeric() and isdigit() doesn't work with fractions and negatives
        return f"{value}"
    else:
        if value.startswith("'") and value.endswith("'"):
            return value
        else:
            return f"'{value}'"

def prop_to_value(value):
    #if is_numeric(value):
    #    return float(value)
    #else:
    #    return value
    if value.isdigit():
        return int(value)
    elif value.replace('.', '', 1).isdigit(): 
        return float(value)
    else:
        return value

def list_to_string(list):
    #return ' '.join(list)
    res = ''
    for el in list:
        res += value_to_string(f"{el}") + ' '
        #if el.isnumeric():
        #    res += f"{el} "
        #else:
        #    res += el + ' ' # f"'{el}'"
    return res.strip()

def props_to_list(props):
    return list(map(lambda el: prop_to_value(el), props))

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