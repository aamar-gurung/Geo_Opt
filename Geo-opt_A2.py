#AIA GEO-OPT
# AMAR GURURNG
# ASSIGNMENT 2

import Rhino.Geometry as rg
"""Provides a scripting component.
    Inputs:
        m: a mesh
        s: sun vector
    Output:
        a: List of Vectors
        b: List of Points
        c: list of angles
        d: exploded mesh
        """
        

#1.
#compute face normals using rg.Mesh.FaceNormals.ComputeFaceNormals()
#output the vectors to a

m.FaceNormals.ComputeFaceNormals()
a = m.FaceNormals

print (a)
print type(a)

#2.
#get the centers of each faces using rg.Mesh.Faces.GetFaceCenter()
#store the centers into a list called centers 
#output that list to b

centers = []
for i in range(m.Faces.Count) :
    cnt = m.Faces.GetFaceCenter(i)
    centers.append(cnt)

b = centers

#3.
#calculate the angle between the sun and each FaceNormal using rg.Vector3d.VectorAngle()
#store the angles in a list called angleList and output it to c

anglelist = []
for i in range(len(b)):
    vectorangle = rg.Vector3d.VectorAngle(rg.Vector3d(b[i]),s)
    anglelist.append(vectorangle)
c = anglelist

dupmesh = rg.Mesh.Duplicate(a)

exploded = []
for i in range(dupmesh.Faces.Count):
    meshface = dupmesh.Faces.ExtractFaces([0])
    exploded.append(meshface)

d = exploded


#c = []

#4. explode the mesh - convert each face of the mesh into a mesh
#for this, you have to first copy the mesh using rg.Mesh.Duplicate()
#then iterate through each face of the copy, extract it using rg.Mesh.ExtractFaces
#and store the result into a list called exploded in output d

#d = exploded

#after here, your task is to apply a transformation to each face of the mesh
#the transformation should correspond to the angle value that corresponds that face to it... 
#the result should be a mesh that responds to the sun position... its up to you!