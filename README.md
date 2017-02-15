# BR-Project
網路書店的書籍資料內容爬蟲，包含：價位、書籍簡介、摘要、出版社與ISBN等等

# python 爬蟲紀錄

--

## 前言

經過三個月的爬蟲工作，從一開始不知從何下手，到現在一般的網站資料爬取應該沒什麼大問題，以下將會分享一些我收藏的**資源**與進行爬蟲時的一些小心得。

## 目的

希望整理出網路書店刊登販售的書籍內容資料進行文字資料分析，並且整理成一份可以進行資料分析的資料集，利用此資料挖掘網路商店的書籍銷售訊息。

## 套件資料整理與簡介

**Requests** 與 **BeautifulSoup** 這兩個套件在Python crawler世界中扮演著關鍵性的角色。

**Requests** 套件主要是用來對欲爬取資料的網站後台發出請求，並幫助我們確認該網頁是否可以正常連接。

**BeautifulSoup** 則是解析欲分析的網頁原始碼，使得我們可以獲得乾淨的網頁原始碼後便可以藉由尋找標籤的方式找出我們有興趣的資料。

**Captcha** 俗稱驗證碼，其實算是一個小魔王，如何有效得突破驗證碼登入該網站後來爬取資料，應該是很多人煩惱的點，在這邊提供一個較為簡單的方式來突破，但是相對的也有其缺點。


相關學習資源網址整理如下：

* **Requests**
	* [Requests爬虫技巧](http://www.jianshu.com/p/cba83709c64c)
	* [Python爬虫利器一之Requests库的用法](http://cuiqingcai.com/2556.html)
	* [[Python] Requests 教學](http://zwindr.blogspot.tw/2016/08/python-requests.html)
	* [Requests官方文件(翻譯版)](http://docs.python-requests.org/zh_CN/latest/user/advanced.html)
	* [Requests: HTTP for Humans
](http://docs.python-requests.org/en/master/)

* **BeautifulSoup** 
	* [Python爬虫利器二之Beautiful Soup的用法](http://cuiqingcai.com/1319.html)
	* [Beautiful Soup 4.4.0 documentation ](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

* **Captcha**
	* [Captcha Solve](https://pypi.python.org/pypi/captcha-solver)

## 網路書店的書籍資料爬取步驟解析

我所針對的網路書店官網網址在此：[Touch me](http://www.bookrep.com.tw/)

### 1. 觀察

菜鳥經過一段時間的琢磨後，其實在整個過程中多多少少會有許多做**白工**的地方，造成你花費很多時間的主要因素，我自己認為在於對欲爬取網站的**觀察**。

大家點進官網網址後，可以發現此官網主要分為幾個大類：書籍瀏覽、得獎好書、特色作家等等，點進去某個類別之後，大家會發現類別之中存在著子類別，接續著下去到刊登的書籍，最後點入刊登書籍則會進入該書籍的內容介紹、摘要、作者簡介等等的頁面，這個頁面才是我們有興趣的頁面，所以















