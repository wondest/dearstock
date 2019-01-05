# -*- coding:utf-8 -*-
'''

Created on Dec 30, 2018

@author:  Tender Xie
@group:  DearBao
@contact: 396934200@qq.com
@public weixin: 笛尔宝
'''
import dearstock
import pandas as pd

if __name__ == '__main__':
    (symbol, df) = dearstock.get_his_day('000001')
    
    df = dearstock.kdj(df)
    
    df = dearstock.kdtechf)
    
    pd.set_option('precision', 2)
    
    print(df[df['kdj_gold']])