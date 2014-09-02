import os
import sys
import re

import os, re
regString="(\w+).\d.png"
for item in os.listdir('.'):
    if (re.match(regString, item)):
        print item
        newname = re.sub(r".(\d)", r"_\1", item)
        os.rename(item, newname)
        print "-->" + newname
        #break
   # print item