import krakenex
import logging
import sys


kraken = krakenex.API()

class Coin:

    def __init__(self, coin_ticker):
        self.coin_ticker = coin_ticker
        self.asset_pair_ticker = f"{coin_ticker}USDT"
        self.last_traded_price = None
        self.minimum_volume = None

    def update_last_traded_price(self):

        asset_pair_ticker = kraken.query_public("Ticker", {"pair": self.asset_pair_ticker})

        if "EQuery:Unknown asset pair" in asset_pair_ticker["error"]:
            raise Exception(f"{self.asset_pair_ticker} asset pair does not exist")

        self.last_traded_price = asset_pair_ticker["result"][self.asset_pair_ticker]["c"][0]

    def update_minimum_volume(self, asset_pair):

        asset_pair_info = kraken.query_public("AssetPairs", {"pair": asset_pair})

        if "EQuery:Unknown asset pair" in asset_pair_info["error"]:
            raise Exception(f"{asset_pair} asset pair does not exist")

        self.asset_pair_result = asset_pair_info["result"][asset_pair]

    
    def _check_for_unknwown_error(self):

ether = Coin("ETH")
print(ether.last_traded_price)
ether.update_last_traded_price()
print(ether.last_traded_price)

exit()

class PublicAPI:

    def __init__(self):
        self.kraken = krakenex.API()

    def asset_pair_last_price(self, asset_pair):  # Sounds like asset should be a class

        asset_pair_ticker = self.kraken.query_public("Ticker", {"pair": asset_pair})

        if "EQuery:Unknown asset pair" in asset_pair_ticker["error"]:
            raise Exception(f"{asset_pair} asset pair does not exist")

        asset_price_euro = asset_pair_ticker["result"][asset_pair]["c"][0]

        return asset_price_euro

    def asset_pair_trading_minimum(self, asset_pair):

        asset_pair_info = self.kraken.query_public("AssetPairs", {"pair": asset_pair})

        if "EQuery:Unknown asset pair" in asset_pair_info["error"]:
            raise Exception(f"{asset_pair} asset pair does not exist")

        self.asset_pair_result = asset_pair_info["result"][asset_pair]


p = PublicAPI()

p.asset_pair_trading_minimum("XETHZEUR")
print(p.asset_pair_result)