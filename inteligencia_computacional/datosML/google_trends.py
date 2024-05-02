from pytrends.request import TrendReq

# Configura la conexión con la API de Google Trends
pytrends = TrendReq()

# Especifica los términos de búsqueda y otros parámetros
kw_list = ["Bitcoin", "Cryptocurrency"]  # Términos de búsqueda
timeframe = "today 1-y"  # Período de tiempo (últimos 5 años)
geo = "US"  # País (Estados Unidos)

# Obtiene los datos de tendencias
pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo=geo)
trends_data = pytrends.interest_over_time()

# Muestra los datos de tendencias
print(trends_data.head())
