# -*- coding: utf-8 -*-
"""
Author:  hnjzsdx
Website: hnjzsdx.com
         https://github.com/wisecube-cn
E-mail:  hnjzsdx.gamil.com
"""

from urllib import request

#Import your bilibili ID
vmid='35156038'#my ID
#vmid='122879'#敖厂长's ID

#Using bilibili API 
url = 'http://api.bilibili.com/x/relation/stat?vmid='+vmid
req = request.Request(url)
page = request.urlopen(req).read()
page = page.decode('utf-8')
#print(page)

#Using Regex to find out the number of fans
import re
string=page
fansNum=re.findall('"follower":([0-9]*)',string,flags=0)
#print('Fans Number:')
#print(fansNum)
num=int(fansNum[0])
print(num)
