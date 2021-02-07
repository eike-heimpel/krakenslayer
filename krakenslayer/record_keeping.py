class My_Ledger:

    def __init__(self):

        self.assets = {}
        self.trades = []

    def add_asset(self, asset):

         self.assets[asset.asset_pair] = asset

    def add_trade(self, trade_info):

        self.trades.append(trade_info)

