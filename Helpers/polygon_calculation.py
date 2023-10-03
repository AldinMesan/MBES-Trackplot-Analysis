from qgis.core import QgsVectorLayer, QgsGeometry, QgsFeature, QgsField
from qgis.PyQt.QtCore import QVariant


def calculate_polygons(trackplot_layer):
    # Create an output polygon layer
    polygon_layer = QgsVectorLayer("Polygon?crs=" + trackplot_layer.crs().authid(), "Polygons", "memory")
    provider = polygon_layer.dataProvider()
    provider.addAttributes([QgsField("Area", QVariant.Double), QgsField("Lines", QVariant.String)])
    polygon_layer.updateFields()

    # Calculate polygons for areas where the distance exceeds 50 meters between trackplots
    features = list(trackplot_layer.getFeatures())
    for i in range(len(features) - 1):
        for j in range(i + 1, len(features)):
            feature1 = features[i]
            feature2 = features[j]

            # Calculate distance between two trackplot points
            distance = feature1.geometry().distance(feature2.geometry())

            if distance > 50:
                # Create a polygon geometry
                polygon = QgsGeometry.fromPolygonXY(
                    [[feature1.geometry().asPoint(), feature2.geometry().asPoint(), feature1.geometry().asPoint()]])

                # Add polygon feature to the output layer
                new_feature = QgsFeature()
                new_feature.setGeometry(polygon)
                new_feature.setAttributes([polygon.area(), f"{feature1['Name']} - {feature2['Name']}"])
                provider.addFeature(new_feature)

    return polygon_layer
