# import requests
# from bs4 import BeautifulSoup
# import re
# import string
#
# def year(endurl, ent3, ent1):
#     endresu = []
#     res = requests.get(endurl)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     for ant0 in soup.select('#divSeries'):
#         endresu1 = []
#         for ant1 in ant0.select('.interval01'):
#             endresu2 = []
#             for ant2 in ant1.select('.interval01-list'):
#                 endresu3=[]
#                 for ant3 in ant2.select('li'):
#                     resu2 = {}
#                     resu2['车系'] = ent3.select('h4 a')[0].text
#                     resu2['品牌'] = ent1.select('dt div a')[0].text
#                     resu2['年款'] = ant3.select('.interval01-list-cars p a')[0].text
#                     if ant2.select('.interval01-list-guidance div'):
#                         resu2['价格'] = ant3.select('.interval01-list-guidance div')[0].text
#                     else:
#                         resu2['价格'] = '暂无报价'
#                     print(resu2)
#                     endresu3.append(resu2)
#                 endresu2.extend(endresu3)
#             endresu1.extend(endresu2)
#         endresu.extend(endresu1)
#     return endresu
#
#
# def fn(carurl):
#     endresult1 = []
#     res = requests.get(carurl)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     for ent1 in soup.select('dl'):
#         endresult3 = []
#         for ent2 in ent1.select('.rank-list-ul'):
#             endresult4 = []
#             for ent3 in ent2.select('li'):
#                 if ent3.select('h4'):
#                     m = re.search('<a href="//car.autohome.com.cn/price(.*)">报价', str(ent3))
#                     if m:
#                         ypnum = m.group(1)
#                         endresult4.extend(year("https://car.autohome.com.cn/price" + ypnum, ent3, ent1))
#             endresult3.extend(endresult4)
#         endresult1.extend(endresult3)
#     return endresult1
#
#
# url = 'https://www.autohome.com.cn/grade/carhtml/{}.html'
#
#
#
#
#
#
#
#
#
# def fn2(url):
#     endresult1 = []
#     for i in range(97, 123):
#         endresult2 = []
#         newurl = url.format(chr(i).upper())
#         endresult2 = fn(newurl)
#         endresult1.extend(endresult2)
#     return endresult1
#
#
# endresult = []
# endresult = fn2(url)

# print(endresult)

# import pandas
# df = pandas.DataFrame(endresult)
# print(df)
# df.to_excel('car9.xlsx')

import requests
from bs4 import BeautifulSoup
import re
import string
import pandas

def year(endurl, ent3, ent1):
    endresu = []
    res = requests.get(endurl)
    soup = BeautifulSoup(res.text, 'html.parser')
    for ant0 in soup.select('#divSeries'):
        for ant1 in ant0.select('.interval01'):
            for ant2 in ant1.select('.interval01-list'):
                for ant3 in ant2.select('li'):
                    resu2 = {}
                    resu2['车系'] = ent3.select('h4 a')[0].text
                    resu2['品牌'] = ent1.select('dt div a')[0].text
                    resu2['年款'] = ant3.select('.interval01-list-cars p a')[0].text
                    if ant2.select('.interval01-list-guidance div'):
                        resu2['价格'] = ant3.select('.interval01-list-guidance div')[0].text
                    else:
                        resu2['价格'] = '暂无报价'
                    print(resu2)
                    endresu.append(resu2)
    return endresu


def fn(carurl):
    endresult1 = []
    res = requests.get(carurl)
    soup = BeautifulSoup(res.text, 'html.parser')
    for ent1 in soup.select('dl'):
        for ent2 in ent1.select('.rank-list-ul'):
            for ent3 in ent2.select('li'):
                if ent3.select('h4'):
                    m = re.search('<a href="//car.autohome.com.cn/price(.*)">报价', str(ent3))
                    if m:
                        ypnum = m.group(1)
                        endresult1.extend(year("https://car.autohome.com.cn/price" + ypnum, ent3, ent1))
    return endresult1



# import multiprocessing
# from multiprocessing import Pool
# class MyProcess(multiprocessing.Process):
#     endres=[]
#     def __init__(self,num):
#         multiprocessing.Process.__init__(self)
#         self.num=num
#
#     def run(self):
#         url='https://www.autohome.com.cn/grade/carhtml/{}.html'
#         newurl=url.format(self.num)
#         self.endres = fn(newurl)
#
#     def get_res(self):
#         return self.endres




# import threading
#
# class MyThread(threading.Thread):
#     def __init__(self, num):
#         # multiprocessing.Process.__init__(self)
#         super(MyThread, self).__init__()
#         self.num = num
#
#     def run(self):
#         url = 'https://www.autohome.com.cn/grade/carhtml/{}.html'
#         newurl = url.format(self.num)
#         self.endresult2 = fn(newurl)
#
#     def get_result(self):
#         return self.endresult2
url = 'https://www.autohome.com.cn/grade/carhtml/{}.html'
from multiprocessing import Pool


if __name__ == '__main__':
    endresult = []
    res=[]

    # 多线程(快)（适用于网络密集型请求）
    # for i in range(97, 123):
    #     p = MyThread(chr(i).upper())
    #     # res.append(p)
    #     p.start()

    # 多进程(还可以)(cpu密集型，io密集型，网络密集型都适用，但相对占用CPU资源)
    # for i in range(97,123):
    #     p=MyProcess(chr(i).upper())
    #     p.start()

    # 进程池(慢)
    p=Pool(4)
    for i in range(97,123):
        newurl=url.format(chr(i).upper())
        res=p.apply(fn, args=(newurl,))
        endresult.extend(res)
    # p.close()
    # p.join()
    print(endresult.__len__())



    # for x in res:
    #     x.join()
    #     endresult.extend(x.get_result())
    # df = pandas.DataFrame(endresult)
    # print(df)
    # df.to_excel('car18.xlsx')


# IO密集型代码(文件处理、网络爬虫等)，
# 多线程能够有效提升效率(单线程下有IO操作会进行IO等待，造成不必要的时间浪费，
# 而开启多线程能在线程A等待时，自动切换到线程B，可以不浪费CPU的资源，从而能提升程序执行效率)。
# 所以python的多线程对IO密集型代码比较友好。