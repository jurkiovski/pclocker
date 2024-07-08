import os
import time
import string
import ctypes
letters = list(string.ascii_uppercase)                      #abeceda v arrayi
b = 1	                                                    #jednotku dame do neznamej ktoru nikdy nepouzijeme ;) sak ty vies kam ma ist 
while True:
    lock_status = 0
    for i in letters:			                            #pre kazde pismenko (usb) skontrolujeme pritomnost suboru
        file_path = i + r":\unlock.txt"                     #vyskladame si cestu k suboru
        if os.path.exists(file_path):	                    #hladame subor
            print("File found at :",file_path)	            #nasli sme ho 
            lock_status = 1                                 #tak si to zaznacime
        else:
            print("File was not found at : ", file_path)    #alebo aj nie 
    if lock_status < 1:
        ctypes.windll.user32.LockWorkStation()		        #zamok PC
        print("Locking computer")
        
    time.sleep(1)   
