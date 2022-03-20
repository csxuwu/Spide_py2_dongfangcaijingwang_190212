#-*- coding:utf-8 -*-
import datetime
import demo1_spider1
import chardet
import re

'''
    测试各个方法
'''
'''初始化基本信息：url，搜索区间'''
file_path = "tradedetail/"
initial_date = datetime.date.today()  # 最初的起始时间为当前时间，精确到“天”
end_date = initial_date
start_date = end_date   # 搜索区间为7天
    # http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/pagesize=50,page=1,sortRule=-1,sortType=,startDate=2018-12-27,endDate=2019-01-27,gpfw=0,js=var%20data_tab_2.html?rt=25809955
url_1 = "http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/pagesize=50,"
url_2 = ",sortRule=-1,sortType=,"
url_3 = ",gpfw=0,js=var%20data_tab_2.html?"
spider = demo1_spider1.Spider1(url_1, url_2, url_3, file_path, start_date, end_date)

'''开始爬取'''
spider = demo1_spider1.Spider1(url_1, url_2,url_3, file_path, start_date, end_date)
# url_start = spider.create_url(start_date,end_date,1)

batch_max = 2 # 160个搜索区间，每个区间为7天
batch = 0



while batch < batch_max:
    spider.start_date = spider.end_date - datetime.timedelta(days=7)  # 搜索区间为7天
    max_page1 = 10
    page = 0
    while page < max_page1
        file_path = spider.file_path  + str(page + 1) +".txt"
        url = spider.create_url(spider.start_date, spider.end_date,page + 1)
        print(url)
        html = spider.load_html(url)
        print (chardet.detect(html))
        html = html.decode('gbk').encode('utf-8')   # 网页源格式为gbk,将其转为utf-8,存入文件时中文不会乱码
        # print (chardet.detect(html))
        if
        spider.write_html(html,file_path,page + 1)
        page += 100
    batch += 1