from qgis.core import QgsProcessingProvider
from .forecast_algorithm import RasterTimeSeriesForecastAlgorithm


class GeoFlexForecastProvider(QgsProcessingProvider):
    def id(self):
        return "geoflexforecast"

    def name(self):
        return "GeoFlexForecast"

    def longName(self):
        return "GeoFlexForecast — Raster Time-Series Forecasting"

    def loadAlgorithms(self):
        self.addAlgorithm(RasterTimeSeriesForecastAlgorithm())
