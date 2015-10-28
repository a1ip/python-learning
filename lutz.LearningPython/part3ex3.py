#!/usr/bin/env python3

SL={'x':1,'f':7,'i':6}
print ("list:", SL)
print ("sorted dict")
for x in sorted(SL.keys()):
	print ('for key \'%s\' value = %s' % (x,SL[x]))
