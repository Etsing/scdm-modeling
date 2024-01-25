ClearAll()
import csv
def l2p(list):
    return Point.Create(UM(list[0]), UM(list[1]), UM(list[2]))
def Ccy(c1, s1, e1):#通过坐标生成圆柱体
    cpt = l2p(c1)
    spt = l2p(s1)
    ept = l2p(e1)
    body = CylinderBody.Create(cpt, spt, ept)
def csp(cen,r):#通过坐标生成球体
    cp = l2p(cen)   
    c1 = [cen[0]+r,cen[1],cen[2]]
    cpr = l2p(c1)
    body = SphereBody.Create(cp,cpr) 
def cyl(sel,r):
    body = TubeBody.Create(sel, UM(r))

def hidedef():
    selection = BodySelection.Create(GetRootPart().Bodies[0])
    visibility = VisibilityType.Hide
    inSelectedView = False
    faceLevel = False
    ViewHelper.SetObjectVisibility(selection, visibility, inSelectedView, faceLevel)

def showdef():
    selection = BodySelection.Create(GetRootPart().Bodies[0])
    visibility = VisibilityType.Show
    inSelectedView = False
    faceLevel = False
    ViewHelper.SetObjectVisibility(selection, visibility, inSelectedView, faceLevel)
def hide(sel):
    visibility = VisibilityType.Hide
    ViewHelper.SetObjectVisibility(sel, visibility, False, False)
def vis(sel):
    visibility = VisibilityType.Show
    ViewHelper.SetObjectVisibility(sel, visibility, False, False)
def cutedge():
    targets = BodySelection.Create(GetRootPart().Bodies[0])
    tools = BodySelection.Create(GetRootPart().Bodies[1])
    options = MakeSolidsOptions()
    options.KeepCutter = False
    result = Combine.Intersect(targets, tools, options)
def del0():
    selection = BodySelection.Create(GetRootPart().Bodies[0])
    Combine.RemoveRegions(selection)
def del1():
    selection = BodySelection.Create(GetRootPart().Bodies[1])
    Combine.RemoveRegions(selection)

def cln(list):
    ptList=List[Point]()
    ptList.Add(Point.Create(UM(list[0]), UM(list[1]), UM(list[2])))
    ptList.Add(Point.Create(UM(list[3]), UM(list[4]), UM(list[5])))
    ncurve = NurbsCurve.CreateThroughPoints(False, ptList, 0.0001) #创建一个样条曲线穿过所有创建的点
    curveSegment = CurveSegment.Create(ncurve) #创建一个有限线段对象
    curve_lenghth=curveSegment.Length
    designCurve = DesignCurve.Create(GetRootPart(),curveSegment) #创建DesignCurve对象
 def Ccube(c1,c2):#生成立方体
    s = l2p(c1)
    e = l2p(c2)
    body = BlockBody.Create(s, e)
   
def intersecbody(targets,tools):
    options = MakeSolidsOptions()
    options.KeepCutter = False
    result = Combine.Intersect(targets, tools, options)
    
def namecreate(selction, str):
    #  输入时str处需要加引号
    # NamedSelection.Rename("原名称","新名称")
    # 重命名
    sel = Selection.Create(selction)
    ns = NamedSelection.Create(sel,Selection())
    ns.CreatedNamedSelection.SetName(str)

###################################
# 参数输入
r = 20 
l = 400
###################################
# 顶点坐标
p1 = [0,0,0]
p2 =[l,0,0] 
p3 = [l,l,0]
p4 = [0,l,0]
p5 = [0,0,l]
p6 = [l,0,l]
p7 = [l,l,l]
p8 = [0,l,l]
###################################
# 生成线段
l1 = p1 + p2
cln(l1)
l2 = p2 + p3
cln(l2)
l3 = p3 + p4
cln(l3)
l4 = p4 + p1
cln(l4)
l5 = p1 + p5
cln(l5)
l6 = p2 + p6
cln(l6)
l7 = p3 + p7
cln(l7)
l8 = p4 + p8
cln(l8)
l9 = p5 + p6
cln(l9)
l10 = p6 + p7
cln(l10)
l11 = p7 + p8
cln(l11)
l12 = p8 + p5
cln(l12)
###################################
#
sel = List[IDesignCurve]()
part = GetRootPart()
for Curve in part.Curves:
    sel.Add(Curve)
linegroup = Selection.Create(sel)
cyl(linegroup,r)
res = Delete.Execute(linegroup)
###################################
#
hidedef()
vmax = l
vmin = 0

v1 = [vmax,vmax,vmax]
v2 = [vmin,vmin,vmin]
Ccube(v1,v2)
showdef()
###################################
#
ta = BodySelection.Create(GetRootPart().Bodies[1])
to = BodySelection.Create(GetRootPart().Bodies[0])
intersecbody(ta,to)
###################################
#
topface = List[IDesignFace]()
wallface = List[IDesignFace]()
bottomface = List[IDesignFace]()
for body in GetRootPart().GetAllBodies():
    for face in body.Faces:
        mid_point = face.EvalMid().Point
        if mid_point[2] ==0 :
            topface.Add(face)
        elif mid_point[2] ==0.4:
            bottomface.Add(face)
        elif mid_point[0] ==0.4 or mid_point[0] ==0 or mid_point[1] ==0.4 or mid_point[1] ==0 :
            wallface.Add(face)
        
namecreate(topface,'top')
wallsel = Selection.Create(wallface)
namecreate(wallface,'wall')
botsel = Selection.Create(bottomface)
namecreate(bottomface,'bottom')

