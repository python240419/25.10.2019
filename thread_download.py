import urllib.request
import threading
import time
import os

#url = 'https://d17fnq9dkz9hgj.cloudfront.net/uploads/2012/11/152964589-welcome-home-new-cat-632x475.jpg'

def download_file(url_file, tofile):
    urllib.request.urlretrieve(url, f'c:/itay/{filename}')

def counting(localFile, thread_ref, maxsize):
    last = -1
    while thread_ref.isAlive():
        time.sleep(1)
        curSize = os.stat(localFile).st_size
        if not curSize * 100 // maxsize == last: # print only if there was a progress
            last = curSize * 100 // maxsize
            print(f'%{curSize * 100 // maxsize}')

url = 'http://www.study-io.com/java/installations/mongodb-win32-x86_64-2008plus-ssl-3.6.3-signed.msi'
filename = os.path.basename('mongodb-win32-x86_64-2008plus-ssl-3.6.3-signed.msi')

download_file_thread = threading.Thread(target=download_file,
                                        args=(url, filename))
download_file_thread.start()

# get max size
d = urllib.request.urlopen(url)
maxsize = int(d.info().get('content-length'))

size_file_thread = threading.Thread(target=counting,
                                        args=('C:/itay/mongodb-win32-x86_64-2008plus-ssl-3.6.3-signed.msi', download_file_thread, maxsize))
size_file_thread.start()



