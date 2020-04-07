import sys
import os
from pymongo import MongoClient
from conf.bsv_tx_sync_conf import BsvTxSyncConf
import bitsv

if __name__ == '__main__':
    username = BsvTxSyncConf.username
    password = BsvTxSyncConf.password
    connectionstr = 'mongodb+srv://%s:%s@cluster0-xhjo9.mongodb.net/test?retryWrites=true&w=majority' % (username, password)
    print(connectionstr)
    mongo = MongoClient(connectionstr)

    addr = "mndvRsa9eyFDpyuUk5bnXwSyrDEZNhq138"
    record_address = mongo.test.transaction.find({"address": addr})
    if record_address.count() == 0:
        mongo.test.address.insert({"address": addr})

    tx_list = mongo.test.transaction.find({"address": addr})
    if tx_list.count() == 0:
        network_api = bitsv.network.NetworkAPI(network='test')
        bsv_transactions = network_api.get_transactions(addr)
        for txid in bsv_transactions:
            mongo.test.transaction.insert({"address": addr, "txid": txid})

    tx_list = mongo.test.transaction.find({"address": addr})
    for item in tx_list:
        print("txid:" + item["txid"])



    