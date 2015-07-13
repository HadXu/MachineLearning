#coding:utf-8
'''
Created on 2015年5月22日

@author: Administrator
'''
#! /usr/bin/env python

import urllib
response = urllib.urlopen("http://d.weibo.com/?c=spr_web_sq_firefox_weibo_t001")

html = response.read()
print html