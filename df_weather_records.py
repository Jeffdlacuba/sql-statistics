import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página con los datos del clima
url = "https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html"

# Descargar el contenido de la página
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# Encontrar la tabla con id="weather_records"
table = soup.find("table", attrs={"id": "weather_records"})

# Convertir la tabla en un DataFrame de Pandas
weather_records = pd.read_html(str(table))[0]

# Imprimir el DataFrame completo
print(weather_records)
