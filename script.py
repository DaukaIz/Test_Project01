import sys
import requests


r = requests.get("https://coreyms.com")
print(r.status_code)
print("Hi my name is !!")
