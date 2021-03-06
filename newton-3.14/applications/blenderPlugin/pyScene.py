# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pyScene', [dirname(__file__)])
        except ImportError:
            import _pyScene
            return _pyScene
        if fp is not None:
            try:
                _mod = imp.load_module('_pyScene', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pyScene = swig_import_helper()
    del swig_import_helper
else:
    import _pyScene
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class objInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, objInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, objInfo, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pyScene.new_objInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_objInfo
    __del__ = lambda self : None;
objInfo_swigregister = _pyScene.objInfo_swigregister
objInfo_swigregister(objInfo)

class meshInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, meshInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, meshInfo, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pyScene.new_meshInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_meshInfo
    __del__ = lambda self : None;
meshInfo_swigregister = _pyScene.meshInfo_swigregister
meshInfo_swigregister(meshInfo)

class texInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, texInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, texInfo, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pyScene.new_texInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_texInfo
    __del__ = lambda self : None;
texInfo_swigregister = _pyScene.texInfo_swigregister
texInfo_swigregister(texInfo)

class matInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, matInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, matInfo, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pyScene.new_matInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_matInfo
    __del__ = lambda self : None;
matInfo_swigregister = _pyScene.matInfo_swigregister
matInfo_swigregister(matInfo)

class rigidBidyInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rigidBidyInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rigidBidyInfo, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pyScene.new_rigidBidyInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_rigidBidyInfo
    __del__ = lambda self : None;
rigidBidyInfo_swigregister = _pyScene.rigidBidyInfo_swigregister
rigidBidyInfo_swigregister(rigidBidyInfo)

class pyTrianglePoint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pyTrianglePoint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pyTrianglePoint, name)
    __repr__ = _swig_repr
    __swig_setmethods__["vertex"] = _pyScene.pyTrianglePoint_vertex_set
    __swig_getmethods__["vertex"] = _pyScene.pyTrianglePoint_vertex_get
    if _newclass:vertex = _swig_property(_pyScene.pyTrianglePoint_vertex_get, _pyScene.pyTrianglePoint_vertex_set)
    __swig_setmethods__["normal"] = _pyScene.pyTrianglePoint_normal_set
    __swig_getmethods__["normal"] = _pyScene.pyTrianglePoint_normal_get
    if _newclass:normal = _swig_property(_pyScene.pyTrianglePoint_normal_get, _pyScene.pyTrianglePoint_normal_set)
    __swig_setmethods__["uv0"] = _pyScene.pyTrianglePoint_uv0_set
    __swig_getmethods__["uv0"] = _pyScene.pyTrianglePoint_uv0_get
    if _newclass:uv0 = _swig_property(_pyScene.pyTrianglePoint_uv0_get, _pyScene.pyTrianglePoint_uv0_set)
    __swig_setmethods__["uv1"] = _pyScene.pyTrianglePoint_uv1_set
    __swig_getmethods__["uv1"] = _pyScene.pyTrianglePoint_uv1_get
    if _newclass:uv1 = _swig_property(_pyScene.pyTrianglePoint_uv1_get, _pyScene.pyTrianglePoint_uv1_set)
    def __init__(self): 
        this = _pyScene.new_pyTrianglePoint()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_pyTrianglePoint
    __del__ = lambda self : None;
pyTrianglePoint_swigregister = _pyScene.pyTrianglePoint_swigregister
pyTrianglePoint_swigregister(pyTrianglePoint)

class pyTriangle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pyTriangle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pyTriangle, name)
    __repr__ = _swig_repr
    __swig_setmethods__["p0"] = _pyScene.pyTriangle_p0_set
    __swig_getmethods__["p0"] = _pyScene.pyTriangle_p0_get
    if _newclass:p0 = _swig_property(_pyScene.pyTriangle_p0_get, _pyScene.pyTriangle_p0_set)
    __swig_setmethods__["p1"] = _pyScene.pyTriangle_p1_set
    __swig_getmethods__["p1"] = _pyScene.pyTriangle_p1_get
    if _newclass:p1 = _swig_property(_pyScene.pyTriangle_p1_get, _pyScene.pyTriangle_p1_set)
    __swig_setmethods__["p2"] = _pyScene.pyTriangle_p2_set
    __swig_getmethods__["p2"] = _pyScene.pyTriangle_p2_get
    if _newclass:p2 = _swig_property(_pyScene.pyTriangle_p2_get, _pyScene.pyTriangle_p2_set)
    __swig_setmethods__["materialIndex"] = _pyScene.pyTriangle_materialIndex_set
    __swig_getmethods__["materialIndex"] = _pyScene.pyTriangle_materialIndex_get
    if _newclass:materialIndex = _swig_property(_pyScene.pyTriangle_materialIndex_get, _pyScene.pyTriangle_materialIndex_set)
    def __init__(self): 
        this = _pyScene.new_pyTriangle()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_pyTriangle
    __del__ = lambda self : None;
pyTriangle_swigregister = _pyScene.pyTriangle_swigregister
pyTriangle_swigregister(pyTriangle)

class pyVertex(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pyVertex, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pyVertex, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _pyScene.pyVertex_x_set
    __swig_getmethods__["x"] = _pyScene.pyVertex_x_get
    if _newclass:x = _swig_property(_pyScene.pyVertex_x_get, _pyScene.pyVertex_x_set)
    __swig_setmethods__["y"] = _pyScene.pyVertex_y_set
    __swig_getmethods__["y"] = _pyScene.pyVertex_y_get
    if _newclass:y = _swig_property(_pyScene.pyVertex_y_get, _pyScene.pyVertex_y_set)
    __swig_setmethods__["z"] = _pyScene.pyVertex_z_set
    __swig_getmethods__["z"] = _pyScene.pyVertex_z_get
    if _newclass:z = _swig_property(_pyScene.pyVertex_z_get, _pyScene.pyVertex_z_set)
    def __init__(self): 
        this = _pyScene.new_pyVertex()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_pyVertex
    __del__ = lambda self : None;
pyVertex_swigregister = _pyScene.pyVertex_swigregister
pyVertex_swigregister(pyVertex)

class pyMatrix4x4(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pyMatrix4x4, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pyMatrix4x4, name)
    __repr__ = _swig_repr
    __swig_setmethods__["e00"] = _pyScene.pyMatrix4x4_e00_set
    __swig_getmethods__["e00"] = _pyScene.pyMatrix4x4_e00_get
    if _newclass:e00 = _swig_property(_pyScene.pyMatrix4x4_e00_get, _pyScene.pyMatrix4x4_e00_set)
    __swig_setmethods__["e01"] = _pyScene.pyMatrix4x4_e01_set
    __swig_getmethods__["e01"] = _pyScene.pyMatrix4x4_e01_get
    if _newclass:e01 = _swig_property(_pyScene.pyMatrix4x4_e01_get, _pyScene.pyMatrix4x4_e01_set)
    __swig_setmethods__["e02"] = _pyScene.pyMatrix4x4_e02_set
    __swig_getmethods__["e02"] = _pyScene.pyMatrix4x4_e02_get
    if _newclass:e02 = _swig_property(_pyScene.pyMatrix4x4_e02_get, _pyScene.pyMatrix4x4_e02_set)
    __swig_setmethods__["e03"] = _pyScene.pyMatrix4x4_e03_set
    __swig_getmethods__["e03"] = _pyScene.pyMatrix4x4_e03_get
    if _newclass:e03 = _swig_property(_pyScene.pyMatrix4x4_e03_get, _pyScene.pyMatrix4x4_e03_set)
    __swig_setmethods__["e10"] = _pyScene.pyMatrix4x4_e10_set
    __swig_getmethods__["e10"] = _pyScene.pyMatrix4x4_e10_get
    if _newclass:e10 = _swig_property(_pyScene.pyMatrix4x4_e10_get, _pyScene.pyMatrix4x4_e10_set)
    __swig_setmethods__["e11"] = _pyScene.pyMatrix4x4_e11_set
    __swig_getmethods__["e11"] = _pyScene.pyMatrix4x4_e11_get
    if _newclass:e11 = _swig_property(_pyScene.pyMatrix4x4_e11_get, _pyScene.pyMatrix4x4_e11_set)
    __swig_setmethods__["e12"] = _pyScene.pyMatrix4x4_e12_set
    __swig_getmethods__["e12"] = _pyScene.pyMatrix4x4_e12_get
    if _newclass:e12 = _swig_property(_pyScene.pyMatrix4x4_e12_get, _pyScene.pyMatrix4x4_e12_set)
    __swig_setmethods__["e13"] = _pyScene.pyMatrix4x4_e13_set
    __swig_getmethods__["e13"] = _pyScene.pyMatrix4x4_e13_get
    if _newclass:e13 = _swig_property(_pyScene.pyMatrix4x4_e13_get, _pyScene.pyMatrix4x4_e13_set)
    __swig_setmethods__["e20"] = _pyScene.pyMatrix4x4_e20_set
    __swig_getmethods__["e20"] = _pyScene.pyMatrix4x4_e20_get
    if _newclass:e20 = _swig_property(_pyScene.pyMatrix4x4_e20_get, _pyScene.pyMatrix4x4_e20_set)
    __swig_setmethods__["e21"] = _pyScene.pyMatrix4x4_e21_set
    __swig_getmethods__["e21"] = _pyScene.pyMatrix4x4_e21_get
    if _newclass:e21 = _swig_property(_pyScene.pyMatrix4x4_e21_get, _pyScene.pyMatrix4x4_e21_set)
    __swig_setmethods__["e22"] = _pyScene.pyMatrix4x4_e22_set
    __swig_getmethods__["e22"] = _pyScene.pyMatrix4x4_e22_get
    if _newclass:e22 = _swig_property(_pyScene.pyMatrix4x4_e22_get, _pyScene.pyMatrix4x4_e22_set)
    __swig_setmethods__["e23"] = _pyScene.pyMatrix4x4_e23_set
    __swig_getmethods__["e23"] = _pyScene.pyMatrix4x4_e23_get
    if _newclass:e23 = _swig_property(_pyScene.pyMatrix4x4_e23_get, _pyScene.pyMatrix4x4_e23_set)
    __swig_setmethods__["e30"] = _pyScene.pyMatrix4x4_e30_set
    __swig_getmethods__["e30"] = _pyScene.pyMatrix4x4_e30_get
    if _newclass:e30 = _swig_property(_pyScene.pyMatrix4x4_e30_get, _pyScene.pyMatrix4x4_e30_set)
    __swig_setmethods__["e31"] = _pyScene.pyMatrix4x4_e31_set
    __swig_getmethods__["e31"] = _pyScene.pyMatrix4x4_e31_get
    if _newclass:e31 = _swig_property(_pyScene.pyMatrix4x4_e31_get, _pyScene.pyMatrix4x4_e31_set)
    __swig_setmethods__["e32"] = _pyScene.pyMatrix4x4_e32_set
    __swig_getmethods__["e32"] = _pyScene.pyMatrix4x4_e32_get
    if _newclass:e32 = _swig_property(_pyScene.pyMatrix4x4_e32_get, _pyScene.pyMatrix4x4_e32_set)
    __swig_setmethods__["e33"] = _pyScene.pyMatrix4x4_e33_set
    __swig_getmethods__["e33"] = _pyScene.pyMatrix4x4_e33_get
    if _newclass:e33 = _swig_property(_pyScene.pyMatrix4x4_e33_get, _pyScene.pyMatrix4x4_e33_set)
    def __init__(self): 
        this = _pyScene.new_pyMatrix4x4()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_pyMatrix4x4
    __del__ = lambda self : None;
pyMatrix4x4_swigregister = _pyScene.pyMatrix4x4_swigregister
pyMatrix4x4_swigregister(pyMatrix4x4)

class pyMesh(meshInfo):
    __swig_setmethods__ = {}
    for _s in [meshInfo]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, pyMesh, name, value)
    __swig_getmethods__ = {}
    for _s in [meshInfo]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, pyMesh, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pyScene.new_pyMesh(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_pyMesh
    __del__ = lambda self : None;
    def SetName(self, *args): return _pyScene.pyMesh_SetName(self, *args)
    def BuildFromVertexListIndexList(self, *args): return _pyScene.pyMesh_BuildFromVertexListIndexList(self, *args)
    def SmoothNormals(self, *args): return _pyScene.pyMesh_SmoothNormals(self, *args)
    def GetVertexCount(self): return _pyScene.pyMesh_GetVertexCount(self)
    def GetVertex(self, *args): return _pyScene.pyMesh_GetVertex(self, *args)
    def GetNormal(self, *args): return _pyScene.pyMesh_GetNormal(self, *args)
    def GetUV0(self, *args): return _pyScene.pyMesh_GetUV0(self, *args)
    def GetUV1(self, *args): return _pyScene.pyMesh_GetUV1(self, *args)
    def GetFirstTriangle(self): return _pyScene.pyMesh_GetFirstTriangle(self)
    def GetNextTriangle(self, *args): return _pyScene.pyMesh_GetNextTriangle(self, *args)
    def GetTriangle(self, *args): return _pyScene.pyMesh_GetTriangle(self, *args)
pyMesh_swigregister = _pyScene.pyMesh_swigregister
pyMesh_swigregister(pyMesh)

class pyScene(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pyScene, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pyScene, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _pyScene.new_pyScene()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_pyScene
    __del__ = lambda self : None;
    def Load(self, *args): return _pyScene.pyScene_Load(self, *args)
    def Save(self, *args): return _pyScene.pyScene_Save(self, *args)
    def GetRoot(self): return _pyScene.pyScene_GetRoot(self)
    def GetFirstChildLink(self, *args): return _pyScene.pyScene_GetFirstChildLink(self, *args)
    def GetNextChildLink(self, *args): return _pyScene.pyScene_GetNextChildLink(self, *args)
    def AddReference(self, *args): return _pyScene.pyScene_AddReference(self, *args)
    def GetNodeFromLink(self, *args): return _pyScene.pyScene_GetNodeFromLink(self, *args)
    def IsSceneNode(self, *args): return _pyScene.pyScene_IsSceneNode(self, *args)
    def IsMeshNode(self, *args): return _pyScene.pyScene_IsMeshNode(self, *args)
    def IsMaterialNode(self, *args): return _pyScene.pyScene_IsMaterialNode(self, *args)
    def IsTextureNode(self, *args): return _pyScene.pyScene_IsTextureNode(self, *args)
    def GetNodeName(self, *args): return _pyScene.pyScene_GetNodeName(self, *args)
    def CreateSceneNode(self, *args): return _pyScene.pyScene_CreateSceneNode(self, *args)
    def CreateMeshNode(self, *args): return _pyScene.pyScene_CreateMeshNode(self, *args)
    def CreateRigidbodyNode(self, *args): return _pyScene.pyScene_CreateRigidbodyNode(self, *args)
    def CreateTextureNode(self, *args): return _pyScene.pyScene_CreateTextureNode(self, *args)
    def CreateMaterialNode(self, *args): return _pyScene.pyScene_CreateMaterialNode(self, *args)
    def GetScene(self): return _pyScene.pyScene_GetScene(self)
pyScene_swigregister = _pyScene.pyScene_swigregister
pyScene_swigregister(pyScene)

class pyObject(objInfo):
    __swig_setmethods__ = {}
    for _s in [objInfo]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, pyObject, name, value)
    __swig_getmethods__ = {}
    for _s in [objInfo]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, pyObject, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pyScene.new_pyObject(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_pyObject
    __del__ = lambda self : None;
    def SetName(self, *args): return _pyScene.pyObject_SetName(self, *args)
    def SetMatrix(self, *args): return _pyScene.pyObject_SetMatrix(self, *args)
    def GetMatrix4x4(self): return _pyScene.pyObject_GetMatrix4x4(self)
    def GetLocalPosition(self): return _pyScene.pyObject_GetLocalPosition(self)
    def GetLocalEulers(self): return _pyScene.pyObject_GetLocalEulers(self)
    def GetLocalScale(self): return _pyScene.pyObject_GetLocalScale(self)
pyObject_swigregister = _pyScene.pyObject_swigregister
pyObject_swigregister(pyObject)

class pyTexture(texInfo):
    __swig_setmethods__ = {}
    for _s in [texInfo]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, pyTexture, name, value)
    __swig_getmethods__ = {}
    for _s in [texInfo]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, pyTexture, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pyScene.new_pyTexture(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_pyTexture
    __del__ = lambda self : None;
    def GetId(self): return _pyScene.pyTexture_GetId(self)
    def GetImageName(self): return _pyScene.pyTexture_GetImageName(self)
pyTexture_swigregister = _pyScene.pyTexture_swigregister
pyTexture_swigregister(pyTexture)

class pyMaterial(matInfo):
    __swig_setmethods__ = {}
    for _s in [matInfo]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, pyMaterial, name, value)
    __swig_getmethods__ = {}
    for _s in [matInfo]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, pyMaterial, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pyScene.new_pyMaterial(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_pyMaterial
    __del__ = lambda self : None;
    def GetId(self): return _pyScene.pyMaterial_GetId(self)
    def SetAmbientTextId(self, *args): return _pyScene.pyMaterial_SetAmbientTextId(self, *args)
    def SetDiffuseTextId(self, *args): return _pyScene.pyMaterial_SetDiffuseTextId(self, *args)
pyMaterial_swigregister = _pyScene.pyMaterial_swigregister
pyMaterial_swigregister(pyMaterial)

class pyRigidBody(rigidBidyInfo):
    __swig_setmethods__ = {}
    for _s in [rigidBidyInfo]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, pyRigidBody, name, value)
    __swig_getmethods__ = {}
    for _s in [rigidBidyInfo]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, pyRigidBody, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pyScene.new_pyRigidBody(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_pyRigidBody
    __del__ = lambda self : None;
    def SetName(self, *args): return _pyScene.pyRigidBody_SetName(self, *args)
    def SetShape(self, *args): return _pyScene.pyRigidBody_SetShape(self, *args)
    def SetMass(self, *args): return _pyScene.pyRigidBody_SetMass(self, *args)
pyRigidBody_swigregister = _pyScene.pyRigidBody_swigregister
pyRigidBody_swigregister(pyRigidBody)

class intArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pyScene.new_intArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_intArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _pyScene.intArray___getitem__(self, *args)
    def __setitem__(self, *args): return _pyScene.intArray___setitem__(self, *args)
    def cast(self): return _pyScene.intArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _pyScene.intArray_frompointer
    if _newclass:frompointer = staticmethod(_pyScene.intArray_frompointer)
intArray_swigregister = _pyScene.intArray_swigregister
intArray_swigregister(intArray)

def intArray_frompointer(*args):
  return _pyScene.intArray_frompointer(*args)
intArray_frompointer = _pyScene.intArray_frompointer

class doubleArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doubleArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doubleArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pyScene.new_doubleArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyScene.delete_doubleArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _pyScene.doubleArray___getitem__(self, *args)
    def __setitem__(self, *args): return _pyScene.doubleArray___setitem__(self, *args)
    def cast(self): return _pyScene.doubleArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _pyScene.doubleArray_frompointer
    if _newclass:frompointer = staticmethod(_pyScene.doubleArray_frompointer)
doubleArray_swigregister = _pyScene.doubleArray_swigregister
doubleArray_swigregister(doubleArray)

def doubleArray_frompointer(*args):
  return _pyScene.doubleArray_frompointer(*args)
doubleArray_frompointer = _pyScene.doubleArray_frompointer



