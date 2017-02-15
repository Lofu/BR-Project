import requests
from bs4 import BeautifulSoup
import json
import os
import time
import random
import smtplib

url_top = 'http://www.bookrep.com.tw' #官網網址
url_book = 'http://www.bookrep.com.tw/book' #官網首頁點擊書籍瀏覽後的網址
type_book = list(range(472,478)) #書籍瀏覽底下有文學小說～其他等類別，其網址規律故先取出期數字方便做字串連接
#type_book_oth = [17,517] 原本要用這個但後來用下面那行即可
join = [17] + type_book + [517] #這些數字拿來與url_book連接，就能得到書籍瀏覽底下各類別網址

# write a crawler books web address file
f = open("crawlerBooks_20160215.txt" , "w")

for num_1 in join :
    url_book_type = url_book + "/" + str(num_1) #字串連接後得到書籍瀏覽底下各類別網址，但各類別底下又存在各種子類別的書籍，
    #例如：華文創作、世界古典文學等，所以必須進入每一種類別，抓取該類別中的所有種類網址
    #print(url_book_type)
    response = requests.get(url_book_type) 
    soup = BeautifulSoup(response.content)
    print(soup)