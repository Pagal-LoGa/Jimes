import os, platform
try:
   import requests
except:
   os.system('pip install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Filpp import maping
    maping()
elif bit == '32bit':
    from Filpp import maping
    maping()
