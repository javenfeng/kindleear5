#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return JavenBlog

class JavenBlog(BaseFeedBook):
    title                 = u'Javen的小站'
    description           = u'爱国主义：一堆随时可以被任何野心家所点燃，去照亮他的名字的易燃垃圾。 ——安卜罗斯·皮尔斯'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = True
    feeds = [
            (u'Javen的小站', 'http://ftr.fivefilters.org/makefulltextfeed.php?url=https%3A%2F%2Fchinmax.info%2Ffeed%2F&max=10', True),
           ]