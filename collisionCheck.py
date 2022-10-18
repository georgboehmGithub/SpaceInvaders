def collisionCheck(obj1,obj2):
    obj1Top = obj1.position[1]
    obj1Bottom = obj1.position[1] + obj1.size[1]
    obj1Right = obj1.position[0] + obj1.size[0]
    obj1Left = obj1.position[0]
    
    obj2Top = obj2.position[1]
    obj2Bottom = obj2.position[1] + obj2.size[1]
    obj2Right = obj2.position[0] + obj2.size[0]
    obj2Left = obj2.position[0]

    Hit = False
    if obj1.objType != obj2.objType:
         if pointInRect (obj1Left, obj1Top, obj2Left, obj2Top, obj2Right, obj2Bottom) or \
            pointInRect (obj2Left, obj2Top, obj1Left, obj1Top, obj1Right, obj1Bottom) or \
            pointInRect(obj1Right, obj1Bottom, obj2Left, obj2Top, obj2Right, obj2Bottom) or \
            pointInRect(obj2Right, obj2Bottom, obj1Left, obj1Top, obj1Right, obj1Bottom):
            Hit = True
    return Hit
     
def pointInRect (pl,pt,l,t,r,b):
    if (pl >= l) and (pl <= r) and (pt >= t) and (pt <= b):
        return True
    else:
        return False