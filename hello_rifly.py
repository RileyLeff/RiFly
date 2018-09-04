import requests

r = requests.get('https://www.southwest.com/air/check-in/index.html')

print(r.text)
