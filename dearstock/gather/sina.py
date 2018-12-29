'''
从新浪爬取数据

Created on 2018年12月26日

@author: Tender
@group: DearBao
@contact: 396934200@qq.com
@public: weixin public "笛尔宝"
'''

from urllib.request import urlopen,Request
import pandas as pd
import dearstock.gather.consts as cnst
import dearstock.util.config as config
import re
import json
import time
import os
import csv
import logging

# logging.basicConfig函数对日志的输出格式及方式做相关配置
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

def get_cur_day_all(pause=1):
    """
        获取当天个股或者指数交易记录
        
    Parameters:
    -----------
      pause : Integer
                爬虫间歇间隙(秒)
    Return
    -------
      DataFrame
        code : 股票代码
        name : 股票名称
        changepercent : 涨跌幅、
        trade : 现价
        open : 开盘价
        high : 最高价
        low : 最低价
        settlement : 收盘价
        volume : 成交量
        turnoverratio : 换手率
        amount : 成交额
        per : 市盈率
        pb :  市净率
        mktcap : 总市值
        nmc : 流通市值 
        date : 交易日期
    """
    today = config.get_today_str()
    csv_path = config.get_local_snap()
    csv_file = os.path.join(csv_path, "sina" + '_' + today + '.csv')
    df = None
    
    if os.path.exists(csv_file):
        logging.debug("Get data from local-repo")
        df = pd.read_csv(csv_file, converters = {u'code':str})
    else:
        logging.debug("Get data from sina")
        logging.debug("Get data from sina: page - 1")
        df = _parse_cur_day_json('hs_a', 1)
        if df is not None:
            for i in range(2, cnst.GL_SINA_DAY_PRICE_PAGE_NUM):
                time.sleep(pause)
                logging.debug("Get data from sina: page - " + str(i))
                newdf = _parse_cur_day_json('hs_a', i)
                df = df.append(newdf, ignore_index=True)
        if not os.path.exists(csv_path):
            os.mkdir(csv_path)

        df['date'] = today
        
        df.to_csv(csv_file, quoting=csv.QUOTE_ALL, index=False)
    return df

def _parse_cur_day_json(type1=None, page_num=1):
    """
        获取当天个股或者指数交易记录
        
    Parameters:
    -----------
      type1 : String
                  爬虫页面类型
      page_num : Integer
                  爬取第几页
    Return (None if nothing)
    -------
      DataFrame
        code : 股票代码
        symbol : 股票编码
        name : 股票名称
        change : 涨跌幅
        trade : 现价
        open : 开盘价
        high : 最高价
        low : 最低价
        close : 收盘价
        volume : 成交量
        turnoverratio : 换手率
        amount : 成交额
        per : 市盈率
        pb :  市净率
        mktcap : 总市值
        nmc : 流通市值 
    """
    request = Request(cnst.GL_SINA_DAY_PRICE_URL%(cnst.GL_PROTOCOL['http'], cnst.GL_DOMAINS['vsf'],
                                              cnst.GL_PAGES['jv'], type1, page_num))
    text = urlopen(request, timeout=10).read()
    
    if text == 'null':
        return None
    ## symbol 加上双引号
    reg = re.compile(r'\,(.*?)\:')
    text = reg.sub(r',"\1":', text.decode('gbk'))
    text = text.replace('"{symbol', '{"symbol')
    text = text.replace('{symbol', '{"symbol"')
    text = text.replace('changepercent', 'change')
    text = text.replace('settlement', 'close')

    jstr = json.dumps(text)
    js = json.loads(jstr)
    df = pd.DataFrame(pd.read_json(js, dtype={'code':object}),
                      columns=['code', 'symbol', 'name', 'change',
                       'trade', 'open', 'high', 'low', 'close', 'volume', 'turnoverratio',
                       'amount', 'per', 'pb', 'mktcap', 'nmc'])
    return df
