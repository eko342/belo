import requests
import time
import json
from bs4 import BeautifulSoup
import schedule

def fetch_viewstate(url):
    # İlk isteği yaparak ViewState ve diğer parametreleri alın
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # ViewState ve diğer parametreleri HTML içinden çıkarın
    viewstate = soup.find('input', {'name': '__VIEWSTATE'})['value']
    viewstate_generator = soup.find('input', {'name': '__VIEWSTATEGENERATOR'})['value']
    event_target = 'girisButton'
    event_argument = ''
    session = requests.Session()  # Session ile çerezleri yönetin

    return viewstate, viewstate_generator, event_target, event_argument, session

def login(url, viewstate, viewstate_generator, event_target, event_argument, session):
    # Giriş işlemini yaparak sonuçları ve çerezleri alın
    data = {
        '__EVENTTARGET': event_target,
        '__EVENTARGUMENT': event_argument,
        '__VIEWSTATE': viewstate,
        '__VIEWSTATEGENERATOR': viewstate_generator,
        'uyeAdi': 'furkankanadikirik',
        'sifre': '12345',
        'tbSmsCode': '',
        'DXScript': '1_304,1_185,1_298,1_211,1_188,1_182,1_290,1_288',
        'DXCss': '0_2517,1_50,1_53,1_51,0_2522,0_5657,1_16,0_2445,css/bootstrap.min.css,css/bootstrap-theme.min.css,css/font-awesome.css,css/font-awesome.min.css,css/main.css,css/custom-sky-forms.css,css/style.css,http://fonts.googleapis.com/css?family=Monda'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': url,
        'Referer': url,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    
    response = session.post(url, data=data, headers=headers)
    
    if response.ok:
        cookies = session.cookies.get_dict()
        with open('cookies.json', 'w') as f:
            json.dump(cookies, f, indent=4)
        print('Giriş başarılı, çerezler kaydedildi.')
    else:
        print('Giriş başarısız. Durum kodu:', response.status_code)

def job():
    url = 'https://bys.onikisubat.bel.tr/SistemeGiris.aspx'
    viewstate, viewstate_generator, event_target, event_argument, session = fetch_viewstate(url)
    if viewstate and viewstate_generator:
        login(url, viewstate, viewstate_generator, event_target, event_argument, session)

# İlk işleme hemen başla
job()

# Daha sonra her 5 dakikada bir devam et
schedule.every(5).minutes.do(job)

print("Scheduler started. Press Ctrl+C to exit.")
while True:
    schedule.run_pending()
    time.sleep(1)
