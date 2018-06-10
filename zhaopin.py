import requests
import time
from lxml import etree


def parse():
       url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?in=210500&jl=530&sm=0&p={}'
       headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
       }
       for i in range(1, 10):
              data = requests.get(url.format(i), headers=headers)
              s = etree.HTML(data.text)
              file = s.xpath('//*[@id="newlist_list_content_table"]/table')
              for tr in file:
                     job = tr.xpath('./tr[1]/td[1]/div/a/text()')
                     rate = tr.xpath('./tr[1]/td[2]/span/text()')
                     com = tr.xpath('./tr[1]/td[3]/a[1]/text()')
                     salary = tr.xpath('./tr[1]/td[4]/text()')
                     add =tr.xpath('./tr[1]/td[5]/text()')
                     print("{}\t{}\t{}\t{}\t{}".format(job,rate,com,salary,add))
                     time.sleep(0.1)


if __name__ == '__main__':
       parse()

