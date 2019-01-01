'''

Created on 2018年12月28日

@author: Tender
@group: DearBao
@contact: 396934200@qq.com
@public: weixin public "笛尔宝"
'''
import dearstock.util.dbMgr as db
import dearstock.util.config as config
from dearstock.gather.api import *
import logging
import pandas as pd

# logging.basicConfig函数对日志的输出格式及方式做相关配置
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

def store_his_day(code):
    """
      Parameter:
          code : string
            股票代码
      Return:
          get_his_day.DataFrame      
    """
    logging.debug("Store his day data")

    # 获取日交易历史数据
    (symbol, df) = get_his_day(code)

    # database information
    db_info = config.get_store_mysql_dbinfo()

    # Delete data
    with db.dbConn(*db_info) as conn:
        cursor = conn.cursor()
        cursor.execute("delete from stock_trading_day_h where symbol='%s'" % symbol)
        conn.commit()

    # Append data
    with db.dbEngine(*db_info) as engine:
        df.to_sql('stock_trading_day_h', engine, if_exists='append')
        
    return df

def get_store_his_day(code):
    """
      Parameter:
          code : string
            股票代码
      Return:
          get_his_day.DataFrame      
    """
    logging.debug("Get store his day data")
    
    symbol = find_stock_symbol(code)
    if symbol is None:
        raise KeyError("symbol = [%s] 非法股票代码" % code)

    # database information
    db_info = config.get_store_mysql_dbinfo()

    # Select data
    with db.dbEngine(*db_info) as engine:
        df = pd.read_sql("SELECT date, open, preclose, close, high, low, code, symbol FROM dearstock.stock_trading_day_h WHERE symbol = '%s'"%symbol,
                    con=engine, index_col=['date'])
        
    return df

def store_cur_day_all():
    """
      Return:
          get_cur_day_all.DataFrame  
    """
    logging.debug("Store cur day data")
        
    # 获取日交易快照数据
    df = get_cur_day_all()
    
    # database information
    db_info = config.get_store_mysql_dbinfo()

    # Delete data
    with db.dbConn(*db_info) as conn:
        cursor = conn.cursor()
        cursor.execute("truncate table stock_trading_day_c")
        
    # Append data
    with db.dbEngine(*db_info) as engine:
        df.to_sql('stock_trading_day_c', engine, index=False, if_exists='append')
        
    return df