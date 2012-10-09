#!/usr/bin/env python
import sys
import subprocess
xivname = subprocess.Popen(["xcli", "-L"],stdout=subprocess.PIPE)
xivname2 =  xivname.communicate() [0]
xivname3 = xivname2.splitlines()
for line in xivname3[1:]:
	line = line.replace("," , "")
	line = line.split()
	iplist = " "
	for ip in line[1:]:
		iplist = iplist + " " + ip

	print line[0]," ",iplist

	
		





