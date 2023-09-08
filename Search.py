
import webbrowser
import time
time.sleep(10)


import os
from random import randrange


print("test")
url="https://www.bing.com/search?q="
#webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
#for i in range(40,0,-1):
#	url1=url+str(randrange(1,1000))
#	webbrowser.get('chrome').open_new_tab(url1)
#	time.sleep(1)
#additional comments
webbrowser.register('edge',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"))
for i in range(40,0,-1):
	url1=url+str(randrange(1,1000))
	webbrowser.get('edge').open_new_tab(url1)
	time.sleep(1)

webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
for i in range(40,0,-1):
	url1=url+str(randrange(1,1000))
	webbrowser.get('firefox').open_new_tab(url1)
	time.sleep(1)

#os.system("taskkill /im chrome.exe /f")
#time.sleep(5)
os.system("taskkill /im msedge.exe /f")
time.sleep(5)
os.system("taskkill /im firefox.exe /f")
time.sleep(5)