#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Author:  Kincaid
# Modified by: CDtoday
# Date:  2017/6/28
# Version: 1.1
# ---------------------

import requests
import re

# Set the number of pictures \
# (or maybe you should try to crawl it down from somewhere in the site)
pic_n = 285

# Get a string-like list, which should be like:
# '[1, 2, ..., pic_n-1, pic_n]'
pic_nums = str(list(range(1, pic_n+1)))

# Api link
# Remember to double your curly-bracket in original url \
# to prevent misrecognized by format method
APILINK = ('http://g.txwy.tw/myapi/vote/result/'
           '?callback=getVoteInfoCB'
           '&q=[{{"groupid": 8,"items": {}}}]'
           '&key=snqx_ch'.format(pic_nums))

# Let crawler communicates with API
r = requests.get(APILINK)

# In python 3, you can prevent from using "u'" for unicode
# You don't need '\' for escaping while already using "r'"
p = re.compile(r'"voteid":([\d]+),"count":"([\d]+)"')
result = re.findall(p, r.text)

# Get ranking by the second element in each tuple (as integer)
# To be noticed, ranking here doesn't give same rank \
# to those votes with same score
ranking = sorted(result, key=lambda x: int(x[1]), reverse=True)

# Now we can print it out! \
# (or maybe store them in some df with pandas library for later use)
for index, each in enumerate(rank):
    # 'Print' is a function in python 3, so should be surrounded by brackets, \
    # which works fine in python 2, too
    # Even though tab ('\t') works, \
    # you can also use format method for better alignment
    print('Rank:', index+1, '\t',
          'ID:', '\t',
          each.num, '\t',
          'vote:', '\t',
          each.rank)
