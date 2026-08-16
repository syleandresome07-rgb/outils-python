import requests

url = "https://api.open-meteo.com/v1/forecast"
parametres = {
    "latitude": 12.37,
    "longitude": -1.53,
    "current_weather": True,
}

reponse = requests.get(url, params=parametres)
print(reponse.status_code)   # doit afficher 200

donnees = reponse.json()     # convertit directement la réponse en dict Python
print(donnees["current_weather"]["temperature"])
