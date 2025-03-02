import json

objectDepths = [None] * 66
objectDepths[0] = -10
objectDepths[1] = 9000
objectDepths[2] = -20
objectDepths[3] = 0
objectDepths[4] = 0
objectDepths[5] = 1
objectDepths[6] = -10
objectDepths[7] = 0
objectDepths[8] = 0
objectDepths[9] = 0
objectDepths[10] = 0
objectDepths[11] = 100
objectDepths[12] = -10000
objectDepths[13] = 0
objectDepths[14] = 0
objectDepths[15] = 0
objectDepths[16] = 0
objectDepths[17] = 0
objectDepths[18] = 0
objectDepths[19] = 0
objectDepths[20] = 0
objectDepths[21] = 10
objectDepths[22] = 10
objectDepths[23] = 10
objectDepths[24] = 10
objectDepths[25] = 0
objectDepths[26] = 0
objectDepths[27] = 0
objectDepths[28] = 0
objectDepths[29] = 0
objectDepths[30] = 0
objectDepths[31] = 0
objectDepths[32] = 0
objectDepths[33] = 0
objectDepths[34] = -1
objectDepths[35] = 15
objectDepths[36] = 15
objectDepths[37] = 15
objectDepths[38] = 15
objectDepths[39] = 15
objectDepths[40] = 15
objectDepths[41] = 0
objectDepths[42] = 0
objectDepths[43] = 0
objectDepths[44] = 0
objectDepths[45] = 0
objectDepths[46] = 0
objectDepths[47] = 0
objectDepths[48] = 0
objectDepths[49] = 0
objectDepths[50] = 0
objectDepths[51] = 0
objectDepths[52] = 0
objectDepths[53] = 0
objectDepths[54] = 0
objectDepths[55] = 9000
objectDepths[56] = 0
objectDepths[57] = 0
objectDepths[58] = 0
objectDepths[59] = 0
objectDepths[60] = 0
objectDepths[61] = 0
objectDepths[62] = 0
objectDepths[63] = 0
objectDepths[64] = 0
objectDepths[65] = 0

objectNames = [None] * 66
objectNames[0] = "obj_menu"
objectNames[1] = "obj_createbigcircle"
objectNames[2] = "obj_renderer"
objectNames[3] = "obj_createlevel"
objectNames[4] = "obj_gameflowhandler"
objectNames[5] = "obj_levelguihandler"
objectNames[6] = "obj_notification"
objectNames[7] = "obj_waitabit"
objectNames[8] = "obj_musichandler"
objectNames[9] = "obj_blackscreen"
objectNames[10] = "obj_hintgetter"
objectNames[11] = "obj_hintshower"
objectNames[12] = "obj_showrotatewarning"
objectNames[13] = "obj_gamestarter"
objectNames[14] = "obj_ratemanager"
objectNames[15] = "obj_ads"
objectNames[16] = "obj_screenshotter"
objectNames[17] = "obj_leveltimes"
objectNames[18] = "obj_autoscreenshotter"
objectNames[19] = "obj_recorder"
objectNames[20] = "obj_you"
objectNames[21] = "obj_collectcircle"
objectNames[22] = "obj_collectcircle_gravitychange"
objectNames[23] = "obj_collectcircle_other"
objectNames[24] = "obj_collectcircle_multi"
objectNames[25] = "obj_collectcircle_creator"
objectNames[26] = "obj_physicsinstance_mc"
objectNames[27] = "obj_physicsinstance_mc_timed"
objectNames[28] = "obj_creator_mc_timed"
objectNames[29] = "obj_linemanager"
objectNames[30] = "obj_physicsinstance_triangle"
objectNames[31] = "obj_physicsinstance_triangle_mc"
objectNames[32] = "obj_physicsinstance_block"
objectNames[33] = "obj_physicsinstance_block_mc"
objectNames[34] = "obj_chainmanager"
objectNames[35] = "obj_ropejointmanager"
objectNames[36] = "obj_pulleyjointmanager"
objectNames[37] = "obj_distancejointmanager"
objectNames[38] = "obj_frictionjointmanager"
objectNames[39] = "obj_weldjointmanager"
objectNames[40] = "obj_prismaticjointmanager"
objectNames[41] = "obj_anyphyobject"
objectNames[42] = "obj_physicsinstance_moveable"
objectNames[43] = "obj_block_rotate"
objectNames[44] = "obj_connectsomethingtothis"
objectNames[45] = "obj_physicsinstance"
objectNames[46] = "obj_vanisher"
objectNames[47] = "obj_multifixtureinstance"
objectNames[48] = "obj_test_softbodies"
objectNames[49] = "solidsurfaces"
objectNames[50] = "obj_zoomout"
objectNames[51] = "obj_splash"
objectNames[52] = "obj_splash_armor"
objectNames[53] = "obj_splash_coolmath"
objectNames[54] = "obj_leveleditor"
objectNames[55] = "obj_le_drawmaincircles"
objectNames[56] = "obj_le_viewhandler"
objectNames[57] = "obj_le_gui"
objectNames[58] = "obj_le_edittool"
objectNames[59] = "obj_le_exporter"
objectNames[60] = "obj_le_par_levelelement"
objectNames[61] = "obj_le_circle"
objectNames[62] = "obj_le_rectangle"
objectNames[63] = "obj_le_triangle"
objectNames[64] = "obj_le_collectcircle"
objectNames[65] = "obj_musicresumer"

# i hate python for this
objectId2Depth = [None] * len(objectDepths)
objectInfos = []
objectId2Name = [None] * len(objectDepths)

for id, depth in enumerate(objectDepths):
    if id >= 0:
        objectId2Depth[id] = depth
        name = objectNames[id]
        if name:
            objectId2Name[id] = name
            objectInfos.append({
                "id": id,
                "name": name,
                "depth": depth,
            })

#print(json.dumps(objectInfos, indent=4))

with open('objects.json', 'w') as f:
    f.write(json.dumps(objectInfos, indent=4))