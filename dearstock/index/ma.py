# -*- coding:utf-8 -*-
'''
移动平均线

Created on Dec 30, 2018

@author:  Tender Xie
@group:  DearBao
@contact: 396934200@qq.com
@public weixin: 笛尔宝
'''

import pandas as pd

def ma(df, n=5):
    """
      算术平均值
      
      Parameter:
        df : DataFrame
          输入数据,包含date,close等价格数据
        window : Integer
          平均窗口
      Return:
        df : DataFame
          ma_{n} : 平均值
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError('Argument df is not DataFrame')
    
    if df is None:
        raise ValueError('Argument df is None')
    
    if n < 1:
        raise ValueError('Argument n must be a positive integer')
    
    #
    new_column = 'ma_' + str(n)
    df[new_column] = df['close'].rolling(window=n).mean()
    
    return df

def ema(df, n=3):
    """
      移动平均值
      
      ewa(n) = 2/(n+1) * p(n) + (n-1)/(n+1) * ewa(n-1)
      
      Parameter:
        df : DataFrame
          输入数据,包含date,close等价格数据
        window : Integer
          平均窗口
      Return:
        df : DataFame
          ma_{n} : 平均值
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError('Argument df is not DataFrame')
    
    if df is None:
        raise ValueError('Argument df is None')
    
    if n < 1:
        raise ValueError('Argument n must be a positive integer')
    
    #
    new_column = 'ema_' + str(n)
    df[new_column] = df['close'].ewm(adjust=False, span=n).mean()
    
    return df

def sma(df, n=3, m=1):
    """
      移动平均值
      算法：若Y=SMA(X,N,M) 则 Y=(M*X+(N-M)*Y')/N，其中Y'表示上一周期Y值，N必须大于M。
      
      ewa
      
      com : float, optional
        Specify decay in terms of center of mass, α=1/(1+com), for com≥0
      span : float, optional
        Specify decay in terms of span, α=2/(span+1), for span≥1
      
      http://pandas.pydata.org/pandas-docs/stable/computation.html#exponentially-weighted-windows
      
      When adjust=False is specified, moving averages are calculated as
        y(0)=x(0)
        y(t)=(1−α)y(t−1)+αx(t)
        
      α 就是权重 ema中权重是 2/(n+1)   sma中权重是m/n       dma中权重是 a
      
      Parameter:
        df : DataFrame
          输入数据,包含date,close等价格数据
        window : Integer
          平均窗口
      Return:
        df : DataFame
          ma_{n} : 平均值
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError('Argument df is not DataFrame')
    
    if df is None:
        raise ValueError('Argument df is None')
    
    if m < 1:
        raise ValueError('Argument m must be a positive integer')
    
    if n < m:
        raise ValueError('Argument n must bigger than m')
    #
    new_column = 'sma_' + str(n)
    df[new_column] = df['close'].ewm(adjust=False, alpha = m/n).mean()
    
    return df

def dma(df, n=3, a=1):
    """
      移动平均值
      算法：若Y=SMA(X,N,M) 则 Y=(M*X+(N-M)*Y')/N，其中Y'表示上一周期Y值，N必须大于M。
      
      ewa
      
      com : float, optional
        Specify decay in terms of center of mass, α=1/(1+com), for com≥0
      span : float, optional
        Specify decay in terms of span, α=2/(span+1), for span≥1
      
      http://pandas.pydata.org/pandas-docs/stable/computation.html#exponentially-weighted-windows
      
      When adjust=False is specified, moving averages are calculated as
        y(0)=x(0)
        y(t)=(1−α)y(t−1)+αx(t)
        
      α 就是权重 = ema中权重是 2/(n+1)   sma中权重是m/n   dma中权重是 a
      
      Parameter:
        df : DataFrame
          输入数据,包含date,close等价格数据
        window : Integer
          平均窗口
        a : Float 
          权重
      Return:
        df : DataFame
          ma_{n} : 平均值
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError('Argument df is not DataFrame')
    
    if df is None:
        raise ValueError('Argument df is None')
    
    if a < 0 or a > 1:
        raise ValueError('Argument a must between 0 and 1')
    #
    new_column = 'sma_' + str(n)
    df[new_column] = df['close'].ewm(adjust=False, alpha=a).mean()
    
    return df