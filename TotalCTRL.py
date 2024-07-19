'''
TotalCTRL ver 1.0 by href
Release Date 19/07/2024
 
INSTALLATION:
1. Put TotalCTRL_icons folder into Documents\maya\20xx\scripts
2. Add this script to shelve or run from script editor(Python)
'''

import maya.cmds as mc
import maya.mel as mel
import sys
from decimal import Decimal, getcontext

def createWin():
    if mc.window('customWin', exists= True):
       mc.deleteUI('customWin')

    window = mc.window('customWin', title= 'Total CTRL', minimizeButton= False, maximizeButton= False, sizeable= False)

    # UI __________________________________________________________________________________________
    mc.columnLayout(adj= True)

    # Curve Icon __________________________________________________________________________________
    cH0 = mc.columnLayout (adj= True, w= 200)
    cH1 = mc.columnLayout (adj= True, w= 200)
    frameEdit = mc.frameLayout(l= 'Curve Shape', cll= 1, cl= 0, bgc= [0.15, 0.15, 0.15])

    mc.rowColumnLayout ( numberOfColumns=5)

    imagecButton01 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton01.png'
    imagecButton02 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton02.png'
    imagecButton03 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton03.png'
    imagecButton04 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton04.png'
    imagecButton05 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton05.png'
    imagecButton06 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton06.png'
    imagecButton07 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton07.png'
    imagecButton08 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton08.png'
    imagecButton09 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton09.png'
    imagecButton10 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton10.png'
    imagecButton11 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton11.png'
    imagecButton12 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton12.png'
    imagecButton13 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton13.png'
    imagecButton14 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton14.png'
    imagecButton15 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton15.png'
    imagecButton16 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton16.png'
    imagecButton17 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton17.png'
    imagecButton18 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton18.png'
    imagecButton19 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton19.png'
    imagecButton20 = mc.internalVar(usd= True) + 'TotalCTRL_icons/cButton20.png'

    # Curve Button _________________________________________________________________________________
    CButton01 = mc.symbolButton( image= imagecButton01, width=40, height=40, c= 'CCircle()')
    CButton02 = mc.symbolButton( image= imagecButton02, width=40, height=40, c= 'CSquare()')
    CButton03 = mc.symbolButton( image= imagecButton03, width=40, height=40, c= 'CTriangle()')
    CButton04 = mc.symbolButton( image= imagecButton04, width=40, height=40, c= 'CCross()')
    CButton05 = mc.symbolButton( image= imagecButton05, width=40, height=40, c= 'CCube()')
    CButton06 = mc.symbolButton( image= imagecButton06, width=40, height=40, c= 'CCog()')
    CButton07 = mc.symbolButton( image= imagecButton07, width=40, height=40, c= 'CArrow1()')
    CButton08 = mc.symbolButton( image= imagecButton08, width=40, height=40, c= 'CArrow2()')
    CButton09 = mc.symbolButton( image= imagecButton09, width=40, height=40, c= 'CArrow4()')
    CButton10 = mc.symbolButton( image= imagecButton10, width=40, height=40, c= 'CPyramid()')
    CButton11 = mc.symbolButton( image= imagecButton11, width=40, height=40, c= 'CLocator()')
    CButton12 = mc.symbolButton( image= imagecButton12, width=40, height=40, c= 'CLolipop()')
    CButton13 = mc.symbolButton( image= imagecButton13, width=40, height=40, c= 'CStar()()')
    CButton14 = mc.symbolButton( image= imagecButton14, width=40, height=40, c= 'CRhombus()')
    CButton15 = mc.symbolButton( image= imagecButton15, width=40, height=40, c= 'CSphere()')
    CButton16 = mc.symbolButton( image= imagecButton16, width=40, height=40, c= 'CEyesSet()')
    CButton17 = mc.symbolButton( image= imagecButton17, width=40, height=40, c= 'CBridge()')
    CButton18 = mc.symbolButton( image= imagecButton18, width=40, height=40, c= 'CCurve()')
    CButton19 = mc.symbolButton( image= imagecButton19, width=40, height=40, c= 'EPCurve()')
    CButton20 = mc.symbolButton( image= imagecButton20, width=40, height=40, c= PolyToCurve_degree1)
    
  
    PolyToCurvePopup = mc.popupMenu(parent= CButton20, button= 3)
    mc.menuItem(l= '1 Linear', parent= PolyToCurvePopup, c= PolyToCurve_degree1)
    mc.menuItem(l= '2', parent= PolyToCurvePopup, c= PolyToCurve_degree2)
    mc.menuItem(l= '3 Cubie', parent= PolyToCurvePopup, c= PolyToCurve_degree3)
    mc.menuItem(l= '5', parent= PolyToCurvePopup, c= PolyToCurve_degree5)
    mc.menuItem(l= '7', parent= PolyToCurvePopup, c= PolyToCurve_degree7)


    mc.setParent(cH1)

    # Color Button ________________________________________________________________________ 
    cH2 = mc.columnLayout(adj= True)
    frameEdit = mc.frameLayout(l= 'Assign Color', cll= 1, cl= 0, bgc= [0.15, 0.15, 0.15])
    mc.separator(h= 1, style= 'double')
    
    mc.gridLayout('gridLayout', numberOfColumns = 8, cellWidthHeight = (25, 25))
    for i in range(1, 32):
        mc.button(label= '', command=lambda _, idx= i: SetColor(idx), backgroundColor= mc.colorIndex(i, query= True))
        
    # Custom color
    mc.button(label= '?', command = 'SetRGB()', height= 20)

    mc.setParent(cH2)

    # Other ____________________________________________________________________________
    
    cH3 = mc.columnLayout(adj= True, w= 200)

    frameEdit = mc.frameLayout(l= 'Other', cll= 1, cl= 0, bgc= [0.15, 0.15, 0.15])
    mc.separator(h= 1, style= 'double')
    cH4 = mc.rowColumnLayout (numberOfColumns= 1)
    mc.rowColumnLayout(nc= 3)
    mc.button(l= 'Combine Curves', h=40,w=93, c= 'CombineCurves()')
    mc.text(l= '')
    
    
    BswapCurve = mc.button(l= 'Swap Curve  [ ]',h= 40,w= 93)
    
    swapCurvePopup = mc.popupMenu(parent= BswapCurve, button= 3)
    mc.menuItem(l= 'Keep Curve', command= lambda *args: SwapCurve(keepCurve= True))
    
    mc.button(BswapCurve, edit= True, command= lambda *args: SwapCurve(keepCurve= False))
    
    mc.text(l= '', h= 6)
    mc.text(l= '', h= 6)
    mc.text(l= '', h= 6)
    mc.button(l= 'Create Offset', h= 40, w= 93, c= 'CreateOffsetGroup()')
    mc.text(l= '')
    mc.button(l= 'Get Curve Attr.', h= 40, w= 93, c= 'GetCurveAttr()')
    mc.setParent(cH4)

    mc.separator(h= 5, style= 'none')
   
    mc.setParent(cH3)
    mc.separator(h= 1, style= 'in')
    
    mc.text(l= 'ver 1.0 ', align= 'right')
    mc.setParent(cH0)

    mc.showWindow(window)

# Curve Button ___________________________________________________________________
def CCircle():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.circle(nr= [0,1,0])

    else:    
        selected_objects = mc.ls(selection= True)
        target = selected_objects[0]
        objectPrim = mc.circle(nr= [0,1,0])
        mc.parentConstraint(target, objectPrim, maintainOffset= False)
        mc.parentConstraint(target, objectPrim, e= True, rm= True)

def CSquare():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.curve(p=[[-1.0, 0.0, -1.0], [-1.0, 0.0, 1.0], [1.0, 0.0, 1.0], [-1.0, 0.0, 1.0], [-1.0, 0.0, -1.0], [1.0, 0.0, -1.0], [1.0, 0.0, 1.0], [1.0, 0.0, -1.0]], d=1)

    else:    
        selected_objects = mc.ls(selection=True)
        target = selected_objects[0]
        objectPrim = mc.curve(p=[[-1.0, 0.0, -1.0], [-1.0, 0.0, 1.0], [1.0, 0.0, 1.0], [-1.0, 0.0, 1.0], [-1.0, 0.0, -1.0], [1.0, 0.0, -1.0], [1.0, 0.0, 1.0], [1.0, 0.0, -1.0]], d=1)
        mc.parentConstraint(target, objectPrim, maintainOffset= False)
        mc.parentConstraint(target, objectPrim, e= True, rm= True)

def CTriangle():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.curve(p=[[0.0, 0.0, -2.291], [2.015, 0.0, 1.222], [-2.015, 0.0, 1.222], [0.0, 0.0, -2.291], [-2.015, 0.0, 1.222]], d=1)

    else:    
        selected_objects = mc.ls(selection= True)
        target = selected_objects[0]
        objectPrim = mc.curve(p=[[0.0, 0.0, -2.291], [2.015, 0.0, 1.222], [-2.015, 0.0, 1.222], [0.0, 0.0, -2.291], [-2.015, 0.0, 1.222]], d=1)
        mc.parentConstraint(target, objectPrim, maintainOffset= False)
        mc.parentConstraint(target, objectPrim, e= True, rm= True)

def CCross():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.curve(p=[[-0.64, -2.56, 0.0], [-0.64, -0.64, 0.0], [-2.56, -0.64, 0.0], [-2.56, 0.64, 0.0], [-0.64, 0.64, 0.0], [-0.64, 2.56, 0.0], [0.64, 2.56, 0.0], [0.64, 0.64, 0.0], [2.56, 0.64, 0.0], [2.56, -0.64, 0.0], [0.64, -0.64, 0.0], [0.64, -2.56, 0.0], [-0.64, -2.56, 0.0]], d=1)

    else:    
        selected_objects = mc.ls(selection= True)
        target = selected_objects[0]
        objectPrim = mc.curve(p=[[-0.64, -2.56, 0.0], [-0.64, -0.64, 0.0], [-2.56, -0.64, 0.0], [-2.56, 0.64, 0.0], [-0.64, 0.64, 0.0], [-0.64, 2.56, 0.0], [0.64, 2.56, 0.0], [0.64, 0.64, 0.0], [2.56, 0.64, 0.0], [2.56, -0.64, 0.0], [0.64, -0.64, 0.0], [0.64, -2.56, 0.0], [-0.64, -2.56, 0.0]], d=1)
        mc.parentConstraint(target, objectPrim, maintainOffset= False)
        mc.parentConstraint(target, objectPrim, e= True, rm= True)

def CStar():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.curve(p=[[0.0, 0.0, -3.0], [-0.577, 0.0, -0.577], [-3.0, 0.0, 0.0], [-0.577, 0.0, 0.577], [0.0, 0.0, 3.0], [0.577, 0.0, 0.577], [3.0, 0.0, 0.0], [0.577, 0.0, -0.577], [0.0, 0.0, -3.0]], d=1)

    else:    
        selected_objects = mc.ls(selection= True)
        target = selected_objects[0]
        objectPrim = mc.curve(p=[[0.0, 0.0, -3.0], [-0.577, 0.0, -0.577], [-3.0, 0.0, 0.0], [-0.577, 0.0, 0.577], [0.0, 0.0, 3.0], [0.577, 0.0, 0.577], [3.0, 0.0, 0.0], [0.577, 0.0, -0.577], [0.0, 0.0, -3.0]], d=1)
        mc.parentConstraint(target, objectPrim, maintainOffset= False)
        mc.parentConstraint(target, objectPrim, e= True, rm= True)

def CLolipop():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.curve(p=[[0.0, 0.0, 0.0], [0.0, 3.083, 0.0], [0.0, 3.089, 0.097], [0.0, 3.113, 0.188], [0.0, 3.15, 0.279], [0.0, 3.198, 0.358], [0.0, 3.259, 0.431], [0.0, 3.332, 0.492], [0.0, 3.417, 0.541], [0.0, 3.502, 0.577], [0.0, 3.593, 0.601], [0.0, 3.691, 0.607], [0.0, 3.788, 0.601], [0.0, 3.879, 0.577], [0.0, 3.964, 0.541], [0.0, 4.049, 0.492], [0.0, 4.122, 0.431], [0.0, 4.183, 0.358], [0.0, 4.231, 0.279], [0.0, 4.268, 0.188], [0.0, 4.292, 0.097], [0.0, 4.298, 0.0], [0.0, 4.292, -0.097], [0.0, 4.268, -0.188], [0.0, 4.231, -0.279], [0.0, 4.183, -0.358], [0.0, 4.122, -0.431], [0.0, 4.049, -0.492], [0.0, 3.964, -0.541], [0.0, 3.879, -0.577], [0.0, 3.788, -0.601], [0.0, 3.691, -0.607], [0.0, 3.593, -0.601], [0.0, 3.502, -0.577], [0.0, 3.417, -0.541], [0.0, 3.332, -0.492], [0.0, 3.259, -0.431], [0.0, 3.198, -0.358], [0.0, 3.15, -0.279], [0.0, 3.113, -0.188], [0.0, 3.113, -0.188], [0.0, 3.089, -0.097], [0.0, 3.083, 0.0]], d=1)

    else:    
        selected_objects = mc.ls(selection= True)
        target = selected_objects[0]
        objectPrim = mc.curve(p=[[0.0, 0.0, 0.0], [0.0, 3.083, 0.0], [0.0, 3.089, 0.097], [0.0, 3.113, 0.188], [0.0, 3.15, 0.279], [0.0, 3.198, 0.358], [0.0, 3.259, 0.431], [0.0, 3.332, 0.492], [0.0, 3.417, 0.541], [0.0, 3.502, 0.577], [0.0, 3.593, 0.601], [0.0, 3.691, 0.607], [0.0, 3.788, 0.601], [0.0, 3.879, 0.577], [0.0, 3.964, 0.541], [0.0, 4.049, 0.492], [0.0, 4.122, 0.431], [0.0, 4.183, 0.358], [0.0, 4.231, 0.279], [0.0, 4.268, 0.188], [0.0, 4.292, 0.097], [0.0, 4.298, 0.0], [0.0, 4.292, -0.097], [0.0, 4.268, -0.188], [0.0, 4.231, -0.279], [0.0, 4.183, -0.358], [0.0, 4.122, -0.431], [0.0, 4.049, -0.492], [0.0, 3.964, -0.541], [0.0, 3.879, -0.577], [0.0, 3.788, -0.601], [0.0, 3.691, -0.607], [0.0, 3.593, -0.601], [0.0, 3.502, -0.577], [0.0, 3.417, -0.541], [0.0, 3.332, -0.492], [0.0, 3.259, -0.431], [0.0, 3.198, -0.358], [0.0, 3.15, -0.279], [0.0, 3.113, -0.188], [0.0, 3.113, -0.188], [0.0, 3.089, -0.097], [0.0, 3.083, 0.0]], d=1)
        mc.parentConstraint(target, objectPrim, maintainOffset= False)
        mc.parentConstraint(target, objectPrim, e= True, rm= True)

def CArrow1():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.curve(p=[[-0.0, 0.0, -4.0], [2.0, 0.0, -1.0], [1.0, 0.0, -1.0], [1.0, -0.0, 3.0], [-1.0, -0.0, 3.0], [-1.0, 0.0, -1.0], [-2.0, 0.0, -1.0], [-0.0, 0.0, -4.0]], d=1)
    else:    
        selected_objects = mc.ls(selection=True)
        target = selected_objects[0]
        objectPrim = mc.curve(p=[[-0.0, 0.0, -4.0], [2.0, 0.0, -1.0], [1.0, 0.0, -1.0], [1.0, -0.0, 3.0], [-1.0, -0.0, 3.0], [-1.0, 0.0, -1.0], [-2.0, 0.0, -1.0], [-0.0, 0.0, -4.0]], d=1)
        mc.parentConstraint(target, objectPrim, maintainOffset= False)
        mc.parentConstraint(target, objectPrim, e= True, rm= True)

def CArrow2():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.curve(p=[[0.0, 0.0, -6.0], [-2.0, 0.0, -3.0], [-1.0, 0.0, -3.0], [-1.0, 0.0, 3.0], [-2.0, 0.0, 3.0], [0.0, 0.0, 6.0], [2.0, 0.0, 3.0], [1.0, 0.0, 3.0], [1.0, 0.0, -3.0], [2.0, 0.0, -3.0], [0.0, 0.0, -6.0]], d=1)

    else:    
        selected_objects = mc.ls(selection= True)
        target = selected_objects[0]
        objectPrim = mc.curve(p=[[0.0, 0.0, -6.0], [-2.0, 0.0, -3.0], [-1.0, 0.0, -3.0], [-1.0, 0.0, 3.0], [-2.0, 0.0, 3.0], [0.0, 0.0, 6.0], [2.0, 0.0, 3.0], [1.0, 0.0, 3.0], [1.0, 0.0, -3.0], [2.0, 0.0, -3.0], [0.0, 0.0, -6.0]], d=1)
        mc.parentConstraint(target, objectPrim, maintainOffset= False)
        mc.parentConstraint(target, objectPrim, e= True, rm= True)

def CArrow4():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.curve(p=[[-0.0, 0.0, -43.11], [-14.37, 0.0, -23.95], [-4.79, 0.0, -23.95], [-4.79, 0.0, -4.79], [-23.95, 0.0, -4.79], [-23.95, 0.0, -14.37], [-43.11, 0.0, 0.0], [-23.95, 0.0, 14.37], [-23.95, 0.0, 4.79], [-4.79, 0.0, 4.79], [-4.79, 0.0, 23.95], [-14.37, 0.0, 23.95], [-0.0, 0.0, 43.11], [14.37, 0.0, 23.95], [4.79, 0.0, 23.95], [4.79, 0.0, 4.79], [23.95, 0.0, 4.79], [23.95, 0.0, 14.37], [43.11, 0.0, -0.0], [23.95, 0.0, -14.37], [23.95, 0.0, -4.79], [4.79, 0.0, -4.79], [4.79, 0.0, -23.95], [14.37, 0.0, -23.95], [-0.0, 0.0, -43.11]], d=1)

    else:    
        selected_objects = mc.ls(selection= True)
        target = selected_objects[0]
        objectPrim = mc.curve(p=[[-0.0, 0.0, -43.11], [-14.37, 0.0, -23.95], [-4.79, 0.0, -23.95], [-4.79, 0.0, -4.79], [-23.95, 0.0, -4.79], [-23.95, 0.0, -14.37], [-43.11, 0.0, 0.0], [-23.95, 0.0, 14.37], [-23.95, 0.0, 4.79], [-4.79, 0.0, 4.79], [-4.79, 0.0, 23.95], [-14.37, 0.0, 23.95], [-0.0, 0.0, 43.11], [14.37, 0.0, 23.95], [4.79, 0.0, 23.95], [4.79, 0.0, 4.79], [23.95, 0.0, 4.79], [23.95, 0.0, 14.37], [43.11, 0.0, -0.0], [23.95, 0.0, -14.37], [23.95, 0.0, -4.79], [4.79, 0.0, -4.79], [4.79, 0.0, -23.95], [14.37, 0.0, -23.95], [-0.0, 0.0, -43.11]], d=1)
        mc.parentConstraint(target, objectPrim, maintainOffset= False)
        mc.parentConstraint(target, objectPrim, e= True, rm= True)

def CCog():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.curve(p=[[0.425, 0.0, -5.647], [0.0, 0.0, -6.254], [-0.425, 0.0, -5.647], [-0.607, 0.0, -5.222], [-0.971, 0.0, -4.736], [-1.396, 0.0, -4.372], [-2.004, 0.0, -4.372], [-2.55, 0.0, -4.554], [-2.975, 0.0, -4.797], [-3.643, 0.0, -5.039], [-3.643, 0.0, -4.311], [-3.582, 0.0, -3.825], [-3.582, 0.0, -3.279], [-3.704, 0.0, -2.732], [-4.189, 0.0, -2.368], [-4.736, 0.0, -2.186], [-5.222, 0.0, -2.125], [-5.89, 0.0, -1.943], [-5.525, 0.0, -1.336], [-5.161, 0.0, -0.971], [-4.797, 0.0, -0.546], [-4.614, 0.0, 0.0], [-4.797, 0.0, 0.546], [-5.161, 0.0, 0.971], [-5.525, 0.0, 1.336], [-5.89, 0.0, 1.943], [-5.222, 0.0, 2.125], [-4.736, 0.0, 2.186], [-4.189, 0.0, 2.368], [-3.704, 0.0, 2.672], [-3.582, 0.0, 3.218], [-3.582, 0.0, 3.825], [-3.643, 0.0, 4.311], [-3.643, 0.0, 5.039], [-2.975, 0.0, 4.797], [-2.55, 0.0, 4.554], [-2.004, 0.0, 4.372], [-1.396, 0.0, 4.372], [-0.971, 0.0, 4.736], [-0.668, 0.0, 5.161], [-0.425, 0.0, 5.647], [0.0, 0.0, 6.193], [0.425, 0.0, 5.647], [0.668, 0.0, 5.161], [0.971, 0.0, 4.736], [1.396, 0.0, 4.372], [2.004, 0.0, 4.372], [2.55, 0.0, 4.554], [2.975, 0.0, 4.797], [3.643, 0.0, 5.039], [3.643, 0.0, 4.311], [3.582, 0.0, 3.825], [3.582, 0.0, 3.218], [3.704, 0.0, 2.672], [4.189, 0.0, 2.368], [4.736, 0.0, 2.186], [5.222, 0.0, 2.125], [5.89, 0.0, 1.943], [5.525, 0.0, 1.336], [5.161, 0.0, 0.971], [4.797, 0.0, 0.546], [4.614, 0.0, 0.0], [4.797, 0.0, -0.546], [5.161, 0.0, -0.971], [5.525, 0.0, -1.336], [5.89, 0.0, -1.943], [5.222, 0.0, -2.125], [4.736, 0.0, -2.186], [4.189, 0.0, -2.368], [3.704, 0.0, -2.732], [3.582, 0.0, -3.279], [3.582, 0.0, -3.825], [3.643, 0.0, -4.311], [3.643, 0.0, -5.039], [2.975, 0.0, -4.797], [2.55, 0.0, -4.554], [2.004, 0.0, -4.372], [1.396, 0.0, -4.372], [0.971, 0.0, -4.736], [0.729, 0.0, -5.039], [0.425, 0.0, -5.647], [0.425, 0.0, -5.647], [0.425, 0.0, -5.647], [0.425, 0.0, -5.647]], d=3)
    else:    
        selected_objects = mc.ls(selection=True)
        target = selected_objects[0]
        objectPrim = mc.curve(p=[[0.425, 0.0, -5.647], [0.0, 0.0, -6.254], [-0.425, 0.0, -5.647], [-0.607, 0.0, -5.222], [-0.971, 0.0, -4.736], [-1.396, 0.0, -4.372], [-2.004, 0.0, -4.372], [-2.55, 0.0, -4.554], [-2.975, 0.0, -4.797], [-3.643, 0.0, -5.039], [-3.643, 0.0, -4.311], [-3.582, 0.0, -3.825], [-3.582, 0.0, -3.279], [-3.704, 0.0, -2.732], [-4.189, 0.0, -2.368], [-4.736, 0.0, -2.186], [-5.222, 0.0, -2.125], [-5.89, 0.0, -1.943], [-5.525, 0.0, -1.336], [-5.161, 0.0, -0.971], [-4.797, 0.0, -0.546], [-4.614, 0.0, 0.0], [-4.797, 0.0, 0.546], [-5.161, 0.0, 0.971], [-5.525, 0.0, 1.336], [-5.89, 0.0, 1.943], [-5.222, 0.0, 2.125], [-4.736, 0.0, 2.186], [-4.189, 0.0, 2.368], [-3.704, 0.0, 2.672], [-3.582, 0.0, 3.218], [-3.582, 0.0, 3.825], [-3.643, 0.0, 4.311], [-3.643, 0.0, 5.039], [-2.975, 0.0, 4.797], [-2.55, 0.0, 4.554], [-2.004, 0.0, 4.372], [-1.396, 0.0, 4.372], [-0.971, 0.0, 4.736], [-0.668, 0.0, 5.161], [-0.425, 0.0, 5.647], [0.0, 0.0, 6.193], [0.425, 0.0, 5.647], [0.668, 0.0, 5.161], [0.971, 0.0, 4.736], [1.396, 0.0, 4.372], [2.004, 0.0, 4.372], [2.55, 0.0, 4.554], [2.975, 0.0, 4.797], [3.643, 0.0, 5.039], [3.643, 0.0, 4.311], [3.582, 0.0, 3.825], [3.582, 0.0, 3.218], [3.704, 0.0, 2.672], [4.189, 0.0, 2.368], [4.736, 0.0, 2.186], [5.222, 0.0, 2.125], [5.89, 0.0, 1.943], [5.525, 0.0, 1.336], [5.161, 0.0, 0.971], [4.797, 0.0, 0.546], [4.614, 0.0, 0.0], [4.797, 0.0, -0.546], [5.161, 0.0, -0.971], [5.525, 0.0, -1.336], [5.89, 0.0, -1.943], [5.222, 0.0, -2.125], [4.736, 0.0, -2.186], [4.189, 0.0, -2.368], [3.704, 0.0, -2.732], [3.582, 0.0, -3.279], [3.582, 0.0, -3.825], [3.643, 0.0, -4.311], [3.643, 0.0, -5.039], [2.975, 0.0, -4.797], [2.55, 0.0, -4.554], [2.004, 0.0, -4.372], [1.396, 0.0, -4.372], [0.971, 0.0, -4.736], [0.729, 0.0, -5.039], [0.425, 0.0, -5.647], [0.425, 0.0, -5.647], [0.425, 0.0, -5.647], [0.425, 0.0, -5.647]], d=3)
        mc.parentConstraint(target, objectPrim, maintainOffset =False)
        mc.parentConstraint(target, objectPrim, e= True, rm= True)

def CCube():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.curve(p=[[-1.0, 1.0, -1.0], [-1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, -1.0], [-1.0, 1.0, -1.0], [-1.0, -1.0, -1.0], [-1.0, -1.0, 1.0], [1.0, -1.0, 1.0], [1.0, 1.0, 1.0], [-1.0, 1.0, 1.0], [-1.0, -1.0, 1.0], [-1.0, -1.0, -1.0], [1.0, -1.0, -1.0], [1.0, 1.0, -1.0], [1.0, 1.0, 1.0], [1.0, -1.0, 1.0], [1.0, -1.0, -1.0]], d=1)

    else:    
        selected_objects = mc.ls(selection= True)
        target = selected_objects[0]
        objectPrim = mc.curve(p=[[-1.0, 1.0, -1.0], [-1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, -1.0], [-1.0, 1.0, -1.0], [-1.0, -1.0, -1.0], [-1.0, -1.0, 1.0], [1.0, -1.0, 1.0], [1.0, 1.0, 1.0], [-1.0, 1.0, 1.0], [-1.0, -1.0, 1.0], [-1.0, -1.0, -1.0], [1.0, -1.0, -1.0], [1.0, 1.0, -1.0], [1.0, 1.0, 1.0], [1.0, -1.0, 1.0], [1.0, -1.0, -1.0]], d=1)
        mc.parentConstraint(target, objectPrim, maintainOffset = False)
        mc.parentConstraint(target, objectPrim, e=True, rm=True)

def CBridge():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.curve(p=[[3.002, 0.0, 15.423], [3.002, 3.948, 15.476], [3.002, 12.174, 12.127], [3.002, 17.127, 0.0], [3.002, 12.174, -12.127], [3.002, 3.948, -15.476], [3.002, 0.0, -15.423], [3.002, 0.0, -15.423], [3.002, 0.0, -15.423], [-3.002, 0.0, -15.423], [-3.002, 0.0, -15.423], [-3.002, 0.0, -15.423], [-3.002, 3.948, -15.476], [-3.002, 12.174, -12.127], [-3.002, 17.127, 0.0], [-3.002, 12.174, 12.127], [-3.002, 3.948, 15.476], [-3.002, 0.0, 15.423], [-3.002, 0.0, 15.423], [-3.002, 0.0, 15.423], [3.002, 0.0, 15.423]], d=3)

    else:    
        selected_objects = mc.ls(selection= True)
        target = selected_objects[0]
        objectPrim = mc.curve(p=[[3.002, 0.0, 15.423], [3.002, 3.948, 15.476], [3.002, 12.174, 12.127], [3.002, 17.127, 0.0], [3.002, 12.174, -12.127], [3.002, 3.948, -15.476], [3.002, 0.0, -15.423], [3.002, 0.0, -15.423], [3.002, 0.0, -15.423], [-3.002, 0.0, -15.423], [-3.002, 0.0, -15.423], [-3.002, 0.0, -15.423], [-3.002, 3.948, -15.476], [-3.002, 12.174, -12.127], [-3.002, 17.127, 0.0], [-3.002, 12.174, 12.127], [-3.002, 3.948, 15.476], [-3.002, 0.0, 15.423], [-3.002, 0.0, 15.423], [-3.002, 0.0, 15.423], [3.002, 0.0, 15.423]], d=3)
        mc.parentConstraint(target, objectPrim, maintainOffset= False)
        mc.parentConstraint(target, objectPrim, e= True, rm= True)

def CPyramid():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.curve(p=[[0.0, 2.0, 0.0], [1.0, 0.0, -1.0], [-1.0, 0.0, -1.0], [0.0, 2.0, 0.0], [-1.0, 0.0, 1.0], [1.0, 0.0, 1.0], [0.0, 2.0, 0.0], [1.0, 0.0, -1.0], [1.0, 0.0, 1.0], [-1.0, 0.0, 1.0], [-1.0, 0.0, -1.0]], d=1)

    else:    
        selected_objects = mc.ls(selection=True)
        target = selected_objects[0]
        objectPrim = mc.curve(p=[[0.0, 2.0, 0.0], [1.0, 0.0, -1.0], [-1.0, 0.0, -1.0], [0.0, 2.0, 0.0], [-1.0, 0.0, 1.0], [1.0, 0.0, 1.0], [0.0, 2.0, 0.0], [1.0, 0.0, -1.0], [1.0, 0.0, 1.0], [-1.0, 0.0, 1.0], [-1.0, 0.0, -1.0]], d=1)
        mc.parentConstraint(target, objectPrim, maintainOffset= False)
        mc.parentConstraint(target, objectPrim, e= True, rm= True)

def CRhombus():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.curve(p=[[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]], d=1)

    else:    
        selected_objects = mc.ls(selection= True)
        target = selected_objects[0]
        objectPrim = mc.curve(p=[[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]], d=1)
        mc.parentConstraint(target, objectPrim, maintainOffset= False)
        mc.parentConstraint(target, objectPrim, e= True, rm= True)

def CSphere():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.curve(p=[[-1.0, 0.0, 0.0], [-0.95, 0.31, 0.0], [-0.81, 0.59, 0.0], [-0.59, 0.81, 0.0], [-0.31, 0.95, 0.0], [0.0, 1.0, 0.0], [0.31, 0.95, 0.0], [0.59, 0.81, 0.0], [0.81, 0.59, 0.0], [0.95, 0.31, 0.0], [1.0, 0.0, 0.0], [0.95, -0.31, 0.0], [0.81, -0.59, 0.0], [0.59, -0.81, 0.0], [0.31, -0.95, 0.0], [0.0, -1.0, 0.0], [-0.31, -0.95, 0.0], [-0.59, -0.81, 0.0], [-0.81, -0.59, 0.0], [-0.95, -0.31, 0.0], [-1.0, 0.0, 0.0], [-0.95, 0.0, 0.31], [-0.81, 0.0, 0.59], [-0.59, 0.0, 0.81], [-0.31, 0.0, 0.95], [0.0, 0.0, 1.0], [0.31, 0.0, 0.95], [0.59, 0.0, 0.81], [0.81, 0.0, 0.59], [0.95, 0.0, 0.31], [1.0, 0.0, 0.0], [0.95, 0.0, -0.31], [0.81, 0.0, -0.59], [0.59, 0.0, -0.81], [0.31, 0.0, -0.95], [0.0, 0.0, -1.0], [0.0, 0.31, -0.95], [0.0, 0.59, -0.81], [0.0, 0.81, -0.59], [0.0, 0.95, -0.31], [0.0, 1.0, 0.0], [0.0, 0.95, 0.31], [0.0, 0.81, 0.59], [0.0, 0.59, 0.81], [0.0, 0.31, 0.95], [0.0, 0.0, 1.0], [0.0, -0.31, 0.95], [0.0, -0.59, 0.81], [0.0, -0.81, 0.59], [0.0, -0.95, 0.31], [0.0, -1.0, 0.0], [0.0, -0.95, -0.31], [0.0, -0.81, -0.59], [0.0, -0.59, -0.81], [0.0, -0.31, -0.95], [0.0, 0.0, -1.0], [-0.31, 0.0, -0.95], [-0.59, 0.0, -0.81], [-0.81, 0.0, -0.59], [-0.95, 0.0, -0.31], [-1.0, 0.0, 0.0]], d=1)

    else:    
        selected_objects = mc.ls(selection= True)
        target = selected_objects[0]
        objectPrim = mc.curve(p=[[-1.0, 0.0, 0.0], [-0.95, 0.31, 0.0], [-0.81, 0.59, 0.0], [-0.59, 0.81, 0.0], [-0.31, 0.95, 0.0], [0.0, 1.0, 0.0], [0.31, 0.95, 0.0], [0.59, 0.81, 0.0], [0.81, 0.59, 0.0], [0.95, 0.31, 0.0], [1.0, 0.0, 0.0], [0.95, -0.31, 0.0], [0.81, -0.59, 0.0], [0.59, -0.81, 0.0], [0.31, -0.95, 0.0], [0.0, -1.0, 0.0], [-0.31, -0.95, 0.0], [-0.59, -0.81, 0.0], [-0.81, -0.59, 0.0], [-0.95, -0.31, 0.0], [-1.0, 0.0, 0.0], [-0.95, 0.0, 0.31], [-0.81, 0.0, 0.59], [-0.59, 0.0, 0.81], [-0.31, 0.0, 0.95], [0.0, 0.0, 1.0], [0.31, 0.0, 0.95], [0.59, 0.0, 0.81], [0.81, 0.0, 0.59], [0.95, 0.0, 0.31], [1.0, 0.0, 0.0], [0.95, 0.0, -0.31], [0.81, 0.0, -0.59], [0.59, 0.0, -0.81], [0.31, 0.0, -0.95], [0.0, 0.0, -1.0], [0.0, 0.31, -0.95], [0.0, 0.59, -0.81], [0.0, 0.81, -0.59], [0.0, 0.95, -0.31], [0.0, 1.0, 0.0], [0.0, 0.95, 0.31], [0.0, 0.81, 0.59], [0.0, 0.59, 0.81], [0.0, 0.31, 0.95], [0.0, 0.0, 1.0], [0.0, -0.31, 0.95], [0.0, -0.59, 0.81], [0.0, -0.81, 0.59], [0.0, -0.95, 0.31], [0.0, -1.0, 0.0], [0.0, -0.95, -0.31], [0.0, -0.81, -0.59], [0.0, -0.59, -0.81], [0.0, -0.31, -0.95], [0.0, 0.0, -1.0], [-0.31, 0.0, -0.95], [-0.59, 0.0, -0.81], [-0.81, 0.0, -0.59], [-0.95, 0.0, -0.31], [-1.0, 0.0, 0.0]], d=1)
        mc.parentConstraint(target, objectPrim, maintainOffset = False)
        mc.parentConstraint(target, objectPrim, e=True, rm=True)

def CLocator():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.spaceLocator(r= 1)
    else:    
        selected_objects = mc.ls(selection= True)
        target = selected_objects[0]
        objectPrim = mc.spaceLocator(r= 1)
        mc.parentConstraint(target, objectPrim, maintainOffset= False)
        mc.parentConstraint(target, objectPrim, e= True, rm= True)

def CEyesSet():
    BulidEyeSet()

def CCurve():
    selection = mc.ls(sl= True)
    if selection ==[]:
        objectPrim = mc.curve(p=[[-5.0, 0.0, 0.0], [-5.0, 0.65, 0.0], [-4.74, 1.965, 0.0], [-3.628, 3.627, 0.0], [-1.963, 4.74, 0.0], [0.0, 5.13, -0.0], [1.963, 4.74, -0.0], [3.628, 3.627, -0.0], [4.74, 1.965, -0.0], [5.0, 0.65, -0.0], [5.0, -0.0, -0.0]], d=3)

    else:    
        selected_objects = mc.ls(selection= True)
        target = selected_objects[0]
        objectPrim = mc.curve(p=[[-5.0, 0.0, 0.0], [-5.0, 0.65, 0.0], [-4.74, 1.965, 0.0], [-3.628, 3.627, 0.0], [-1.963, 4.74, 0.0], [0.0, 5.13, -0.0], [1.963, 4.74, -0.0], [3.628, 3.627, -0.0], [4.74, 1.965, -0.0], [5.0, 0.65, -0.0], [5.0, -0.0, -0.0]], d=3)
        mc.parentConstraint(target, objectPrim, maintainOffset= False)
        mc.parentConstraint(target, objectPrim, e= True, rm= True)

def BulidEyeSet():
    objectPrim1 = mc.curve(name= 'eyesMain_CTL',p=[[5.657, 4.635, 0.001], [5.003, 4.635, 0.001], [3.696, 4.634, 0.001], [1.733, 4.637, 0.001], [-0.228, 4.632, 0.001], [-2.191, 4.643, 0.001], [-3.823, 4.622, 0.001], [-5.136, 4.662, 0.001], [-6.431, 4.5, 0.001], [-7.632, 3.85, 0.001], [-8.448, 2.827, 0.001], [-9.064, 1.661, 0.001], [-9.36, 0.023, 0.001], [-9.019, -1.935, 0.001], [-7.956, -3.644, 0.001], [-6.498, -4.495, 0.001], [-5.192, -4.677, 0.001], [-4.211, -4.576, 0.001], [-3.261, -4.309, 0.001], [-2.414, -3.802, 0.001], [-1.651, -3.18, 0.001], [-0.745, -2.775, 0.001], [0.245, -2.692, 0.001], [1.543, -3.016, 0.001], [2.759, -4.182, 0.001], [4.686, -4.758, 0.001], [6.342, -4.545, 0.001], [7.501, -3.894, 0.001], [8.178, -3.18, 0.001], [8.743, -2.371, 0.001], [9.078, -1.44, 0.001], [9.202, -0.633, 0.001], [9.287, 0.02, 0.001], [9.195, 0.667, 0.001], [9.07, 1.483, 0.001], [8.715, 2.394, 0.001], [8.161, 3.225, 0.001], [7.447, 3.886, 0.001], [6.606, 4.431, 0.001], [5.997, 4.635, 0.001], [5.657, 4.635, 0.001]], d=3)
    objectPrim2 = mc.curve(name= 'eye_L_CTL', p=[[4.645, -2.303, 0.0], [5.126, -2.303, 0.0], [6.091, -1.989, 0.0], [6.984, -0.76, 0.0], [6.984, 0.76, -0.0], [6.091, 1.989, -0.0], [4.645, 2.459, -0.0], [3.2, 1.989, -0.0], [2.306, 0.76, -0.0], [2.307, -0.76, 0.0], [3.199, -1.989, 0.0], [4.164, -2.303, 0.0], [4.645, -2.303, 0.0]], d=3)
    mc.xform(objectPrim2, pivots= [4.645, 0.078, 0])
    objectPrim3 = mc.curve(name= 'eye_R_CTL',p=[[-4.645, 2.303, 0.0], [-5.126, 2.303, 0.0], [-6.091, 1.989, 0.0], [-6.984, 0.76, 0.0], [-6.984, -0.76, -0.0], [-6.091, -1.989, -0.0], [-4.645, -2.459, -0.0], [-3.2, -1.989, -0.0], [-2.306, -0.76, -0.0], [-2.307, 0.76, 0.0], [-3.199, 1.989, 0.0], [-4.164, 2.303, 0.0], [-4.645, 2.303, 0.0]], d=3)
    mc.xform(objectPrim3, pivots= [-4.645, 0.078, 0])
    mc.parent(objectPrim3,objectPrim2,objectPrim1)
    mc.select(objectPrim1)

def EPCurve():
    mc.EPCurveTool()

def PolyToCurve(degree):
    selected_edges = mc.ls(selection= True)
    if selected_edges:
        for edge in selected_edges:
                mc.polyToCurve(form= 2, degree= degree)
    else:
        print("no edge selected.")

def PolyToCurve_degree1(*args):
    PolyToCurve(1)
def PolyToCurve_degree2(*args):
    PolyToCurve(2)
def PolyToCurve_degree3(*args):
    PolyToCurve(3)
def PolyToCurve_degree5(*args):
    PolyToCurve(5)
def PolyToCurve_degree7(*args):
    PolyToCurve(7)


# Color __________________________________________________________________________
def SetColor(color_index):      
    selected_objects = mc.ls(selection= True)
    for obj in selected_objects:
        mc.setAttr(f'{obj}.overrideEnabled', True)
        mc.setAttr(f'{obj}.overrideRGBColors', False)
        mc.setAttr(f'{obj}.overrideColor', color_index)
        
# ? Custom ColorButton ?__________________________________________________________      
def SetRGB(*args):
    # Open the color editor and get the color chosen by the user
    result = mc.colorEditor()
    if mc.colorEditor(query= True, result= True):
        # Extract RGB values from the colorEditor, which returns them normalized
        r, g, b = mc.colorEditor(query= True, rgb= True)  # Unpack the RGB values
        
        selected = mc.ls(selection= True)
        if selected:
            mc.setAttr(selected[0] + '.overrideEnabled', True)
            mc.setAttr(selected[0] + '.overrideRGBColors', True)
            mc.setAttr(selected[0] + '.overrideColorRGB', r, g, b)

# Combine Curve __________________________________________________________________
def CombineCurves():
    selected_objects = mc.ls(selection= True)
    
    if not selected_objects:
        mc.error('Please select one or more NURBS curves to combine.')

    newCurve = mc.group(empty= True, name= selected_objects[-1])
    
    # Match the transformation (position and rotation) of newCurve with the last selected object
    oldCurve = selected_objects[-1]
    mc.matchTransform(newCurve, oldCurve, position= True, rotation= True)
    
    # Apply identity transformation to newCurve
    mc.makeIdentity(newCurve, apply= True, t= True, r= True, s= True, n= False, pn= True)
    
    # List to store all control names for later use
    all_ctl = []
    
    # Iterate over each selected object
    for obj in selected_objects:
        # Store the control names
        all_ctl.append(obj)
        
        # Apply identity transformation to the selected object
        mc.makeIdentity(obj, apply= True, t= True, r= True, s= True, n= False, pn= True)
        
        # Get the shapes of the selected object
        curveShape = mc.listRelatives(obj, shapes= True)
        
        # Iterate over each shape of the selected object
        for shape in curveShape:
            # Parent the shape to newCurve with the -r -s flags
            mc.parent(shape, newCurve, relative= True, shape= True)
        
        # Delete the selected object
        mc.delete(obj)
        mc.select(newCurve)
    
    # Print the names of the combined shapes
    combined_shapes = ', '.join(all_ctl)
    print(f'// Combine Curve Shape :: {combined_shapes}\n')

    return newCurve

# Swap Curve _____________________________________________________________________
def SwapCurve(keepCurve= False):
    selected_objects = mc.ls(selection= True)
    newShape = selected_objects[-1]  # The last selected object is the new curve
    
    # Exclude oldCurve from the selected list to get child controls
    child_ctls = [obj for obj in selected_objects if obj != newShape]

    # Iterate over each child control
    for child_ctl in child_ctls:
        # Duplicate the mom control and get the duplicated shape
        new_curve = mc.duplicate(newShape, rr= True)[0]
        newShape_shapes = mc.listRelatives(new_curve, shapes= True)
        
        # Get the shapes of the child control
        child_shapes = mc.listRelatives(child_ctl, shapes= True)
        
        # Iterate over each shape of the child control
        for idx, child_shape in enumerate(child_shapes):
            # Rename the new shape based on the child control
            new_shape_name = mc.rename(newShape_shapes[idx], f'{child_ctl}{idx + 1}_shp')
            
            # Parent the new shape to the child control
            mc.parent(new_shape_name, child_ctl, shape= True, relative= True)
        
        # Delete the original child shape and the duplicated mom control
        mc.delete(child_shapes[0], new_curve)
        
    #if not keep curve
    if not keepCurve:
        mc.delete(newShape)

# Create Offset __________________________________________________________________
def CreateOffsetGroup():
    print('offset')
    selected_curves = mc.ls(selection= True)
    
    if selected_curves:
        for curve in selected_curves:
            # Create a group for each curve and name it with "_offset"
            group = mc.group(empty= True, name= f'{curve}_offset')
            
            # Copy translate, rotate, and scale from the curve to the group
            translate = mc.getAttr(curve + '.translate')[0]
            rotate = mc.getAttr(curve + '.rotate')[0]
            scale = mc.getAttr(curve + '.scale')[0]
            
            mc.setAttr(group + '.translate', *translate)
            mc.setAttr(group + '.rotate', *rotate)
            mc.setAttr(group + '.scale', *scale)
            
            # Parent the curve to the group
            mc.parent(curve, group)
            
            # Freeze the group's scale
            mc.makeIdentity(group, apply=True, t= 0, r= 0, s= 1, n= 0, pn= 1)
            print('Offset Group Created')

# Get Curve Attr _________________________________________________________________
def GetCurveAttr(): 
    getcontext().prec = 5
    
    shp = mc.listRelatives(mc.ls(sl=True)[0], s= True)[0]
    cvs = mc.getAttr(shp + '.cv[*]')
    cvsSimple = []
    for c in cvs:
        cvsSimple.append([
            float(Decimal('%.3f' % c[0])),
            float(Decimal('%.3f' % c[1])),
            float(Decimal('%.3f' % c[2]))
        ])
    
    out = '\n\n# Get Curve Attr #\nmc.curve(p='  
    out += '[%s]' % ', '.join(map(str, cvsSimple))
    out += ', d=' + str(mc.getAttr(shp + '.degree')) + ')'
    
    print(out)

createWin()