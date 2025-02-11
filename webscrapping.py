import requests
from bs4 import BeautifulSoup

def contar_encabezados(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error al acceder a la página: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    h1_count = len(soup.find_all('h1'))
    h2_count = len(soup.find_all('h2'))
    h3_count = len(soup.find_all('h3'))

    print(f"Cantidad de <h1>: {h1_count}")
    print(f"Cantidad de <h2>: {h2_count}")
    print(f"Cantidad de <h3>: {h3_count}")

url = "https://www.mercadolibre.com.co"
contar_encabezados(url)