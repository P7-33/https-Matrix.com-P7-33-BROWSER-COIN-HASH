# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.base.exchange import Exchange
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import BadSymbol


class coincheck(Exchange):

    def describe(self):
        return self.deep_extend(super(coincheck, self).describe(), {
            'id': 'coincheck',
            'name': 'coincheck',
            'countries': ['JP', 'ID'],
            'rateLimit': 1500,
            'has': {
                'cancelOrder': True,
                'CORS': None,
                'createOrder': True,
                'fetchBalance': True,
                'fetchMyTrades': True,
                'fetchOpenOrders': True,
                'fetchOrderBook': True,
                'fetchTicker': True,
                'fetchTrades': True,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/51840849/87182088-1d6d6380-c2ec-11ea-9c64-8ab9f9b289f5.jpg',
                'api': 'https://coincheck.com/api',
                'www': 'https://coincheck.com',
                'doc': 'https://coincheck.com/documents/exchange/api',
                'fees': [
                    'https://coincheck.com/exchange/fee',
                    'https://coincheck.com/info/fee',
                ],
            },
            'api': {
                'public': {
                    'get': [
                        'exchange/orders/rate',
                        'order_books',
                        'rate/{pair}',
                        'ticker',
                        'trades',
                    ],
                },
                'private': {
                    'get': [
                        'accounts',
                        'accounts/balance',
                        'accounts/leverage_balance',
                        'bank_accounts',
                        'deposit_money',
                        'exchange/orders/opens',
                        'exchange/orders/transactions',
                        'exchange/orders/transactions_pagination',
                        'exchange/leverage/positions',
                        'lending/borrows/matches',
                        'send_money',
                        'withdraws',
                    ],
                    'post': [
                        'bank_accounts',
                        'deposit_money/{id}/fast',
                        'exchange/orders',
                        'exchange/transfers/to_leverage',
                        'exchange/transfers/from_leverage',
                        'lending/borrows',
                        'lending/borrows/{id}/repay',
                        'send_money',
                        'withdraws',
                    ],
                    'delete': [
                        'bank_accounts/{id}',
                        'exchange/orders/{id}',
                        'withdraws/{id}',
                    ],
                },
            },
            'markets': {
                'BTC/JPY': {'id': 'btc_jpy', 'symbol': 'BTC/JPY', 'base': 'BTC', 'quote': 'JPY', 'baseId': 'btc', 'quoteId': 'jpy', 'type': 'spot', 'spot': True},  # the only real pair
                # 'ETH/JPY': {'id': 'eth_jpy', 'symbol': 'ETH/JPY', 'base': 'ETH', 'quote': 'JPY', 'baseId': 'eth', 'quoteId': 'jpy'},
                'ETC/JPY': {'id': 'etc_jpy', 'symbol': 'ETC/JPY', 'base': 'ETC', 'quote': 'JPY', 'baseId': 'etc', 'quoteId': 'jpy', 'type': 'spot', 'spot': True},
                # 'DAO/JPY': {'id': 'dao_jpy', 'symbol': 'DAO/JPY', 'base': 'DAO', 'quote': 'JPY', 'baseId': 'dao', 'quoteId': 'jpy'},
                # 'LSK/JPY': {'id': 'lsk_jpy', 'symbol': 'LSK/JPY', 'base': 'LSK', 'quote': 'JPY', 'baseId': 'lsk', 'quoteId': 'jpy'},
                'FCT/JPY': {'id': 'fct_jpy', 'symbol': 'FCT/JPY', 'base': 'FCT', 'quote': 'JPY', 'baseId': 'fct', 'quoteId': 'jpy', 'type': 'spot', 'spot': True},
                'MONA/JPY': {'id': 'mona_jpy', 'symbol': 'MONA/JPY', 'base': 'MONA', 'quote': 'JPY', 'baseId': 'mona', 'quoteId': 'jpy', 'type': 'spot', 'spot': True},
                # 'XMR/JPY': {'id': 'xmr_jpy', 'symbol': 'XMR/JPY', 'base': 'XMR', 'quote': 'JPY', 'baseId': 'xmr', 'quoteId': 'jpy'},
                # 'REP/JPY': {'id': 'rep_jpy', 'symbol': 'REP/JPY', 'base': 'REP', 'quote': 'JPY', 'baseId': 'rep', 'quoteId': 'jpy'},
                # 'XRP/JPY': {'id': 'xrp_jpy', 'symbol': 'XRP/JPY', 'base': 'XRP', 'quote': 'JPY', 'baseId': 'xrp', 'quoteId': 'jpy'},
                # 'ZEC/JPY': {'id': 'zec_jpy', 'symbol': 'ZEC/JPY', 'base': 'ZEC', 'quote': 'JPY', 'baseId': 'zec', 'quoteId': 'jpy'},
                # 'XEM/JPY': {'id': 'xem_jpy', 'symbol': 'XEM/JPY', 'base': 'XEM', 'quote': 'JPY', 'baseId': 'xem', 'quoteId': 'jpy'},
                # 'LTC/JPY': {'id': 'ltc_jpy', 'symbol': 'LTC/JPY', 'base': 'LTC', 'quote': 'JPY', 'baseId': 'ltc', 'quoteId': 'jpy'},
                # 'DASH/JPY': {'id': 'dash_jpy', 'symbol': 'DASH/JPY', 'base': 'DASH', 'quote': 'JPY', 'baseId': 'dash', 'quoteId': 'jpy'},
                # 'ETH/BTC': {'id': 'eth_btc', 'symbol': 'ETH/BTC', 'base': 'ETH', 'quote': 'BTC', 'baseId': 'eth', 'quoteId': 'btc'},
                'ETC/BTC': {'id': 'etc_btc', 'symbol': 'ETC/BTC', 'base': 'ETC', 'quote': 'BTC', 'baseId': 'etc', 'quoteId': 'btc', 'type': 'spot', 'spot': True},
                # 'LSK/BTC': {'id': 'lsk_btc', 'symbol': 'LSK/BTC', 'base': 'LSK', 'quote': 'BTC', 'baseId': 'lsk', 'quoteId': 'btc'},
                # 'FCT/BTC': {'id': 'fct_btc', 'symbol': 'FCT/BTC', 'base': 'FCT', 'quote': 'BTC', 'baseId': 'fct', 'quoteId': 'btc'},
                # 'XMR/BTC': {'id': 'xmr_btc', 'symbol': 'XMR/BTC', 'base': 'XMR', 'quote': 'BTC', 'baseId': 'xmr', 'quoteId': 'btc'},
                # 'REP/BTC': {'id': 'rep_btc', 'symbol': 'REP/BTC', 'base': 'REP', 'quote': 'BTC', 'baseId': 'rep', 'quoteId': 'btc'},
                # 'XRP/BTC': {'id': 'xrp_btc', 'symbol': 'XRP/BTC', 'base': 'XRP', 'quote': 'BTC', 'baseId': 'xrp', 'quoteId': 'btc'},
                # 'ZEC/BTC': {'id': 'zec_btc', 'symbol': 'ZEC/BTC', 'base': 'ZEC', 'quote': 'BTC', 'baseId': 'zec', 'quoteId': 'btc'},
                # 'XEM/BTC': {'id': 'xem_btc', 'symbol': 'XEM/BTC', 'base': 'XEM', 'quote': 'BTC', 'baseId': 'xem', 'quoteId': 'btc'},
                # 'LTC/BTC': {'id': 'ltc_btc', 'symbol': 'LTC/BTC', 'base': 'LTC', 'quote': 'BTC', 'baseId': 'ltc', 'quoteId': 'btc'},
                # 'DASH/BTC': {'id': 'dash_btc', 'symbol': 'DASH/BTC', 'base': 'DASH', 'quote': 'BTC', 'baseId': 'dash', 'quoteId': 'btc'},
            },
            'fees': {
                'trading': {
                    'tierBased': False,
                    'percentage': True,
                    'maker': self.parse_number('0'),
                    'taker': self.parse_number('0'),
                },
            },
            'exceptions': {
                'exact': {
                    'disabled API Key': AuthenticationError,  # {"success":false,"error":"disabled API Key"}'
                    'invalid authentication': AuthenticationError,  # {"success":false,"error":"invalid authentication"}
                },
                'broad': {},
            },
        })

    def parse_balance(self, response):
        result = {'info': response}
        codes = list(self.currencies.keys())
        for i in range(0, len(codes)):
            code = codes[i]
            currency = self.currency(code)
            currencyId = currency['id']
            if currencyId in response:
                account = self.account()
                reserved = currencyId + '_reserved'
                account['free'] = self.safe_string(response, currencyId)
                account['used'] = self.safe_string(response, reserved)
                result[code] = account
        return self.safe_balance(result)

    async def fetch_balance(self, params={}):
        await self.load_markets()
        response = await self.privateGetAccountsBalance(params)
        return self.parse_balance(response)

    async def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        await self.load_markets()
        # Only BTC/JPY is meaningful
        market = None
        if symbol is not None:
            market = self.market(symbol)
        response = await self.privateGetExchangeOrdersOpens(params)
        rawOrders = self.safe_value(response, 'orders', [])
        parsedOrders = self.parse_orders(rawOrders, market, since, limit)
        result = []
        for i in range(0, len(parsedOrders)):
            result.append(self.extend(parsedOrders[i], {'status': 'open'}))
        return result

    def parse_order(self, order, market=None):
        #
        # fetchOpenOrders
        #
        #     {                       id:  202835,
        #                      order_type: "buy",
        #                            rate:  26890,
        #                            pair: "btc_jpy",
        #                  pending_amount: "0.5527",
        #       pending_market_buy_amount:  null,
        #                  stop_loss_rate:  null,
        #                      created_at: "2015-01-10T05:55:38.000Z"}
        #
        # todo: add formats for fetchOrder, fetchClosedOrders here
        #
        id = self.safe_string(order, 'id')
        side = self.safe_string(order, 'order_type')
        timestamp = self.parse8601(self.safe_string(order, 'created_at'))
        amount = self.safe_string(order, 'pending_amount')
        remaining = self.safe_string(order, 'pending_amount')
        price = self.safe_string(order, 'rate')
        status = None
        marketId = self.safe_string(order, 'pair')
        symbol = self.safe_symbol(marketId, market, '_')
        return self.safe_order({
            'id': id,
            'clientOrderId': None,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'amount': amount,
            'remaining': remaining,
            'filled': None,
            'side': side,
            'type': None,
            'timeInForce': None,
            'postOnly': None,
            'status': status,
            'symbol': symbol,
            'price': price,
            'stopPrice': None,
            'cost': None,
            'fee': None,
            'info': order,
            'average': None,
            'trades': None,
        }, market)

    async def fetch_order_book(self, symbol, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'pair': market['id'],
        }
        response = await self.publicGetOrderBooks(self.extend(request, params))
        return self.parse_order_book(response, symbol)

    async def fetch_ticker(self, symbol, params={}):
        if symbol != 'BTC/JPY':
            raise BadSymbol(self.id + ' fetchTicker() supports BTC/JPY only')
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'pair': market['id'],
        }
        ticker = await self.publicGetTicker(self.extend(request, params))
        timestamp = self.safe_timestamp(ticker, 'timestamp')
        last = self.safe_number(ticker, 'last')
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_number(ticker, 'high'),
            'low': self.safe_number(ticker, 'low'),
            'bid': self.safe_number(ticker, 'bid'),
            'bidVolume': None,
            'ask': self.safe_number(ticker, 'ask'),
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': self.safe_number(ticker, 'volume'),
            'quoteVolume': None,
            'info': ticker,
        }

    def parse_trade(self, trade, market=None):
        #
        # fetchTrades(public)
        #
        #      {
        #          "id": "206849494",
        #          "amount": "0.01",
        #          "rate": "5598346.0",
        #          "pair": "btc_jpy",
        #          "order_type": "sell",
        #          "created_at": "2021-12-08T14:10:33.000Z"
        #      }
        #
        # fetchMyTrades(private) - example from docs
        #
        #      {
        #          "id": 38,
        #          "order_id": 49,
        #          "created_at": "2015-11-18T07:02:21.000Z",
        #          "funds": {
        #              "btc": "0.1",
        #              "jpy": "-4096.135"
        #                  },
        #           "pair": "btc_jpy",
        #           "rate": "40900.0",
        #           "fee_currency": "JPY",
        #           "fee": "6.135",
        #           "liquidity": "T",
        #           "side": "buy"
        #      }
        #
        timestamp = self.parse8601(self.safe_string(trade, 'created_at'))
        id = self.safe_string(trade, 'id')
        priceString = self.safe_string(trade, 'rate')
        marketId = self.safe_string(trade, 'pair')
        market = self.safe_value(self.markets_by_id, marketId, market)
        symbol = None
        baseId = None
        quoteId = None
        if marketId is not None:
            if marketId in self.markets_by_id:
                market = self.markets_by_id[marketId]
                baseId = market['baseId']
                quoteId = market['quoteId']
                symbol = market['symbol']
            else:
                ids = marketId.split('_')
                baseId = ids[0]
                quoteId = ids[1]
                base = self.safe_currency_code(baseId)
                quote = self.safe_currency_code(quoteId)
                symbol = base + '/' + quote
        if symbol is None:
            if market is not None:
                symbol = market['symbol']
        takerOrMaker = None
        amountString = None
        costString = None
        side = None
        fee = None
        orderId = None
        if 'liquidity' in trade:
            if self.safe_string(trade, 'liquidity') == 'T':
                takerOrMaker = 'taker'
            elif self.safe_string(trade, 'liquidity') == 'M':
                takerOrMaker = 'maker'
            funds = self.safe_value(trade, 'funds', {})
            amountString = self.safe_string(funds, baseId)
            costString = self.safe_string(funds, quoteId)
            fee = {
                'currency': self.safe_string(trade, 'fee_currency'),
                'cost': self.safe_string(trade, 'fee'),
            }
            side = self.safe_string(trade, 'side')
            orderId = self.safe_string(trade, 'order_id')
        else:
            amountString = self.safe_string(trade, 'amount')
            side = self.safe_string(trade, 'order_type')
        return self.safe_trade({
            'id': id,
            'info': trade,
            'datetime': self.iso8601(timestamp),
            'timestamp': timestamp,
            'symbol': symbol,
            'type': None,
            'side': side,
            'order': orderId,
            'takerOrMaker': takerOrMaker,
            'price': priceString,
            'amount': amountString,
            'cost': costString,
            'fee': fee,
        }, market)

    async def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        response = await self.privateGetExchangeOrdersTransactions(self.extend({}, params))
        #
        #      {
        #          "success": True,
        #          "transactions": [
        #                              {
        #                                  "id": 38,
        #                                  "order_id": 49,
        #                                  "created_at": "2015-11-18T07:02:21.000Z",
        #                                  "funds": {
        #                                      "btc": "0.1",
        #                                      "jpy": "-4096.135"
        #                                          },
        #                                  "pair": "btc_jpy",
        #                                  "rate": "40900.0",
        #                                  "fee_currency": "JPY",
        #                                  "fee": "6.135",
        #                                  "liquidity": "T",
        #                                  "side": "buy"
        #                               },
        #                          ]
        #      }
        #
        transactions = self.safe_value(response, 'transactions', [])
        return self.parse_trades(transactions, market, since, limit)

    async def fetch_trades(self, symbol, since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'pair': market['id'],
        }
        if limit is not None:
            request['limit'] = limit
        response = await self.publicGetTrades(self.extend(request, params))
        #
        #      {
        #          "id": "206849494",
        #          "amount": "0.01",
        #          "rate": "5598346.0",
        #          "pair": "btc_jpy",
        #          "order_type": "sell",
        #          "created_at": "2021-12-08T14:10:33.000Z"
        #      }
        #
        data = self.safe_value(response, 'data', [])
        return self.parse_trades(data, market, since, limit)

    async def create_order(self, symbol, type, side, amount, price=None, params={}):
        await self.load_markets()
        request = {
            'pair': self.market_id(symbol),
        }
        if type == 'market':
            order_type = type + '_' + side
            request['order_type'] = order_type
            prefix = (order_type + '_') if (side == 'buy') else ''
            request[prefix + 'amount'] = amount
        else:
            request['order_type'] = side
            request['rate'] = price
            request['amount'] = amount
        response = await self.privatePostExchangeOrders(self.extend(request, params))
        id = self.safe_string(response, 'id')
        return {
            'info': response,
            'id': id,
        }

    async def cancel_order(self, id, symbol=None, params={}):
        request = {
            'id': id,
        }
        return await self.privateDeleteExchangeOrdersId(self.extend(request, params))

    def nonce(self):
        return self.milliseconds()

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'] + '/' + self.implode_params(path, params)
        query = self.omit(params, self.extract_params(path))
        if api == 'public':
            if query:
                url += '?' + self.urlencode(query)
        else:
            self.check_required_credentials()
            nonce = str(self.nonce())
            queryString = ''
            if method == 'GET':
                if query:
                    url += '?' + self.urlencode(self.keysort(query))
            else:
                if query:
                    body = self.urlencode(self.keysort(query))
                    queryString = body
            auth = nonce + url + queryString
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'ACCESS-KEY': self.apiKey,
                'ACCESS-NONCE': nonce,
                'ACCESS-SIGNATURE': self.hmac(self.encode(auth), self.encode(self.secret)),
            }
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, httpCode, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is None:
            return
        #
        #     {"success":false,"error":"disabled API Key"}'
        #     {"success":false,"error":"invalid authentication"}
        #
        success = self.safe_value(response, 'success', True)
        if not success:
            error = self.safe_string(response, 'error')
            feedback = self.id + ' ' + self.json(response)
            self.throw_exactly_matched_exception(self.exceptions['exact'], error, feedback)
            self.throw_broadly_matched_exception(self.exceptions['broad'], body, feedback)
            raise ExchangeError(self.id + ' ' + self.json(response))
