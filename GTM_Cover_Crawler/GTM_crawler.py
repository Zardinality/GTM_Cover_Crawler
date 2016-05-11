import requests as rq
import re
import os
from bs4 import BeautifulSoup
base_dir = os.path.join(os.getcwd(), "GTM")
if not os.path.exists(base_dir):
    os.mkdir(base_dir)
url2 = 'http://www.springer.com/new+%26+forthcoming+titles+%28default%29?SGWID=8-40356-404-653425-136&originalID=173621337&sortOrder=pubdateSortdesc&searchType=BYSERIES&searchScope=editions&resultStart='

num = 1
s = rq.session()
for i in range(33):
    url = url2 + str(num)
    prepare = rq.Request('GET', url=url).prepare()
    r = s.send(prepare)
    soup = BeautifulSoup(r.text, 'lxml')
    imgurls = soup.findAll('img', width='83')
    for imgurl in imgurls:
        url = imgurl['src']
        try:
            img = rq.get(url).conten
        except Exception as e:
            pass
        with open(base_dir + '\\' + str(num) + '.jpg', 'wb') as f:
            f.write(img)
            print('successfully retrieve ' + str(num) + 'pics')
        num += 1
        # print(url)
# print(r.text.encode('utf-8'))
