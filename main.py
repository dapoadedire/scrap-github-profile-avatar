import requests
from bs4 import BeautifulSoup
import urllib.request


github_user = input('Input your github username: ')
url = 'https://github.com/' + github_user

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
profile_image = soup.find('img', {'class': 'avatar'})

image_url = profile_image.get('src')
try:
    filename = 'profile_image.jpg'
    urllib.request.urlretrieve(image_url, filename)

except:
    print ('Could not retrieve profile image')