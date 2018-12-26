# -*- coding:utf-8 -*-
'''

Created on Dec 23, 2018

@author:  Tender Xie
@group:  DearBao
@contact: 396934200@qq.com
@public weixin: 笛尔宝
'''

import codecs
import os

__version__ = codecs.open(os.path.join(os.path.dirname(__file__), 'VERSION.txt')).read()
__author__ = 'Tender Xie'
__config__ = os.path.join(os.path.dirname(__file__), '../docs' ,'conf.yml')


"""
for trading data
"""
from dearstock.gather.tdx import (get_tdx_his_day)