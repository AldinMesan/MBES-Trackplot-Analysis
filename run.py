from qgis.core import QgsApplication, QgsVectorLayer
from qgis.PyQt.QtCore import QgsProject
from Helpers.polygon_calculation import calculate_polygons
# Initialize QGIS
qgs = QgsApplication([], False)
qgs.initQgis()

# Load the trackplot layer from the "Input" folder
input_trackplot_path = 'Input/trackplot.shp'
trackplot_layer = QgsVectorLayer(input_trackplot_path, "Trackplot", "ogr")

if not trackplot_layer.isValid():
    print("Error: Unable to load trackplot layer")
    exit()

# Calculating polygons
polygon_layer = calculate_polygons(trackplot_layer)

# Save the calculated polygons as a shapefile in the "Output" folder
output_polygon_path = 'Output/calculated_polygons.shp'
QgsVectorLayer.writeFile(polygon_layer, output_polygon_path, "utf-8")

# Add the calculated polygons to the QGIS project
QgsProject.instance().addMapLayer(polygon_layer)

# Exit QGIS
qgs.exitQgis()
