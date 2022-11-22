import requests
import re
import os
from bs4 import BeautifulSoup
import time

def download_page(url):
	r=requests.get(url)
	r.encoding="utf-8"
	return r.text

def create_dir(name):
   if not os.path.exists(name):
       os.makedirs(name)


def get_main_list(soup):
	pic_list=soup.find_all('div',class_='entry-media')
	for i in pic_list:
		href=i.find('a').get('href')
		text=i.find('a').find('img').get('alt')
		get_pic(href,text)


def get_pic(href,text):
	html=download_page(href)
	soup=BeautifulSoup(html,'lxml')
	headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
	pic_list=soup.find('div',class_='entry-wrapper').find_all('img')	
	create_dir('pic2/{}'.format(text))
	for i in pic_list:
		src=i.get('src')
		pic=requests.get(src)
		with open('pic/{}/{}'.format(text,src.split('/')[-1]),'wb') as f:
			f.write(pic.content)


def main():
	create_dir('pic2')
	for i in range(2,5):
		html=download_page("http://81.68.202.74/datu/xinggan/page/%s"%i)
		BeautifulSoup=BeautifulSoup(html,'lxml')
		get_main_list(soup)

if __name__=='__main__':
	main()
