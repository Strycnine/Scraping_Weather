import urllib.request
from bs4 import BeautifulSoup

header = "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'"

def temp(city):
    url = 'https://google.com/search?q=weather+in+' + city
    request = urllib.request.Request(url)
    request.add_header('User-Agent', header)
    response = urllib.request.urlopen(request).read()
    html = response.decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.select("#search span.TVtOme")
    ville = soup.select("#search div.mfMhoc")
    return('\n' + ville[0].text + ' : ' + temp[0].text)

while True:
    print('\n \n')
    city = input('Ville ? ')
    city = city.replace(' ', '+')
    print(temp(city) + '°C')
