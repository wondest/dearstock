# -*- coding:utf-8 -*-
'''
读取配置文件

Created on Dec 23, 2018

@author:  Tender Xie
@group:  DearBao
@contact: 396934200@qq.com
@public weixin: 笛尔宝
'''

import yaml
from dearstock import __config__

def get_tdxdata_lday():
    config_dict = _load_yml(__config__)
    return config_dict['gather']['tdxdata']['lday']

def get_tdxdata_csv():
    config_dict = _load_yml(__config__)
    return config_dict['gather']['tdxdata']['csv']

def _load_yml(file = __config__):
    f = open(file, encoding='utf-8')
    res = yaml.load(f)
    f.close()
    return res

if __name__ == '__main__':
    print(get_tdxdata_csv())
    
    
    