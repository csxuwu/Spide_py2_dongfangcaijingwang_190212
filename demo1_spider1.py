#-*- coding:utf-8 -*-
import urllib
import urllib2
import os
import random
import datetime
from bs4 import BeautifulSoup
import chardet
import re


'''
    -1 反爬虫措施：
        1) 随机选user-agent
        2) 随机选代理IP  https://www.xicidaili.com/
    -2 爬数据
        1) 设置url
        2) 存储数据，先将网页数据存储到本地，不要每次调试都到网站爬取
    -3 筛选数据
        1) re
        2) beautifulsoup
    -4 存储数据
        将筛选好的数据存储     
'''
class Spider1():

    def __init__(self,url_1,url_2,url_3,file_path,start_date,end_date):
        self.url_1 = url_1
        self.url_2 = url_2
        self.url_3 = url_3
        self.file_path = file_path
        self.start_date = start_date
        self.end_date = end_date
        # self.create_url(self.start_date,self.end_date,1)

    '''-1 反爬虫措施'''
    '''随机选user-agent'''
    def user_agent(self):
        ua_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",                                                 # firefox
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",             # firefox
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",             # charm
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",            # 360
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",     # 猎豹浏览器
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",                              # QQ浏览器
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",   # 搜狗浏览器
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2"                # Safari
        ]
        return random.choice(ua_list)

    '''随机选代理IP'''
    def proxys(self):
        ip_list = [
            "117.21.191.154",
            "110.52.235.214",
            "218.85.22.69",
            "101.132.122.230",
            "222.217.30.151	"
        ]
        proxy = {"http":random.choice(ip_list)}
        return proxy

    '''-2 爬网页数据'''
    '''构建url'''
    def create_url(self,start_date,end_date,page):
        '''
        构建目标url     没问题
        :param start_date:
        :param end_date:
        :return:
        '''
        # url_1 = "http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/pagesize=50,"
        # url_2 = ",sortRule=-1,sortType=,"
        # url_3 = ",gpfw=0,js=var%20data_tab_2.html?"
        # http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/pagesize=50,page=1,sortRule=-1,sortType=,startDate=2018-12-27,endDate=2019-01-27,gpfw=0,js=var%20data_tab_2.html?rt=25809955
        page = urllib.urlencode({"page":page})
        startDate = urllib.urlencode({"startDate":start_date})
        endDate = urllib.urlencode({"endDate":end_date})
        url = self.url_1 + page + self.url_2 + startDate + "," + endDate +  self.url_3
        return url

    '''获取html'''
    def load_html(self,url):
        '''
        仅获取网页数据
        :param url:
        :return:
        '''
        # 构建request
        user_agent = self.user_agent()
        header = {"Uers-Agent":user_agent}
        request = urllib2.Request(url,headers=header)

        # 构建opener
        proxy = self.proxys()
        httpproxy_handler = urllib2.ProxyHandler(proxy)
        opener = urllib2.build_opener(httpproxy_handler)

        # 发送请求，接受响应
        html = opener.open(request)
        # html = urllib2.urlopen(request)
        return html.read()


    '''存储html'''
    def write_html(self,html,filename,page):
        '''

        :param html:
        :param filename:
        :param page:
        :return:
        '''
        print(" "*10 + "将 第{}页 内容写入 {}".format(page,filename))
        file = open(filename.decode('gbk').encode('utf-8'),'w')
        # print(chardet.detect(file.read()))
        file.write(html)
        if page % 5 == 0:
            print(" " * 10 + '-' * 77)


    '''-3 筛选数据'''
    def filter_html(self,html):
        pass

    '''-4 存储筛选好的数据'''
    def write_filter_html(self,file_path,page):
        pass

def all():
    '''初始化基本信息：url，搜索区间'''
    file_path = "tradedetail/"
    initial_date = datetime.date.today()  # 最初的起始时间为当前时间，精确到“天”
    start_date = initial_date
    end_date = start_date - datetime.timedelta(days=7)  # 搜索区间为7天
    url_start = "http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/pagesize=50,page=1,sortRule=-1,sortType=,startDate=" + str(
        start_date) + ",endDate=" + str(end_date) + ",gpfw=0,js=var%20data_tab_2.html?"
    url_1 = "http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/pagesize=50,"
    url_2 = ",gpfw=0,js=var%20data_tab_2.html?"

    '''开始爬取'''
    spider = Spider1(url_1, url_2, file_path, start_date, end_date)
    batch_max = 160  # 160个搜索区间，每个区间为7天
    batch = 0
    while batch < batch_max:
        spider.end_date = spider.start_date - datetime.timedelta(days=7)  # 搜索区间为7天

        '''-1 获取搜索区间内总的页数'''
        '''下载第一张页面'''
        html_start = spider.load_html(url_start)
        '''筛选第一张页面数据，包括最大页码'''
        filter_html1, max_page1 = spider.filter_html(html_start)
        '''-2 循环爬取当前区间的所有内容'''
        for page in max_page1:
            url = spider.create_url(spider.url_1, spider.url_2, spider.start_date, spider.end_date)
            html = spider.load_html(url)
            spider.write_html(html, spider.file_path, page)

            filter_html2, max_page2 = spider.filter_html(html)
            spider.write_filter_html(spider.file_path, page)
        batch += 1

def load_html():
    '''
    仅仅获取html内容，不进行数据筛选 OK
    :return:
    '''
    '''初始化基本信息：url，搜索区间'''
    file_path = "tradedetail/"
    # initial_date = datetime.date.today()  # 最初的起始时间为当前时间，精确到“天”
    date = '2018-07-10'
    initial_date = datetime.datetime.strptime(date,'%Y-%m-%d').date()
    end_date = initial_date

    start_date = end_date  # 搜索区间为7天
    # http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/pagesize=50,page=1,sortRule=-1,sortType=,startDate=2018-12-27,endDate=2019-01-27,gpfw=0,js=var%20data_tab_2.html?rt=25809955
    url_1 = "http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/pagesize=50,"
    url_2 = ",sortRule=-1,sortType=,"
    url_3 = ",gpfw=0,js=var%20data_tab_2.html?"
    pattern = re.compile(r'.("data":[[]]).')

    '''开始爬取'''
    spider = Spider1(url_1, url_2, url_3, file_path, start_date, end_date)

    batch_max = 160  # 160个搜索区间，每个区间为7天
    batch = -1
    while batch < batch_max:
        batch += 1
        spider.start_date = spider.end_date - datetime.timedelta(days=7)  # 搜索区间为7天
        page = 0
        file_path1 = spider.file_path + "[" + str(spider.start_date) + "]" + "~" + "[" +str(spider.end_date) + "]"     # 存储某搜索区间结果的文件夹名
        if not os.path.exists(file_path1):
            os.makedirs(file_path1)
        index = batch + 1
        print("="*20 + " " + str(index) + " 爬取 " + "[" + str(spider.start_date) + "]" + "~" + "[" +str(spider.end_date) + "] 龙虎榜上榜股票成交明细 " + "="*20)
        while True:
            page += 1
            print(" "*10 +  "爬取 第{}页 ...".format(page))
            file_path = file_path1  + "/" + str(page) + ".txt"
            url = spider.create_url(spider.start_date, spider.end_date, page)
            # print(url)
            html = spider.load_html(url)
            html = html.decode('gbk').encode('utf-8')  # 网页源格式为gbk,将其转为utf-8,存入文件时中文不会乱码
            '''匹配爬取的"data":[]，是否存在，如果存在，则表明当前区间的内容已经爬取完，跳出循环，开始下一个区间的爬取'''
            match = pattern.search(html, 0, 60)
            if match :
                print("第{}页 无内容".format(page))
                break
            spider.write_html(html, file_path, page)
        spider.end_date = spider.start_date     # 更新起终止时间
        print("\n")

if __name__ == "__main__":
    load_html()


















