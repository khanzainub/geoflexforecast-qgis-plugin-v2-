def classFactory(iface):
    from .plugin import GeoFlexForecastPlugin
    return GeoFlexForecastPlugin(iface)
