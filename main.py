import requests

response = requests.get("https://playground.learnqa.ru/api/get_500")

print(response.text)