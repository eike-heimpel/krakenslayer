from krakenslayer.api import Coin

ether = Coin("ETH")
ada = Coin("ADA")

ada.update_asset_pair_info()
print(ada.last_traded_price)
