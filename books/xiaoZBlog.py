#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return xiaoZBlog

class xiaoZBlog(BaseFeedBook):
    title                 = u'小Z的博客'
    description           = u'各类网站技术信息，享你所想。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'小Z的博客', 'http://www.xiaoz.me/feed', True),
           ]