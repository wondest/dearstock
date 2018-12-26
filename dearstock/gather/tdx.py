# -*- coding:utf-8 -*-
'''
股票交易数据
Created on Dec 22, 2018

@author:  Tender Xie
@group:  DearBao
@contact: 396934200@qq.com
@public weixin: 笛尔宝
'''
import os
import struct
import pandas as pd
import csv

from dearstock.gather import consts as cnst
from dearstock.util import config

import logging

# logging.basicConfig函数对日志的输出格式及方式做相关配置
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

def get_tdx_his_day(code, start=None, end=None):
    """
        获取个股或者指数历史交易记录（天）
        
    Parameters:
    -----------
      code : String
              股票代码 或者 别名
      start : string
              起始日期
      end : string
              终止日期

    Return
    -------
      DataFrame
          date: YYYY-MM-DD  -- index
          name: 指数名称
          change: 涨跌幅
          open: 开盘价
          preclose: 昨日收盘价
          close: 收盘价
          high: 最高价
          low: 最低价
          volume: 成交量(手)
          amount: 成交金额（亿元）
          code: 股票代码
          symbol: 股票编码
    """
    
    symbol = _find_tdx_label(code)
    if symbol is None:
        raise KeyError("symbol = [%s] 非法股票代码" % code)

    today = config.get_today_str()
    csv_path = config.get_tdx_data_csv()
    csv_file = os.path.join(csv_path, symbol + '_' + today + '.csv')
    df = None
    
    if os.path.exists(csv_file):
        logging.debug("Get data from csv")
        date_parser = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
        df = pd.read_csv(csv_file, parse_dates=['date'], index_col='date', date_parser=date_parser, converters = {u'code':str})
    else:
        logging.debug("Get data from lday")
        
        day_file = os.path.join(config.get_tdx_sh_lday(), symbol + '.day')
        
        if(not os.path.exists(day_file)):
            day_file = os.path.join(config.get_tdx_sz_lday(), symbol + '.day')
        
        df = _parse_tdx_lday(day_file)
        df['code'] = str(symbol[2:])
        df['symbol'] = symbol

        if not os.path.exists(csv_path):
            os.mkdir(csv_path)
        
        df.to_csv(csv_file, quoting=csv.QUOTE_ALL)

    if start is not None:
        df = df[df.date >= start]
    
    if end is not None:
        df = df[df.date <= end]

    return df
    
def _find_tdx_label(code):
    """
        根据股票代码或者别名搜索到对应的通达信文件名
    
    Parameters
    ------------
        code : String
                   股票代码或者别名
    
    Return
    -------
        symbol : String
                    股票编码，如果没找到则返回None
    """
    return cnst.STOCK_CHAIN.setdefault(code, None)

def _parse_tdx_lday(day_file, field_bytes=32):
    """
        解析通达信文件
        
        每32个字节为一天数据
        每4个字节为一个字段，每个字段内低字节在前
        00 ~ 03 字节：年月日, 整型
        04 ~ 07 字节：开盘价*100， 整型
        08 ~ 11 字节：最高价*100, 整型
        12 ~ 15 字节：最低价*100, 整型
        16 ~ 19 字节：收盘价*100, 整型
        20 ~ 23 字节：成交额（元），float型
        24 ~ 27 字节：成交量（股），整型
        28 ~ 31 字节：（保留）
    
    Parameters
    -----------
      day_file : String
               通达信文件名
      filed_bytes : Integer
              一行数据占用字节

    Return
    -------
      DataFrame
          date:YYYY-MM-DD  -- index
          name:指数名称
          change:涨跌幅
          open:开盘价
          preclose:昨日收盘价
          close:收盘价
          high:最高价
          low:最低价
          volume:成交量(手)
          amount:成交金额（亿元）
    """
    
    data_list = []
    data_columns = ['date', 'change', 'open', 'preclose', 'high', 'low', 'volume', 'amount']
    
    with open(day_file, 'rb') as f:
        buffer = f.read()
        num_line = int(len(buffer)/field_bytes)
        
        for i in range(num_line):
            
            byte_index_b = i * field_bytes;
            
            field_data = struct.unpack('IIIIIfII', buffer[byte_index_b:(byte_index_b+field_bytes)])
            
            date = _str_yyyymmdd(field_data[0])
            open_1 = field_data[1]/100.0
            high = field_data[2]/100.0
            low =  field_data[3]/100.0
            close = field_data[4]/100.0
            amount = field_data[5]/10.0
            volume = field_data[6]
            
            if i==0:
                preclose = close
            change = round((close - preclose)/preclose*100, 2)

            preclose = close

            data_list.append([date, change, open_1, preclose, high, low, volume, amount])
    
    df = pd.DataFrame(data_list, columns=data_columns)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index("date", inplace=True)
    return df

def _str_yyyymmdd(i_yyyymmdd):
    """
        将整数的年月日转换成字符串
    
    Parameters
    -------
      i_yyyymmdd : Integer

    Return
    -------
      s_yyyymmdd : String
          yyyy-mm-dd
    """
    year = int(i_yyyymmdd/10000);
    m = int((i_yyyymmdd%10000)/100);
    month = str(m);
    if m <10 :
        month = "0" + month;
    
    d = (i_yyyymmdd%10000)%100;
    day=str(d);
    if d< 10 :
        day = "0" + str(d);
    
    return str(year) + "-" + month + "-" + day

if __name__ == '__main__':
    print("Trading test")
    print(get_tdx_his_day('sh'))