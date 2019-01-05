'''

Created on 2018年12月29日

@author: Tender
@group: DearBao
@contact: 396934200@qq.com
@public: weixin public "笛尔宝"
'''

import dearstock

if __name__ == '__main__':
    dearstock.get_cur_day_all()
    dearstock.fetch_his_day_all()
    (symbol,df) = dearstock.get_his_day('000001')
    print(df)