# -*- coding:utf-8 -*-
'''
kdj

Created on Dec 30, 2018

@author:  Tender Xie
@group:  DearBao
@contact: 396934200@qq.com
@public weixin: 笛尔宝
'''

import pandas as pd

def rsv(df, n=9):
    """
    Description:
      n日 RSV=（Cn－Ln）/（Hn－Ln）×100 Cn为第n日收盘价；Ln为n日内的最低价；Hn为n日内的最高价。
    Parameter:
      df : DataFrame : 交易数据 close,low,high
      n : Integer : 窗口大小
    Return:
      DataFrame :交易数据,rsv
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError('Argument df is not DataFrame')

    if df is None:
        raise ValueError('Argument df is None')

    df['kdj_high'] = df['high'].rolling(window=n).max()
    df['kdj_low'] = df['low'].rolling(window=n).min()

    df['kdj_rsv'] = 100 * (df['close'] - df['kdj_low'])/(df['kdj_high'] - df['kdj_low'])

    return df.drop(columns=['kdj_high','kdj_low'])

def kdj(df, n=9, m1=3, m2=3):
    """
    Description:
      当日K值=2/3×前一日K值+1/3×当日RSV
      当日D值=2/3×前一日D值+1/3×当日K值
      若无前一日K 值与D值，则可分别用50来代替。
      当日J值=3*当日K值-2*当日D值
    Parameter:
      df : DataFrame : 交易数据,close,low,high
      n : Integer : rsv窗口大小
      m1 : Integer : k 窗口大小
      m2 : Integer : j 窗口大小
    Return:
      DataFrame : 交易数据,k,d,j
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError('Argument df is not DataFrame')

    if df is None:
        raise ValueError('Argument df is None')

    # Calc rsv
    df = rsv(df, n)

    # Calc K
    df['kdj_k'] = df['kdj_rsv'].ewm(adjust=False, com=(m1-1)).mean()

    # Calc D
    df['kdj_d'] = df['kdj_k'].ewm(adjust=False, com=(m2-1)).mean()

    # Calc J
    df['kdj_j'] = 3*df['kdj_k'] - 2*df['kdj_d']

    return df.drop(columns=['kdj_rsv'])