import os, platform, time, sys
os.system('git pull')
print('\033[1;32m Tools Is On Updating Please Wait...')
exit()
try: 
    import requests 
except: 
    os.system('pip install requests')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
    print('\033[1;32m Congratulations Your Phone Supported This Tools \033[0;m')
    from SUBHAN import KHAN
    KHAN()
elif bit == '32bit':
    print('\033[1;31m Sorry 32 bit Not Supported This Tools')
    exit()
