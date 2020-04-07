import sys
import os
from pymongo import MongoClient
from conf.bsv_tx_sync_conf import BsvTxSyncConf

if __name__ == '__main__':
    username = BsvTxSyncConf.username
    password = BsvTxSyncConf.password
    connectionstr = 'mongodb+srv://%s:%s@cluster0-xhjo9.mongodb.net/test?retryWrites=true&w=majority' % (username, password)
    print(connectionstr)
    client = MongoClient(connectionstr)

    transaction = client.test.transaction.find()
    for item in transaction:
        print(item["txid"])