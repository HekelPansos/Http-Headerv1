#coding: UTF-8
#BY: DARK<VIPER>
#SUPPORT: 爪丹尺Ｓモㄥ工れモ♥
import random
import sys
import time
import urllib
import os
def mengetik(s):
      for c in s+'\n ' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random()*0.1)
os.system('clear')
hijau = '\x1b[1;92m'
cyan = '\x1b[1;96m'
kuning = '\x1b[1;93m'
ungu = '\x1b[1;95m'
putih = '\x1b[1;97m'
biru = '\x1b[1;94m'
merah = '\x1b[1;91m'
print
print '\x1b[1;96m'
logo = """
               _           _    ___                                
  /\  /\  ___ | | __  ___ | |  / _ \  __ _  _ __   ___   ___   ___ 
 / /_/ / / _ \| |/ / / _ \| | / /_)/ / _` || '_ \ / __| / _ \ / __|
/ __  / |  __/|   < |  __/| |/ ___/ | (_| || | | |\__ \| (_) |\__ \

\/ /_/   \___||_|\_\ \___||_|\/      \__,_||_| |_||___/ \___/ |___/"""
print (logo)
print ("\x1b[1;91m               <!•HTTP HEADER B""\x1b[1;97mY DARK<VIPER>•!>")
time.sleep(2)
print
print
print "\x1b[1;93m ############################################"
mengetik("\x1b[1;95m [~]Author : DARK<VIPER>")
mengetik("[~]Support: 爪丹尺Ｓモㄥ工れモ♥")
mengetik("[~]Github : https://github.com/HekelPansos")
mengetik("[~]Team   : InfectSecurity")
mengetik("[~]Phone  : +6283862851420")
print "\x1b[1;93m############################################"
time.sleep(1)
print
print
mengetik("\x1b[1;97m=>> ""\x1b[1;94mContoh: http://www.google.com\x1b[1;91m"" \x1b[1;97m<<=\x1b[1;97m")
print
urli = raw_input("\x1b[1;92m[•Masukkan URL Target•]=>>""\x1b[1;97m ")
time.sleep (1)
print '\x1b[1;97m'
respon_kode = urllib.urlopen(urli)
if respon_kode.code == 200:
	print respon_kode.headers

print '\x1b[1;97m'
 
