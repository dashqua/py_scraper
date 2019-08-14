import requests
from bs4 import BeautifulSoup
import time 
from datetime import datetime
import os
try:
  from conf import *
  print("[+] Config file found\n")
except ImportError:
	print("[+] Config file not found\n")
	sys.exit()

CWD = os.getcwd()

def get_price(URL):
	headers = {
		"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

	print("[+] Contacting the page")
	page = requests.get(URL, headers=headers)
	print("[+] Page received")

	soup1 = BeautifulSoup(page.content, 'lxml')

	soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

	price = soup1.find(id="priceblock_ourprice").get_text()[1:]
	f_price = float(price)
	print("[+] Price found: %s" % f_price)

	return f_price



