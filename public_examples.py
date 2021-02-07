from krakenslayer.coins import Coin
from krakenslayer.record_keeping import My_Ledger
import krakenex
from pprint import pprint


my_ledger = My_Ledger()

ether = Coin("ETH", "EUR")
ada = Coin("ADA", "EUR")

my_ledger.add_asset(ether)
my_ledger.add_asset(ada)

ada.update_asset_pair_info()

kraken = krakenex.API()
kraken.load_key('kraken.key')


## lets trade some

order_ids = []
# assume we placed multiple market orders here and added the ordertxid

# now we need to check the trade history until we see all orders fulfilled so we can log them.
trade_history = kraken.query_private("TradesHistory")["result"]

for trade_id, trade in trade_history["trades"].items():
    if trade["ordertxid"] in order_ids:
        current_coin = my_ledger.assets[trade["pair"]]
        my_ledger.add_trade(trade)
        current_coin.update_with_new_trade(trade)

        order_ids.remove(trade["ordertxid"])



