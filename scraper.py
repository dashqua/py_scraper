import requests
from bs4 import BeautifulSoup
import time 
from datetime import datetime

URL = 'https://www.amazon.co.uk/Hydration-Bladder-Reservoir-Approved-Backpacking/dp/B07BVNQXCJ/ref=sr_1_16?keywords=hydration+bladder&qid=1565718054&s=gateway&sr=8-16'
DUMP_FILE = "dump_file.log"
COOLDOWN_TIME_SEC = 5

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

while (True):
	time.sleep(COOLDOWN_TIME_SEC)
	tic = time.time()
	f_time = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
	print("[+] %s" % f_time)
	price = get_price(URL)
	toc = time.time()
	with open("DUMP_FILE","a+") as f:
		f.write("%f \t %f \t %f\n" % (tic, price, toc-tic))
	f.close()
	print("[+] Data written in %s\n" % DUMP_FILE)
