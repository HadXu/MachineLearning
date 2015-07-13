#coding:utf-8
'''
Created on 2015年5月18日

@author: xuzhenlei
'''

import urllib,re
def getHtml(url):
    return urllib.urlopen(url).read()

def getImg(html):
    reg=r':"(.*?\.jpg)",'
    reImg=re.compile(reg)
    
    imglist=re.findall(reImg, html)
    
    i=0
    for im in imglist:
        urllib.urlretrieve(im, "%s.jpg"%i);
        i+=1
    return imglist
html=getHtml("http://image.baidu.com/i?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1431504964782_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&itg=0&ie=utf-8&word=%E5%A4%B4%E5%83%8F#z=0&pn=&ic=0&st=-1&face=0&s=0&lm=-1")
print getImg(html)