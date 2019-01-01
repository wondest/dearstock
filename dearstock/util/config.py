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

def get_remote_tdx_lday():
    config_dict = _load_config(__config__)
    return config_dict['remote']['tdx']['lday']

def get_local_snap():
    config_dict = _load_config(__config__)
    return config_dict['local']['snap']

def get_local_hist():
    config_dict = _load_config(__config__)
    return config_dict['local']['hist']

def get_store_mysql_user():
    config_dict = _load_config(__config__)
    return config_dict['store']['mysql']['user']

def get_store_mysql_password():
    config_dict = _load_config(__config__)
    return config_dict['store']['mysql']['password']

def get_store_mysql_dbname():
    config_dict = _load_config(__config__)
    return config_dict['store']['mysql']['dbname']

def get_store_mysql_host():
    config_dict = _load_config(__config__)
    return config_dict['store']['mysql']['host']

def get_store_mysql_port():
    config_dict = _load_config(__config__)
    return config_dict['store']['mysql']['port']

def get_store_mysql_dbinfo():
    config_dict = _load_config(__config__)
    return (config_dict['store']['mysql']['dbname']
            ,config_dict['store']['mysql']['user']
            ,config_dict['store']['mysql']['password']
            ,config_dict['store']['mysql']['host']
            ,config_dict['store']['mysql']['port'])

def _load_config(file = __config__):
    f = open(file, encoding='utf-8')
    res = yaml.load(f)
    f.close()
    return res

def get_today_str():
    return time.strftime('%Y%m%d',time.localtime(time.time()))

if __name__ == '__main__':
    print(get_store_mysql_dbinfo())