from krakenslayer.public_api import Coin

ether = Coin("ETH")
print(ether.maximum_trading_fee)
print(ether.last_traded_price)
ether.update_asset_pair_infos()
print(ether.maximum_trading_fee)
print(ether.last_traded_price)
