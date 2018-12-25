# -*- coding:utf-8 -*-
'''

Created on Dec 22, 2018

@author:  Tender Xie
@group:  DearBao
@contact: 396934200@qq.com
@public weixin: 笛尔宝
'''

from collections import ChainMap

STOCK_ALIAS = {'sh': 'sh000001', 'sz': 'sz399001', 'hs300': 'sh000300',
              'sz50': 'sh000016', 'zxb': 'sz399005', 'cyb': 'sz399006', 
              'zx300': 'sz399008', 'zh500':'sh000905'}

STOCK_DICT = {'000001': 'sz000001', '600005': 'sh600005'}

STOCK_CHAIN = ChainMap(STOCK_ALIAS, STOCK_DICT)