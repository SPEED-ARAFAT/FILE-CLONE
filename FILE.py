import os, sys, platform,time
 
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('git pull')
    os.system('chmod 777 FILE64;./FILE64')
elif bit == '32bit':
    os.system('clear')
    os.system('git pull')
    os.system('chmod 777 FILE32;/.FILE32')
