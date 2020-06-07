import os
from datetime import date
today = date.today()
d1 = today.strftime("%d/%m/%Y")
_src = "/path/to/directory/"
_ext = ".txt"
for i,filename in enumerate(os.listdir(_src)):
    if filename.endswith(_ext):
        os.rename(filename, _src+d1 + str(i).zfill(3)+_ext)
