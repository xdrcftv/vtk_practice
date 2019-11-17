def vtkImage2Numpy(image, pixelDim):
    pointData = image.GetPointData()
    arrayData = pointData.GetArray(0)
    ArrayDicom = numpy_support.vtk_to_numpy(arrayData)
    ArrayDicom = ArrayDicom.reshape(pixelDims, order='F')

    return ArrayDicom

def plotHeatmap(array, name='plot'):
    data = Data([Heatmap(z=array,scl='Greys')])
    layout = Layout(autosize=False,title=name)
    fig = Figure(data=data, layout=layout)

    return pl