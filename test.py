#from circlib import Level

lvl = """/
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

craze = """/
/ circloO level
/ Made with circloO Level Editor v1.3
totalCircles 8 1
/ EDITOR_TOOL 0 
/ EDITOR_VIEW 2281 2415 1
/ EDT 24807
/ _SAVE_TIME_1708779801000_END
levelscriptVersion 6
COLORS 97
grav 1 270
gs 1392.42 1501.42 0
c 1266 1538 87.965904235839844
< 0
b 1563 1368 102 52 0
< 1
t 1628 1691 1720 1523 1830 1707
< 2
l_at 1216 1793 1483 1756 2
< 3
/ LE_ARC_DESCRIPTION 1500 1500 200.90 338.82 375.71 -1 -1 2 2
/ SKIP 7
* 1
+ 0 0
repeatchp 200.90 -175.71 111 -2
+* 0
chp 338.82 -175.71
chmake_arc 0 2
=
< 4
/ LE_ARC_DESCRIPTION 1786.73 1610.22 223.44 84.25 232.38 2393 1903 2 2
/ SKIP 7
* 1
+ 286.73 110.22
repeatchp 223.44 -32.38 69 -2
+* 0
chp 84.25 -32.38
chmake_arc 0 2
=
< 5
curve 2020 1748 2123.56 1600.95 1948.44 1430.05 2052 1283 2 100
< 6
gc 865 1559 87.321243286132812
< 7
rGr 1124 1393.50 152 18.50 0
< 8
mb 1427 1262.50 112 19.50 1 -1 0 -1
< 9
mcG 1445.50 1601.50 0 69.559326171875 1 0
< 10
mtG 1286 1346 1399 1381 1333 1477 1 0
< 11
rr 1098 1732.50 220 133 0 1 0
< 12
rc 1947.50 1331.50 100.262153625488281 0 100
< 13
/ SKIP 3
c 833.50 1415 10
mb 833.50 1415 99.50 9 1 -1 0
w 833.50 1415 0 2 0.30 0
wr 833.50 1415 99.50 9 0 1 2 0.30 0 10
< 14
tmc 1331 1700.50 48.541217803955078 1 300 60 0
< 15
tmb 2055 1580.50 132 19.50 1 -1 0 -1 300 60 0
< 16
portal 1650 1271 1824 1568 1 7 0
< 17
y 1175 2096  1 1 1
bullet
< 18
ic 'i' 1412 2096 1 
< 19
ic 'io' 1541 2081 1 
< 20
ic 'ig' 1667 2086 1  90 1
< 21
ic 'im' 1783 2081 1  90 1
< 22
ic 'is' 1723 2002 1  32.50
< 23
ic 'iso' 1353 2000 1  32.50
< 24
ic 'irb' 1046 1963 1 
< 25
ic 'irbo' 1184 1941 1 
< 26
ic 'ips' 1308 2217 1  1 -1
< 27
ic 'ipso' 1480 2240 1  1 -1
< 28
ic 'isp' 1632 2269 1 
< 29
ic 'ispo' 1705 2241 1 
< 30
> 2
> 10
r  0 0 0 0 0
< 31
> 11
> 9
p 0 -100 0 -100 1 53.33 55.33 0 0
/ p_description 0 0 0 0 0 -100 0 -100 1
< 32
> 1
> 0
hinge  0 0 0 0 0 100
< 33
> 10
> 1
pr 0.45 -0.89 -1 -1 0 0
< 34
/ GLUE 10 11
< 35
> 29
> 10
spc 'Follow'
< 36
> 30
> 16
spc 'On'
< 37
> 29
> 15
spc 'Off'
< 38
"""

#lvl_obj = Level.parse(craze)
#print(lvl_obj.stringify())
#print(type(lvl_obj.objects[0].id))
#new_level = Level()
# b x1563 y1368 w102 h52 r0
# x and y differ from ingame
# width and height are two times smaller in file than in game
#new_level.create_object("fixed_rectangle", ["1563", "1368", "102", "52", "0"])
#f = new_level.create_object("fixed_rectangle", ["1363", "1330", "10", "200", "15"]) # ingame: 2173 1514 20 400 15
#new_level.create_object("rope_connection", ["0", "0", "0", "0", "0"], ["0", "1"])
#print(new_level.stringify())
#new_level.remove_object_by_id(2)
#print(new_level.stringify())
# b1   x1563 y1368 w102 h52 r0   ->   x2281 y1700 w204 h104  718 332
# b2   x1424 y1300 w103 h40 r0   ->   x2414 y1644 w206 h80   990 344