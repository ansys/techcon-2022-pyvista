import vtk
reader = vtk.vtkSTLReader()
reader.SetFileName("bunny.stl")
mapper = vtk.vtkPolyDataMapper()
output_port = reader.GetOutputPort()
mapper.SetInputConnection(output_port)
actor = vtk.vtkActor()
actor.SetMapper(mapper)
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
ren.AddActor(actor)
iren.Initialize()
renWin.Render()
iren.Start()
