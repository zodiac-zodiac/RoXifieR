import Image
from pytesser import *
import glob
import os
os.chdir("/var/www/traffic_providor/images/samair/")
s = ''
for file in glob.glob("*.png"):
	print('STEP 2 : extracting text from :'+file)
	s = s+'\n' + image_file_to_string(file)
f = open('/var/www/traffic_providor/tmp/samair/ips.txt', 'w+')
f.write(s)
f.close() 
