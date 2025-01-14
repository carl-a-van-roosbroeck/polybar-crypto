#!/usr/bin/env python3

import configparser
import sys
import requests
from decimal import Decimal
from os.path import expanduser

config = configparser.ConfigParser()
icon_color = "#50fa7b"
round_symbol = False
round_symbol_precision = 3

# File must be opened with utf-8 explicitly
with open(expanduser('~/.config/polybar/modules/polybar-crypto/crypto-config'), 'r', encoding='utf-8') as f:
    config.read_file(f)

# Everything except the general section
currencies = [x for x in config.sections() if x != 'general']
base_currency = config['general']['base_currency']
params = {'convert': base_currency}
round_value = int(config['general']['round'])  # Extract the round value as an integer

for currency in currencies:
    try:
        icon = config[currency]['icon']
        color = config[currency]['color']
        colored_icon = f"%{{F{color}}}{icon}%{{F-}}"
        json = requests.get(f'https://api.coingecko.com/api/v3/coins/{currency}').json()["market_data"]
        local_price = round(Decimal(json["current_price"][f'{base_currency.lower()}']), 2)
        change_24 = float(json['price_change_percentage_24h'])
        # custom option, less precision
        if round_value > 0:
            change_24 = round(change_24, round_value)
        display_opt = config['general']['display']
        if display_opt == 'both' or display_opt == None:
            sys.stdout.write(f'{colored_icon} {local_price}/{change_24:+}%')
        elif display_opt == 'percentage':
            sys.stdout.write(f'{colored_icon} {change_24:+}%')
        elif display_opt == 'price':
            sys.stdout.write(f'{colored_icon} {local_price}')
        if currency != currencies[-1]:
            sys.stdout.write('  ')
    except requests.exceptions.ConnectionError as e:
        sys.stdout.write('not connected')
        break
