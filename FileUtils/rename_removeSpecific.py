import os
import sys
import re

import os, re
regString="(\w+)@2x.png"
for item in os.listdir('.'):
    if (re.match(r"(\w+)@2x.png", item)):
        print item
        newname = re.sub(r"@2x", "", item)
        os.rename(item, newname)
        print "-->" + newname
   # print item