import sys, os.path, time, shutil
import datetime as dt

for root,dirs,files in os.walk('/Users/slnburg/Desktop/Folder A/'):

    for file_name in files:
        now = dt.datetime.now()
        before = now - dt.timedelta(minutes=1440)
        path = os.path.join(root,file_name)
        st = os.stat(path)

        mod_time = dt.datetime.fromtimestamp(st.st_mtime)
        if mod_time > before:
            shutil.copy(os.path.join(root, file_name), '/Users/slnburg/Desktop/Folder B/') 
