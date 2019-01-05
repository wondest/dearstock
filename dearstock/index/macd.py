# -*- coding:utf-8 -*-
'''
macd

Created on Jan 1, 2019

@author:  Tender Xie
@group:  DearBao
@contact: 396934200@qq.com
@public weixin: 笛尔宝
'''

import pandas as pd

def macd(df, n=9, m1=12, m2=26):
    """
    Description:
        1、dea=ema(dif,n)
        2、macd=dif - dea
    Parameter:
      df : DataFrame : 交易数据,close
      n  : Integer : dea
      m1 : Integer : ema1 窗口大小
      m2 : Integer : ema2 窗口大小
    Return:
      DataFrame : 交易数据,macd_dif,macd_dea,macd_bar
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError('Argument df is not DataFrame')

    if df is None:
        raise ValueError('Argument df is None')

    # Calc dif
    df = _dif(df, m1, m2)
    
    # Calc dea
    df['macd_dea'] = df['macd_dif'].ewm(adjust=False, span=n).mean()
    
    # Calc macd_bar
    df['macd_bar'] = 2*(df['macd_dif'] - df['macd_dea'])
    
    return df

def _dif(df, m1, m2):
    """
    Description:
        1、计算移动平均值（快)（EMA）
        2、计算移动平均值（慢)（EMA）
        3、计算离差值（DIF）
            DIF=今日EMA（快）－今日EMA（慢）
    Parameter:
      df : DataFrame : 交易数据,close
      m1 : Integer : ema1 窗口大小
      m2 : Integer : ema2 窗口大小
    Return:
      DataFrame : 交易数据,macd_dif
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError('Argument df is not DataFrame')

    if df is None:
        raise ValueError('Argument df is None')
    
    if m1 > m2:
        slow = m1
        fast = m2
    else:
        slow = m2
        fast = m1

    # Calc fast
    df['macd_fast'] = df['close'].ewm(adjust=False, span=fast).mean()

    # Calc slow
    df['macd_slow'] = df['close'].ewm(adjust=False, span=slow).mean()

    # Calc dif
    df['macd_dif'] = (df['macd_fast'] - df['macd_slow'])

    return df.drop(columns=['macd_fast', 'macd_slow'])
