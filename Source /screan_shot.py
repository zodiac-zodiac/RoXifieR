#!/usr/bin/env python
from selenium import webdriver
import os 

profile = webdriver.FirefoxProfile(os.path.expanduser("~/.mozilla/firefox/a6mpn2rf.default"))
browser = webdriver.Firefox(firefox_profile=profile) 
for i in range(8):
	browser.get('http://www.cool-proxy.net/proxies/http_proxy_list/page:'+str(i))
	browser.save_screenshot('page'+str(i)+'.png')
	print('STEP 1 : taking screan shots from '+str(i))

browser.quit()

#http://www.freeproxylists.net/fr/?u=10&page=1
#http://proxylist.hidemyass.com/1
#http://www.samair.ru/proxy/proxy-30.htm
#http://www.getproxy.jp/en/default/5
#http://www.cool-proxy.net/proxies/http_proxy_list/page:6