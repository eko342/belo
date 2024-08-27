import asyncio
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import RecaptchaV2ProxylessRequest

app = Flask(__name__)

API_KEY = "" # website api key buraya site kütüphanelerden bulursunuz zaten


url = "https://www.mtvodemeleri.web.tr/vergi/internet-mtv-borc-sorgulama-ve-odeme"


client_options = ClientOptions(api_key=API_KEY)
cap_monster_client = CapMonsterClient(options=client_options)


async def solve_captcha():
    recaptcha2request = RecaptchaV2ProxylessRequest(
        websiteUrl=url,
        websiteKey="6LfKvB8UAAAAANG3nfiIVu2KlyqAsWuCcRhrYRd1"  # websiteapikey budur gençlersiteye göre değişiklik gösterir
    )
    return await cap_monster_client.solve_captcha(recaptcha2request)

@app.route('/main', methods=['GET'])
def main():
    plaka = request.args.get('plaka')
    if not plaka:
        return jsonify({"error": "Plaka belirtilmedi."}), 400


    response = requests.get(url)


    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')
        

        token_element = soup.find('input', {'name': '__RequestVerificationToken'})
        
        if token_element:

            token_value = token_element.get('value')
        else:
            return jsonify({"error": "Token bulunamadı."}), 500
    else:
        return jsonify({"error": f"İstek başarısız oldu. HTTP Status Code: {response.status_code}"}), 500


    responses = asyncio.run(solve_captcha())
    captcha_response = responses.get("gRecaptchaResponse")

    post_data = {
        'aboneno1': plaka,
        'aboneno2': plaka,
        'aboneno3': '2024',
        'g-recaptcha-response': captcha_response,
        'kvkk': 'on',
        '__RequestVerificationToken': token_value
    }


    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'tr,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.mtvodemeleri.web.tr',
        'Referer': url,
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    post_response = requests.post(url, headers=headers, data=post_data)


    soup = BeautifulSoup(post_response.text, 'html.parser')


    table = soup.find('table', {'id': 'faturalist'})
    data2 = []
    if table:
        rows = table.find_all('tr', {'data-type': 'Data'})
        
        for row in rows:
            cols = row.find_all('td')
            son_odeme_tarihi = cols[1].text.strip()
            borc = cols[2].text.strip()
            donem = cols[3].text.strip()
            aciklama = cols[4].text.strip()
            
            data2.append({
                "Son Ödeme Tarihi": son_odeme_tarihi,
                "Borc": borc,
                "Dönem": donem,
                "Açıklama": aciklama
            })
    else:
        return jsonify({"error": "Tablo bulunamadı."}), 500


    div_content = soup.find('div', {'class': 'alert alert-success margin-bottom-10'}).decode_contents()
    data1 = {}
    try:
        kurum = div_content.split('<strong>Kurum : </strong>')[1].split('<span>')[1].split('</span>')[0].strip()
        sorgulanan_numara = div_content.split('<strong>Sorgulanan Numara : </strong>')[1].split('<span>')[1].split('</span>')[0].strip()
        abone = div_content.split('<strong>Abone : </strong>')[1].split('<span>')[1].split('</span>')[0].strip()

        data1 = {
            "Kurum": kurum,
            "Sorgulanan Numara": sorgulanan_numara,
            "Abone": abone
        }
        info = {
        "api oner": " legali & canlaryakan",
        "channel": "@cyberarsiv",
        "ufakinfo": "bana site verin size apisi çekip src salayım tg @canlaryakan",

        }
    except IndexError as e:
        return jsonify({"error": f"İçerik ayrıştırma sırasında bir hata oluştu: {e}"}), 500

#result bu gençler isteğe göre ekleme veya silme yapınız
    result = {
        "succes":True,
        "info": info,
        "data1": data1,
        "data2": data2
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
