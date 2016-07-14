#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return TennfyBlog

class TennfyBlog(BaseFeedBook):
    title                 = u'Tennfy的博客'
    description           = u'网站技术，VPS评测和推荐达人。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'Tennfy的博客', 'http://www.tennfy.com/feed', True),
           ]