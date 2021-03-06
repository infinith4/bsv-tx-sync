import sys
import os
from pymongo import MongoClient
from conf.bsv_tx_sync_conf import BsvTxSyncConf
import bitsv
from libraries.whats_on_chain_lib import WhatsOnChainLib
import logging

if __name__ == '__main__':
    username = BsvTxSyncConf.username
    password = BsvTxSyncConf.password
    connectionstr = 'mongodb+srv://%s:%s@cluster0-xhjo9.mongodb.net/test?retryWrites=true&w=majority' % (username, password)
    print(connectionstr)
    mongo = MongoClient(connectionstr)

    record_address = mongo.test.address.find()
    for item in record_address:
        addr = item['address']
        print("addr:" + addr)
        ## search woc network during xx minutes
        # if get_textdata is None, not insert to db
        network_api = bitsv.network.NetworkAPI(network='test')
        bsv_transactions = network_api.get_transactions(addr)
        for txid in bsv_transactions:
            print("txid:" + txid)
            record_tx = mongo.test.transaction.find_one({"address": addr, "txid": txid})
            print(record_tx)
            if record_tx == None:
                responseTx = WhatsOnChainLib.get_textdata(txid)
                if responseTx != None and responseTx.data != "":
                    mongo.test.transaction.insert({"address": addr, "txid": txid})
                    print("inserted")


    