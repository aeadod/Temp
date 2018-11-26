import os
libs=['matplotlib','sklearn','wheel','beautifulsoup4','networkx',\
      'sympy','flask']
try:
    for i in libs:
        os.system("pip install "+i)
    print("ok")
except:
    print("error")
