# -*- coding: utf-8 -*-

import ccxtpro
from asyncio import gather, get_event_loop


async def symbol_loop(exchange, method, symbol):
    print('Starting', exchange.id, method, symbol)
    while True:
        try:
            response = await getattr(exchange, method)(symbol)
            now = exchange.milliseconds()
            iso8601 = exchange.iso8601(now)
            if method == 'watchOrderBook':
                print(iso8601, exchange.id, method, symbol, response['asks'][0], response['bids'][0])
            elif method == 'watchTicker':
                print(iso8601, exchange.id, method, symbol, response['high'], response['low'], response['bid'], response['ask'])
            elif method == 'watchTrades':
                print(iso8601, exchange.id, method, symbol, len(response), 'trades')
        except Exception as e:
            print(str(e))
            # raise e  # uncomment to break all loops in case of an error in any one of them
            break  # you can break just this one loop if it fails


async def symbols_method_loop(exchange, method, symbols):
    print('Starting', exchange.id, method, symbols)
    loops = [symbol_loop(exchange, method, symbol) for symbol in symbols]
    await gather(*loops)


async def method_loop(exchange, method):
    print('Starting', exchange.id, method)
    while True:
        try:
            response = await getattr(exchange, method)()
            now = exchange.milliseconds()
            iso8601 = exchange.iso8601(now)
            print(iso8601, exchange.id, method, response)
        except Exception as e:
            print(str(e))
            # raise e  # uncomment to break all loops in case of an error in any one of them
            break  # you can break just this one loop if it fails


async def exchange_loop(asyncio_loop, exchange_id, methods, config={}):
    print('Starting', exchange_id, methods)
    exchange = getattr(ccxtpro, exchange_id)({
        'enableRateLimit': True,
        'asyncio_loop': asyncio_loop,
    })
    for attr, value in config.items():
        setattr(exchange, attr, value)
    loops = [symbols_method_loop(exchange, method, symbols) if len(symbols) else method_loop(exchange, method) for method, symbols in methods.items()]
    await gather(*loops)
    await exchange.close()


async def main(asyncio_loop):
    keys = {
        'okex': {
            'apiKey': 'YOUR_API_KEY',
            'secret': 'YOUR_SECRET',
        },
        'binance': {
            'apiKey': 'YOUR_API_KEY',
            'secret': 'YOUR_SECRET',
        },
    }
    exchanges = {
        'okex': {
            'watchOrderBook': ['BTC/USDT', 'ETH/BTC', 'ETH/USDT'],
            'watchTicker': ['BTC/USDT'],
            'watchBalance': [],
        },
        'binance': {
            'watchOrderBook': ['BTC/USDT', 'ETH/BTC'],
            'watchTrades': [ 'ETH/BTC' ],
            'watchBalance': [],
        },
    }
    loops = [exchange_loop(asyncio_loop, exchange_id, methods, keys.get(exchange_id, {})) for exchange_id, methods in exchanges.items()]
    await gather(*loops)


if __name__ == '__main__':
    asyncio_loop = get_event_loop()
    asyncio_loop.run_until_complete(main(asyncio_loop))
