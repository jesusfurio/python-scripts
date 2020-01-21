import os

def usb_boot():
    os.system('lsblk')
    usb = input("Insert the USB path (/dev/sdx): ")
    os.system ('dd if=' + ruta + ' of=' + usb + ' bs=4M')

if __name__ == '__main__':
    ruta = input("Insert the ISO path to mount (/path/name.iso): ")
    usb_boot()
    print("USB boot created")