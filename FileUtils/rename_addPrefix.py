import os
import sys
import re

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
os.chdir(dirname)
fileList = os.listdir(dirname)
print dirname
name='edge_effect_'
for fileItem in fileList:
	dotIndex = fileItem.rfind('.')
	fileName = fileItem[: dotIndex]
	fileExt = fileItem[dotIndex : ]
	print fileName,fileExt
	#m=re.search("[^qd]\w+",fileName)
	if fileName.find(name)<0 and fileName.find("rename")<0:
		print "111"
		os.rename(fileItem,name+fileName+fileExt)
	 	pass 
	#print 'm.group:'m.group(0)