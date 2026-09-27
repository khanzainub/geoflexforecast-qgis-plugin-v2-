from qgis.core import QgsApplication
from .processing_provider.provider import GeoFlexForecastProvider


class GeoFlexForecastPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.provider = None

    def initProcessing(self):
        self.provider = GeoFlexForecastProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()

    def unload(self):
        if self.provider is not None:
            QgsApplication.processingRegistry().removeProvider(self.provider)
