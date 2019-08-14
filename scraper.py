import sys
from funs import *
from pyfiglet import Figlet

print(Figlet(font='doom').renderText('Py_Scraper v1'))

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
