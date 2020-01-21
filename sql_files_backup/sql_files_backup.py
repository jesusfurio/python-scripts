import os
from datetime import datetime, date
from ftplib import FTP

backup_origin_path="/var/docker"

#Remote directory where the backup will be placed
remotedir=os.environ.get('FTP_PATH')

d = datetime.today().strftime('%Y-%m-%d')

sql_file = "docker01-alldatabases-" + d + ".sql"
storage_file="docker01-storage-"+d+".tgz"

def create_backup():

    userdata=os.environ.get('DATABASE_USER')
    passworddata=os.environ.get('DATABASE_PASSWORD')
    hostdata=os.environ.get('DATABASE_HOST')
    portdata=os.environ.get('DATABASE_PORT')

    os.system('umask 177')

    command_list = ['mysqldump --user=' + userdata + ' --password=' + passworddata + ' --host=' + hostdata + ' --port=' + portdata + ' --all-databases > ' + sql_file,
                    'tar -zcvf ' + sql_file + '.tgz ' + sql_file,
                    'rm ' + sql_file]

    for i in command_list:
        os.system(i)

    os.system('tar -zcf '+storage_file+' /var/docker/storage/')
    print("Backup complete")

def clean_backup():

    command_list = ['rm -f ' + backup_origin_path + '/' + sql_file,
                    'rm -f ' + backup_origin_path + '/' + sql_file + '.tgz',
                    'rm -f ' + backup_origin_path + '/' + storage_file]

    for i in command_list:
        os.system(i)

    print("Local backup removed")

def ftp_send():
    userftp=os.environ.get('FTP_USER')
    passwordftp=os.environ.get('FTP_PASSWORD')
    server=os.environ.get('FTP_SERVER')

    ftp = FTP(server)
    ftp.login(user=userftp, passwd=passwordftp)

    with open(sql_file, 'wb') as fp:
        ftp.retrbinary('RETR ' + sql_file, fp.write)
    ftp.quit()

def scp_send():
    userscp = os.environ.get('SCP_USER')
    serverscp = os.environ.get('SCP_SERVER')
    os.system('scp ' + sql_file + '.tgz '+ userscp + '@' + serverscp + ':' + remotedir)
    os.system('scp ' + storage_file + ' ' + userscp + '@' + serverscp + ':' + remotedir)    

if __name__ == '__main__':
    TYPE=2

    os.system('cd ' + backup_origin_path)
    create_backup()

    if TYPE == 1:
        ftp_send()
    elif TYPE ==2: 
        scp_send()
    else:
        print('Please select a valid type')

    print('Remote backup complete')
    clean_backup()