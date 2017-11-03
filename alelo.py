import sys

import requests
from bs4 import BeautifulSoup

from alelo_ticket import get_alelo_ticket


def get_alelo_balance(ticket):
    BASE_URL = 'https://www.cartoesbeneficio.com.br/inst/convivencia/SaldoExtratoAlelo.jsp?ticket={ticket}&primeiroAcesso=S&origem=Alelo'
    url = BASE_URL.format(ticket=ticket)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html5lib')

    div_card_balance = soup.find('div', class_='bt-saldo')
    alelo_balance = div_card_balance.find('strong').text

    return alelo_balance


if __name__ == '__main__':
    ticket = None

    if len(sys.argv) > 1:
        ticket = sys.argv[1]

    if not ticket:
        print('Insira o número do cartão (somente números)')
        card_number = input()
        ticket = get_alelo_ticket(card_number) 

    print(get_alelo_balance(ticket))
