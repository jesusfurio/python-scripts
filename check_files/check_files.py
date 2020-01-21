import time, os

folder = ['/path1',
        '/path2']
delete_older_days = 10
now = time.time()

def clean_files():
    for i in folder:
        for j in os.listdir(i):
            f = os.path.join(i,j)
            if os.stat(f).st_mtime < now - (60*60*24*delete_older_days) and os.path.isfile(f):
                print ("...Deleting old files "+f)
                os.remove(f)

if __name__ == '__main__':
    clean_files()