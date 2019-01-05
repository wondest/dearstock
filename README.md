# DearStock: Use python to analysize stock

## 1. Something
### version
* git@github.com:wondest/dearstock.git
### database
* mysql
    root/xieqin#2018#ROOT
    dearAdmin/xieqin#2018#DBA
    dearApp/dear#2018#APP
    127.0.0.1 3306 dearstock
  
## 2. Feature Support
* gather : 从tdx采集lday数据功能
* gather : 从新浪爬取当天所有股票数据 
* store  : 将数据装入mysql中
* index : ma,kdj,macd数据加工
* gether : 完成所有文件fetch功能

## 3. TODO LIST
* gather : 实现股票数据的收集功能
* gather : 完善股票代码信息
* kdj选股因子
* macd选股因子
* ma选股因子
* 蜡烛图
* kdj_cross 验证
* kdj_oversold
* kdj_passivation

## 4. DONE LIST
### 2018/12/23
* 从通达信提取股票交易数据 

### 2018/12/25
* 完成Windows下 Eclipse+Anaconda+开发环境搭建
* 完成Github版本提交控制

### 2018/12/26
* 从新浪爬取当天所有股票数据

### 2018/12/27
* 优化了路径
* 重新安装Mysql环境

### 2018/12/29
* 数据装入mysql中

### 2019/01/01
* ma数据加工
* kdj数据加工
* macd数据加工
* kdj_cross

### 2019/01/03
* gether完成所有文件fetch功能
* mysql启动失败解决
