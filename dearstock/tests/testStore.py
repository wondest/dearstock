'''

Created on 2018年12月29日

@author: Tender
@group: DearBao
@contact: 396934200@qq.com
@public: weixin public "笛尔宝"
'''
import dearstock

if __name__ == '__main__':
    #dearstock.store_his_day('000001')
    #dearstock.store_cur_day_all()
    
    df = dearstock.get_store_his_day('000001')
    print(df)