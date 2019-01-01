# -*- coding:utf-8 -*-
'''

Created on Dec 30, 2018

@author:  Tender Xie
@group:  DearBao
@contact: 396934200@qq.com
@public weixin: 笛尔宝
'''
import dearstock

if __name__ == '__main__':
    #dearstock.store_his_day('000001')
    #dearstock.store_cur_day_all()
    
    #df = dearstock.get_store_his_day('000001')
    (symbol, df) = dearstock.get_his_day('000001')
    
    #df = dearstock.ma(df, 20)
    
    #df = dearstock.ema(df, 5)
    
    df = dearstock.kdj(df)

    print(df)
    
    