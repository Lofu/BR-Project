import requests
from bs4 import BeautifulSoup
import json
import os
import time
import random
import smtplib
import unicodedata
import shutil
import csv


bookdata_url = open("crawlerBooks_20160110_distinct.txt","r").read().split("\n")[:-1]
aaaa = []
for aa in bookdata_url :
    aaa = aa.replace('"','')
    aaaa.append(aaa)
#bookjsonDict = {}
#nforDICT = {}
booklist = []
ttt = []
f = open( "bookbrowse_20160110_CSV.csv", "w",encoding='utf8')
f.write('書名,作者,內容簡介,作者簡介,名人推薦,書摘,詳細資料,折扣價格,主類別,子類別,出版社,出版日期,產品編號,\n')
for text_url in aaaa[0:2] :
    #print(text_url)
    #input()
    book_text = requests.get(text_url)
    book_text_real = BeautifulSoup(book_text.content)

    book_text_catch_title = book_text_real.findAll('h2',{"class":"node-title"})    # title書名
    for real_title in book_text_catch_title :
        #print("title" , real_title.text)
        real_title = real_title.text  # real title

    book_text_catch_writer = book_text_real.findAll('div',{"class":"book-authors"})# writer作者
    for real_writer in book_text_catch_writer :
        real_writer = real_writer.text 
        #print("writer",real_writer)
        #input()
    
    book_text_catch_info = book_text_real.findAll('div',{"id":"book-des"})# info內容簡介
    for real_info in book_text_catch_info:
        real_info = real_info.text 
        #print("info",real_info)
        #input()       
        
    book_text_catch_manu = book_text_real.findAll('div',{"id":"book-author-desc"})# menu作者簡介
    for real_manu in book_text_catch_manu:
        real_manu = real_manu.text 
        #print("menu" ,real_manu)
        #input()

    book_text_catch_summary = book_text_real.findAll('div',{"id":"book-specialtext"})# summary名人推薦
    for real_summary in book_text_catch_summary:
        real_summary = real_summary.text
        #print("summary" ,real_summary)
        #input()
    book_text_catch_detail = book_text_real.findAll('div',{"id":"book-shyue"})# detail書摘
    for real_detail in book_text_catch_detail:
        real_detail = real_detail.text 
        #print("detail" ,real_detail)
        #input()
    book_text_catch_ISBN = book_text_real.findAll('div',{"id":"book-more-detail"})# ISBN詳細資料
    for real_ISBN in book_text_catch_ISBN:
        real_ISBN = real_ISBN.text
        #t = random.randint(4,20)
        #time.sleep(t)
    book_text_catch_price = book_text_real.findAll('div',{"class":"sale-price ip"}) #價格 
    for real_price in book_text_catch_price :
        real_price = real_price.text

    book_text_catch_maintype = book_text_real.findAll('span',{"class":"inline odd"}) #主類別 
    for real_maintype in book_text_catch_maintype :
        real_maintype = real_maintype.text    
        #print(real_maintype)
    book_text_catch_viatype = book_text_real.findAll('span',{"class":"inline even"}) #子類別
    for real_viatype in book_text_catch_viatype :
        real_viatype = real_viatype.text   
        
    book_text_catch_pub = book_text_real.findAll('li',{"class":"shs-parent first"}) #出版社
    for real_pub in book_text_catch_pub :
        real_pub = real_pub.text            
        
    book_text_catch_pubdate = book_text_real.findAll('span',{"class":"date-display-single"}) #出版日期 
    for real_pubdate in book_text_catch_pubdate :
        real_pubdate = real_pubdate.text       

    book_text_catch_lab = book_text_real.findAll('span',{"class":"product-info-value"}) #產品編號
    for real_lab in book_text_catch_lab :
        real_lab = real_lab.text     
    t = random.randint(3,6)
    time.sleep(t)        
    booklist = [real_title, real_writer ,real_info ,real_manu ,real_summary ,real_detail , real_ISBN,real_price,real_maintype,real_viatype,real_pub,real_pubdate,real_lab] 
    ttt.append(booklist)

wr = csv.writer(f)
wr.writerows(ttt)    