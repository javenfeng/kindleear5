#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return GuboBlog

class GuboBlog(BaseFeedBook):
    title                 = u'古博的博客'
    description           = u'分享互联网知识，建站、IT话题杂谈。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'古博的博客', 'http://ftr.fivefilters.org/makefulltextfeed.php?url=http%3A%2F%2Fgubo.org%2Ffeed%2F&max=10', True),
           ]