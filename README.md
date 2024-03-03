# circlib

Python library for creating and editing CircloO levels
Currently the library isn't hosted on PyPi, so instead, just clone the repository and then extract the `circlib` folder.
`git clone https://github.com/qaptivator/circlib.git`

# Usage

Here are some examples of how you can use this library.
You can parse an arleady existing level:

```py
from circlib import Level

level = Level.parse('your level string')
level.create_object("fixed_rectangle", ["1563", "1368", "102", "52", "0"])
print(level.stringify())
```

Or create a new one from scratch:

```py
level = Level()
level.create_object("fixed_rectangle", ["1500", "1300", "50", "50", "45"])
```

**Note:** strings which are not numbers in the properties of the object automatically get surrounded by '' (quotes). It does not happen when you add a newline to the start of the prop, for example: `\nnoanim`. This can be used for multi-line properties like forementioned `noanim`, or for trigger collectibles like `trigger`.

# API

## class Level

- Level.headers -- Headers of the level. For example: color, gravity, total circles. It is a dictionary.
- Level.objects -- Objects of the level. Not recommended to change it manually, use the provided methods instead. It is a list of Object class instances.

- Level.parse(str) -- A static method. Create a new level by parsing level's string. Returns a new Level object with all the headers and objects.
- Level.stringify() -- Returns the stringified version of the level, which can be imported in-game.
- Level.get_object_by_id(id) -- Returns an object with matching it. Be aware that in CircloO levels, ids are numbers, not strings.
- Level.get_object_by_type(type) -- Returns every object with matching type. See all types in the further section.
- Level.create_object(type, props, connections?) -- Creates a new object and returns it. Type and props are necessary, but connections is only needed for connectable objects, like ropes.
- Level.remove_object(object) -- Removes an object by giving it an Object instance.
- Level.remove_object_by_id(id) - Removes an object which matches the id.

## class Object

- Object. id -- Object's integer id, not a string.
- Object.type -- Object's type as a string. See all types in the further section.
- Object.props -- Array of every object's prop. It is stuff like position or rotation. P.S. there isn't any documentation of every prop of every object.
- Object.get_connections() -- Returns every connection of the object, such as two objects connected by a rope. If the object isn't an connectable, it throws an error.

## Object types

Format: object type -> corresponding type in the level's text file

- fixed_circle -> c
- fixed_rectangle -> b
- triangle -> t
- line -> l_at
- arc -> / LE_ARC_DESCRIPTION
- bezier_curve -> curve
- growing_circle -> gc
- growing_rectangle -> rGr
- movable_circle -> mcG
- movable_rectangle -> mb
- movable_triangle -> mtG
- superglue_connection -> GLUE
- rope_connection -> r
- pulley_connection -> p
- hinge_connection -> hinge
- prismatic_connection -> pr
- rotatable_rectangle -> rr
- rotatable_circle -> rc
- springy_rectangle -> wr
- ball_generator -> tmc
- box_generator -> tmb
- portal -> portal
- start -> y
- collectable -> ic
- special_connection -> spc

## Header types

- totalCircles -> totalCircles
- editorTool -> / EDITOR_TOOL
- editorView -> / EDITOR_VIEW
- edit -> / EDT
- gravity -> grav
- levelscriptVersion -> levelscriptVersion
- colors -> COLORS

## Collectable types

- regular -> i
- regular_collision -> io
- gravity -> ig
- gravity_collision -> im
- size -> is
- size_collision -> iso
- disconnect -> irb
- disconnect_collision -> irbo
- speed -> ips
- speed_collision -> ipso
- special -> isp
- special_collision -> ispo
