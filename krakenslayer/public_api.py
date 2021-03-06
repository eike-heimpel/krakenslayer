import krakenex
from pprint import pprint


kraken = krakenex.API()

class Coin:

    def __init__(self, coin_ticker):
        self.coin_ticker = coin_ticker
        self.asset_pair = f"{coin_ticker}USDT"
        self.last_traded_price = None
        self.minimum_order_volume = None
        self.maximum_trading_fee = None
        self.lot_multiplier = None

    def update_asset_pair_infos(self):

        self._update_last_traded_price()

        asset_pair_info = kraken.query_public("AssetPairs", {"pair": self.asset_pair})
        self._check_for_unknwown_asset_pair_error(asset_pair_info)

        self.minimum_order_volume = asset_pair_info["result"][self.asset_pair]["ordermin"]
        self.maximum_trading_fee = asset_pair_info["result"][self.asset_pair]["fees"][0][1]
        self.lot_multiplier = asset_pair_info["result"][self.asset_pair]["lot_multiplier"]  # BEFORE EACH TRADE CHECK IF THE LOT MULTIPLIER IS 1 OTHERWISE DONT TRADE/ALERT. COULD COST MONEY


    def _update_last_traded_price(self):

        asset_pair_ticker = kraken.query_public("Ticker", {"pair": self.asset_pair})

        self._check_for_unknwown_asset_pair_error(asset_pair_ticker)

        self.last_traded_price = asset_pair_ticker["result"][self.asset_pair]["c"][0]


    def _check_for_unknwown_asset_pair_error(self, api_asset_response):

        if "EQuery:Unknown asset pair" in api_asset_response["error"]:
            raise Exception(f"{api_asset_response} asset pair does not exist")

