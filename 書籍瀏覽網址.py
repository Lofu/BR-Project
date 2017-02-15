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
    test_table = soup.findAll('div',{"class":"view-header"}) #由html原始碼發現，子類別網址藏在某tag底下
    #print(test_table)
    for num_2 in test_table :
        #print(num_2)
        for num_3 in  num_2.findAll('h3') :
            #print(num_3)
            for num_4 in num_3.findAll('a',{'href':True}):
                #print(num_4)
                ans = num_4['href']
                #print(ans)
                url_book_type_levels = []
                url_book_type_levels = url_top  + ans #列出各個子類別的網址，但子類別頁面中存在著很多分頁，若要自動翻頁則必須自動進入分頁網址，所以從子類別網址去找每種子類別有多少分頁
                #print(url_book_type_levels)
                #print('stop')
                response_1 = requests.get(url_book_type_levels)
                soup_1 = BeautifulSoup(response_1.content)
                test_table_1 = soup_1.findAll('li',{"class":"pager-last last"}) #在html中發現，有一個tag包含各子分類的最後一頁。
                #print(test_table_1)
                for test_table_2 in test_table_1 :
                   #print(test_table_2)
                    for num_5 in test_table_2.findAll('a',{'href':True}) :
                        #print(num_5)
                        table_num_5 = num_5['href'].split("=") #以=好做分割，抓出一個list，然後取後面是最大頁數的位置
                        #print(table_num_5[1])
                        table_num_5_int = int(table_num_5[1]) # 這一步就是取最大頁數的位置存入table_num_5_int
                        num_page = list(range(1,table_num_5_int+1)) #想數字有小到最大頁數存入新物件方便等等跟網址字串連接出子分類底下各分頁網址
                        num_page[:] = [str(x) for x in num_page]
                        num_page_list = []
                        num_page_list.append("") #這一步的原因是因為：子類別底下分頁的第一分頁就是子類別網址不包含?page=，所以必須自行定義一個空白字串位置來創造出第一分頁網址
                        num_page_list_new = num_page_list + num_page
                        #print(num_page_list_new)
                        for num_6 in num_page_list_new :  #連接字串開始，但因為分頁的數字list中有""這格空白字串，所以當字串位置數大於0就進行連接，否則不動，這樣就能造出第一分頁就是子類別的網址，其他分頁則是加上頁數
                            if len(num_6) > 0:
                                test_num_6 = url_book_type_levels + "?page=" + num_6
                            else:
                                test_num_6 = url_book_type_levels
                            #print(test_num_6)
                            response_6 = requests.get(test_num_6) #抓出分頁後，最後要抓出分頁中每一本書的編號放在網址的後面就能進入要爬資料的頁面
                            soup_6 = BeautifulSoup(response_6.content) #為了自動抓出這些數字，所以針對頁面解析，希望能找出每個分頁連接最後頁面的網址
                            test_table_6 = soup_6.findAll('div',{"class":"book-title"})
                            #print(test_table_6)
                            for num_7 in test_table_6 :
                                #print(num_7)
                                for num_8 in num_7.findAll('a',{"href":True}) :
                                    #print(num_8)
                                    #print('stop')
                                    num_8_test = num_8['href'].split("/")
                                    #print(num_8_test)
                                    num_8_booknum = num_8_test[4]
                                    #print(num_8_booknum)
                                    num_8_booknum_new =  url_book_type_levels + "/" + str(num_8_booknum)
                                    #print("ready" , num_8_booknum_new)
                                    f.write(num_8_booknum_new + "\n")    