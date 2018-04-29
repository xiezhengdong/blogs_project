from django.test import TestCase

# -*- coding:utf-8 -*-
import os,json
import pymongo
from concurrent.futures import  ThreadPoolExecutor


class Aanyen(object):
    def __init__(self):
        self.date_tr = {'qw':'FM','wg':'WG'}
        self.client = pymongo.MongoClient('jmongo-hb1-prod-mongo-wrh71cm1sq1.jmiss.jcloud.com')
        self.client.wtoip_yun_patent.authenticate('wtoip_yun_patent', '1x1NsMpJrCUmTknl',mechanism='SCRAM-SHA-1')

    def retion(self):
        db = self.client['wtoip_yun_patent']
        collection = db['pdf_name_da']
        cc = collection.find({})
        return cc
    def gt(self,na):
        db = self.client['wtoip_yun_patent']
        collection = db['pdf_name_qc']
        collection.insert(na)


    def celue(self):
        set_r = {'{"name" : "000000_20170215_0C_CN_0.pdf","type" : "FM","path" : "2017/001/753/998/}'}
        date = self.retion()
        #print(date)
        try:
            for n,i in  enumerate(date):
                del i['_id']
                print(n,i)
                set_r.add(str(i))
            print('#########################################')
            for m,j in enumerate(set_r):
                dict_r = json.loads(j)

                print(m,dict_r)
                self.gt(dict_r)
        except Exception as e:
            print(e)


if __name__ =="__main__":
    r = Aanyen()

    #r.quchong()
    r.celue()
