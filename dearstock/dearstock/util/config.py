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
import time
from dearstock import __config__

def get_tdx_sh_lday():
    config_dict = _load_config(__config__)
    return config_dict['gather']['tdx']['sh']['lday']

def get_tdx_sz_lday():
    config_dict = _load_config(__config__)
    return config_dict['gather']['tdx']['sz']['lday']

def get_tdx_data_csv():
    config_dict = _load_config(__config__)
    return config_dict['gather']['tdx']['data']['csv']

def get_sina_data_csv():
    config_dict = _load_config(__config__)
    return config_dict['gather']['sina']['data']['csv']

def _load_config(file = __config__):
    f = open(file, encoding='utf-8')
    res = yaml.load(f)
    f.close()
    return res

def get_today_str():
    return time.strftime('%Y%m%d',time.localtime(time.time()))

if __name__ == '__main__':
    print(get_today_str())
    
    
    