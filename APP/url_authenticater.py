from urllib.parse import urlparse, urljoin
from flask import request

# Lien pour la documentation:
# Vérification des redirections: 'https://web.archive.org/web/20120517003641/http://flask.pocoo.org/snippets/62/'
# Pour créer des fonction de décoration: 'https://realpython.com/primer-on-python-decorators/

domains = [
    "http://192.168.0.129:8080",
    "http://127.0.0.1:8080"
]

endpoints = [
    '/',
    '/main/secure',
    '/main/acceuil',

    '/recherches/secure',
    '/recherches/device_model',
    '/recherches/home',
    '/recherches/mission',
    '/recherches/origin',
    '/recherches/founders',
    '/recherches/process',
    '/recherches/documentation',
    '/recherches/FAQ',
]

Accepted_endpoints = [
    domain + endpoint
    for domain in domains
    for endpoint in endpoints
]

print(Accepted_endpoints)


# Cette fonction est pour vérifier si l'url de redirection est un url appartenant à notre serveur.
def is_url_safe(target):
    host_url = request.host_url
    print(host_url)
    reference_url = urlparse(host_url)
    test_http_link = urljoin(host_url, target)
    test_url = urlparse(test_http_link)
    
    print(test_url.scheme in ('http', 'https'), '1')
    print(reference_url.netloc == test_url.netloc, 2)
    print(test_http_link)
    print(test_http_link in Accepted_endpoints)
    
    return test_url.scheme in ('http', 'https') and reference_url.netloc == test_url.netloc and test_http_link in Accepted_endpoints


# Cette fonction permet de rediriger les utilisateurssi jamais l'url s'avère à ne pas appartenir à notre serveur.
# Cette une fonction dite "fallback" -> "plan de secours".
def redirect_back(target, redirect_back_endpoint):
    if not is_url_safe(target):
        print('url not secure')
        target = redirect_back_endpoint
        print(target)
    return target