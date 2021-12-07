import time
import requests
import pymysql
import pandas as pd
import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode


# address
def get_balance():  # CTO
    payload = {
        'access_key': 'E8wyyyo54ZaQRuP7daxpGkLntWnrTj1mKqfBwSjO',
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, 'NDSucxWG0lA3Fxq8KZCtuAzxL7EGlONRbc8YOSIc')
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {'Authorization': authorize_token}

    res = requests.get('https://api.upbit.com/v1/accounts', headers=headers)
    account = res.json()

    return account


def ceo_balance():
    payload = {
        'access_key': 'J4djQbu6GvN7xDeiccllQBtK3Gcq6bJ2uxonpyIv',
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, 'jQnhUwhVrkD7I5Xk6XovkkD7x6XdlzUScFJvFF0l')
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {'Authorization': authorize_token}

    res = requests.get('https://api.upbit.com/v1/accounts', headers=headers)
    account = res.json()

    return account


# order
def get_order(side, count, price, order_type, coin_name):
    query = {
        'market': coin_name,
        'side': side,  # 매수: bid, 매도: ask
        'volume': count,
        'price': price,
        'ord_type': order_type,  # 지정가 주문: limit, 시장가 주문(매수): price, 시장가 주문(매도): market
    }
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': 'E8wyyyo54ZaQRuP7daxpGkLntWnrTj1mKqfBwSjO',
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, 'NDSucxWG0lA3Fxq8KZCtuAzxL7EGlONRbc8YOSIc')
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {'Authorization': authorize_token}

    res = requests.post('https://api.upbit.com/v1/orders', params=query, headers=headers)
    res = res.json()

    return res['uuid']


def ceo_order(side, count, price, order_type, coin_name):
    query = {
        'market': coin_name,
        'side': side,  # 매수: bid, 매도: ask
        'volume': count,
        'price': price,
        'ord_type': order_type,  # 지정가 주문: limit, 시장가 주문(매수): price, 시장가 주문(매도): market
    }
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': 'J4djQbu6GvN7xDeiccllQBtK3Gcq6bJ2uxonpyIv',
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, 'jQnhUwhVrkD7I5Xk6XovkkD7x6XdlzUScFJvFF0l')
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {'Authorization': authorize_token}

    res = requests.post('https://api.upbit.com/v1/orders', params=query, headers=headers)
    res = res.json()

    return res['uuid']


# run process
def main():
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 120)

    while True:
        coin_code = []

        market_url = 'https://api.upbit.com/v1/market/all'
        querystring = {'isDetails': 'false'}
        response = requests.request('GET', market_url, params=querystring)
        markets = response.json()

        for coins in markets:
            if coins['market'].split('-')[0] == 'KRW':
                coin_code.append(coins['market'])

        for coin_name in coin_code:
            candle_url = 'https://api.upbit.com/v1/candles/minutes/5'
            querystring = {'market': coin_name, 'count': '10'}
            response = requests.request('GET', candle_url, params=querystring)
            candles = response.json()

            rate_url = 'https://api.upbit.com/v1/candles/days'
            rate_querystring = {'market': coin_name, 'count': '1'}
            response = requests.request('GET', rate_url, params=rate_querystring)
            rates = response.json()

            result = pd.DataFrame(candles)[::-1]
            result = result.drop(['unit', 'candle_date_time_utc', 'timestamp', 'candle_acc_trade_price', 'candle_acc_trade_volume', 'opening_price'], axis=1).rename(columns={'trade_price': 'close_price'})
            result['low'] = result['low_price'].rolling(window=5).min()
            result['high'] = result['high_price'].rolling(window=5).max()
            result['rate'] = rates[0]['change_rate'] * 100
            result['average_n'] = ((result['close_price'] - result['low']) / (result['high'] - result['low'])) * 100
            result['average_k'] = result['average_n'].rolling(window=3).mean()  # red
            result['average_d'] = result['average_k'].rolling(window=3).mean()  # blue

            ceo_accounts = ceo_balance()

            for account in ceo_accounts:
                if account['currency'] != 'KRW':
                    currency = 'KRW-' + account['currency']
                    ceo_order('ask', account['balance'], '', 'market', currency)
                    print(currency)
            exit()


if __name__ == '__main__':
    main()