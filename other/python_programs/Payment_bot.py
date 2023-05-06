import requests
from bs4 import BeautifulSoup
response =  requests.get('https://www.kartable.fr/ressources/francais/cours/les-valeurs-de-lindicatif/16054')
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())