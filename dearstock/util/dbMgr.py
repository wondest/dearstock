'''

Created on 2018年12月28日

@author: Tender
@group: DearBao
@contact: 396934200@qq.com
@public: weixin public "笛尔宝"
'''

from sqlalchemy import create_engine
import mysql.connector as mysql

class dbEngine():
    def __init__(self, dbname=None, user=None, password=None, host='localhost', port='3306', dbtype='mysql+pymysql'):
        # "mysql://scott:tiger@hostname:port/dbname"
        self.dburl = "%s://%s:%s@%s:%s/%s" %(dbtype, user, password, host, port, dbname)
        
    def __enter__(self):
        self.engine = create_engine(self.dburl)
        return self.engine
    
    def __exit__(self, exc_type, exc_instalce, traceback):
        pass
    
class dbConn():
    def __init__(self, dbname=None, user=None, password=None, host='localhost', port='3306', dbtype='mysql+pymysql'):
        # "mysql://scott:tiger@hostname:port/dbname"
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
        
    def __enter__(self):
        self.conn = mysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  passwd=self.password,
                                  database=self.dbname)
        return self.conn
    
    def __exit__(self, exc_type, exc_instalce, traceback):
        self.conn.close()