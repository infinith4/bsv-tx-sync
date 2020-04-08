import sys
import os
from pymongo import MongoClient
from conf.bsv_tx_sync_conf import BsvTxSyncConf
import bitsv
from lib.whats_on_chain_lib import WhatsOnChainLib
import logging

if __name__ == '__main__':
    username = BsvTxSyncConf.username
    password = BsvTxSyncConf.password
    connectionstr = 'mongodb+srv://%s:%s@cluster0-xhjo9.mongodb.net/test?retryWrites=true&w=majority' % (username, password)
    print(connectionstr)
    mongo = MongoClient(connectionstr)

    addr = "mndvRsa9eyFDpyuUk5bnXwSyrDEZNhq138"
    record_address = mongo.test.address.find({"address": addr})
    if record_address.count() == 0:
        mongo.test.address.insert({"address": addr})

    ## search woc network during xx minutes
    network_api = bitsv.network.NetworkAPI(network='test')
    bsv_transactions = network_api.get_transactions(addr)
    for txid in bsv_transactions:
        record_tx = mongo.test.transaction.find_one({"address": addr, "txid": txid})
        if record_tx == None:
            responseTx = WhatsOnChainLib.get_textdata(txid)
            if responseTx != None and responseTx.data != "":
                mongo.test.transaction.insert({"address": addr, "txid": txid})



    