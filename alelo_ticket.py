import sys

import requests
from bs4 import BeautifulSoup
from PIL import Image

def get_alelo_ticket(card_number):
    URL = 'https://www.meualelo.com.br'
    post_url = 'https://www.meualelo.com.br/SaldoExtratoValidacaoServlet'

    session = requests.Session()
    response = session.get(URL)
    soup = BeautifulSoup(response.text, 'html5lib')
    img = soup.find(id='imgCaptcha')
    image_url = URL + img['src']

    img = Image.open(session.get(image_url, stream=True).raw)
    img.show()

    print('Digite o captcha:')
    captcha = input()

    data = {
        'txtCartao1': card_number,
        'captcha': captcha,
    }
    response = session.post(url=post_url, data=data)

    soup = BeautifulSoup(response.text, 'html5lib')
    iframes = soup.find_all('iframe')
    ticket = iframes[0].get('src').split('=')[1]

    return ticket

if __name__ == '__main__':
    card_number = None

    if len(sys.argv) > 1:
        card_number = sys.argv[1]

    if not card_number:
        print('Insira o número do cartão (somente números)')
        card_number = input()

    print(get_alelo_ticket(card_number))
