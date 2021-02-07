from krakenslayer.coins import Coin
from krakenslayer.record_keeping import My_Ledger


my_ledger = My_Ledger()

ether = Coin("ETH")
ada = Coin("ADA")

my_ledger.add_asset("Etherium", ether)
my_ledger.add_asset("Cardano", ada)

ada.update_asset_pair_info()

print(my_ledger.assets["Cardano"].last_traded_price)
