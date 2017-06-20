#!/usr/bin/python2

### Author:  Kincaid
### Date  :  2017/6/20
### Version: 1.0

import requests
import re

requests.packages.urllib3.disable_warnings()

picNums="1"
for i in range (2,286):     #2 to 285
    picNums=picNums+','+str(i)      #"1,2,3,4,...,284,285"

APILINK='http://g.txwy.tw/myapi/vote/result/?callback=getVoteInfoCB&q=[{"groupid":8,"items":['+picNums+']}]&key=snqx_ch'

LINK = APILINK
r = requests.get( LINK )

p=re.compile(ur'\"voteid\":([\d]+),\"count\":\"([\d]+)\"')
result = re.findall(p,r.text)
#print result

class RankClass:
    num=0
    rank=0

rank = []

for i in range(0,285):
    thisData = RankClass()
    thisData.num,thisData.rank = result[i]
    thisData.num = int(thisData.num)
    thisData.rank= int(thisData.rank)
    #print thisData.num,thisData.rank
    rank.append(thisData)

#DEBUG
#for each in rank:
#    print each.num, each.rank

j=i
for i in range(1,285):
    j=i
    while j >= 1:
        if rank[j].rank > rank[j-1].rank:
            tempNum = rank[j].num
            tempRank= rank[j].rank
            rank[j].num = rank[j-1].num
            rank[j].rank= rank[j-1].rank
            rank[j-1].num = tempNum
            rank[j-1].rank= tempRank
            j=j-1
        else:
            break

i=1
for each in rank:
    print 'Rank:', i, '\t', 'ID:\t', each.num, '\tvote:\t', each.rank
    i = i+1

inp = raw_input()
