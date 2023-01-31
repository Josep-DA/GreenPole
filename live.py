from time import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys


def get_data(path:str):
    with open(path, 'r') as file:
       return file.readlines()


chrome_driver_path = "F:/chromedriver/chromedriver.exe"

service_ = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service_)


driver.get("http://127.0.0.1:8080/main/acceuil")

# driver.close()

data = {
    "html": {
        "path": 'F:/E-commerce/Projet SJD-ART3D/SiteWeb/Flask/SiteWeb/App/main/templates/main/acceuil.html',
        "data": "",
        "isuptodate": ""
    },
    "css": {
        "path": 'F:/E-commerce/Projet SJD-ART3D/SiteWeb/Flask/SiteWeb/App/main/static/main/css/model.css',
        "data": "",
        "isuptodate": ""
    }
}

duration = ''
try:
    duration = int(sys.argv[1])
except IndexError:
    if not duration or not isinstance(duration, int) or duration == 0:
        duration = 2000

print(duration)

start = time()   

while not round(time() - start) >= duration:
    data["html"]["data"] = get_data(data["html"]["path"])
    data["css"]["data"] = get_data(data["css"]["path"])
       
    if data["html"]["isuptodate"] != data["html"]["data"]:
        data["html"]["isuptodate"] = get_data(data["html"]["path"])
        print('update')
        driver.get("http://127.0.0.1:8080/main/acceuil")

    if data["css"]["isuptodate"] != data["css"]["data"]:
        data["css"]["isuptodate"] = get_data(data["css"]["path"])
        print('update')
        driver.get("http://127.0.0.1:8080/main/acceuil")

print(round(time() - start) >= duration)
driver.quit()
