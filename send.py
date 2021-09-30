
 # upload file along with data by python
import requests;
import glob
import os
def hconn_send() :
     list_of_files = glob.glob('/home/pi/test.py')
     # * means all if need specific format then *.jpg
     latest_file = max(list_of_files, key=os.path.getctime)
     print(latest_file)
     #----------------------------------------
     url = 'http://140.131.114.151/photo.php'
     file = {'myfile': open('%s'%latest_file,'rb')}
     r = requests.post(url, files=file)
     if r.status_code != 200:
         print('sendErr: '+r.url)
     else :
         print(r.text)
 # main
hconn_send();
