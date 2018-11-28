# coding=utf-8
import os
import re
import sys
# import urllib2
import urllib
import time
 
import requests
"""根据搜索词下载百度图片"""
 
 
 
def getPage(keyword,page,n):
    page=page*n
    keyword=urllib.request.quote(keyword, safe='/')
    url_begin= "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="
    url = url_begin+ keyword + "&pn=" +str(page) + "&gsm="+str(hex(page))+"&ct=&ic=0&lm=-1&width=0&height=0"
    return url
 
def get_onepage_urls(onepageurl):
    try:
        html = requests.get(onepageurl).text
    except Exception as e:
        print(e)
        pic_urls = []
        return pic_urls
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    return pic_urls
 
 
def down_pic(pic_urls, keyword):
    """给出图片链接列表, 下载所有图片"""
    filepath = judge_filepath(keyword)
    for i, pic_url in enumerate(pic_urls):
        try:
            pic = requests.get(pic_url, timeout=15)
            name =str(i + 1) + '.jpg'
            filename = os.path.join(filepath, name)
            with open(filename, 'wb') as f:
                f.write(pic.content)
                print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
        except Exception as e:
            print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
            print(e)
            continue
        time.sleep(1)
 
def judge_filepath(keyword):
    basepath = "/home/fantasy/MachineLearning/project/spiders/downloads"
    filepath = os.path.join(basepath, keyword)
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    return filepath
 
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("python scrapy.py 猫/狗 1")
        sys.exit(1)
    keyword = sys.argv[1]
    page_size = int(sys.argv[2])
    # keyword = '狗'  # 关键词, 改为你想输入的词即可, 相当于在百度图片里搜索一样
    page_begin=0
    page_number=20
    all_pic_urls = []
    while page_begin < page_size:
        print("第[%d]次请求数据" % page_begin)
        url=getPage(keyword,page_begin,page_number)
        onepage_urls= get_onepage_urls(url)
        page_begin += 1
 
        all_pic_urls.extend(onepage_urls)
        # time.sleep(1)
 
    down_pic(list(set(all_pic_urls)), keyword)
