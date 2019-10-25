import urllib.request
import threading
import time
import os

def download_file(url, tofile):
    urllib.request.urlretrieve(url, tofile)

def counting(localFile, thread_ref, maxsize):
    last = -1
    while thread_ref.isAlive():
        time.sleep(1)
        curSize = os.stat(localFile).st_size
        if not curSize * 100 // maxsize == last: # print only if there was a progress
            last = curSize * 100 // maxsize
            print(f'%{curSize * 100 // maxsize}')

url = 'http://www.study-io.com/java/installations/mongodb-win32-x86_64-2008plus-ssl-3.6.3-signed.msi'
filename = os.path.basename(url)
filename_full = f'c:/itay/{filename}'
download_file_thread = threading.Thread(target=download_file,
                                        args=(url, filename_full))
download_file_thread.start()

# get max size
d = urllib.request.urlopen(url)
maxsize = int(d.info().get('content-length'))

size_file_thread = threading.Thread(target=counting,
                                        args=(filename_full, download_file_thread, maxsize))
size_file_thread.start()



