'''
Place to store functions to create control curves

'''

#Create partial box for tail controls
###May need to add snapping ivot point to center###
def create_trail_control_box():
	cmds.curve(d = 1, p = [(-1, 2, 0), (-1, 0, 0), (1, 0, 0), (1, 2, 0), (1, 2, -2), (-1, 2, -2), (-1, 2, 0), (-1, 0, 0), (-1, 0, -2), (1, 0, -2), (1, 0, 0), (1, 2, 0), (-1, 2, 0)], k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

#Create full box
###May need to add snapping ivot point to center###
def createBox():
	cmds.curve(d = 1, p = [(-1, 2, 0), (-1, 0, 0), (1, 0, 0), (1, 2, 0), (1, 2, -2), (1, 0, -2), (-1, 0, -2), (-1, 2, -2), (-1, 2, 0), (-1, 0, 0), (-1, 0, -2), (-1, 2, -2), (1, 2, -2), (1, 0, -2), (1, 0, 0), (1, 2, 0), (-1, 2, 0)], k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

