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
import sys

__version__ = codecs.open(os.path.join(os.path.dirname(__file__), 'VERSION.txt')).read()
__author__ = 'Tender'

if sys.platform == 'win32':
    __config__ = os.path.join(os.path.dirname(__file__), '../docs' ,'conf-win32.yml')
else:
    __config__ = os.path.join(os.path.dirname(__file__), '../docs' ,'conf.yml')

"""
gather api
"""
from dearstock.gather.api import *
from dearstock.store.dao import *
from dearstock.index.api import *