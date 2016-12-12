import re
import math
import time
import json

killed = open('killed.txt', 'r')
mutants = open('mutants.log', 'r')
killed.readline()
temp = killed.readline()
temp2 = mutants.readline()
with open("killed.txt") as f:
        for i, l in enumerate(f):
            pass
length = i + 1
toggle = True
skip = False
line = {}
info = []
final = ''
fails = 0
live = 0
totalKill = 0
totalLive = 0
print(length)
final = 'var data = {"lines": '

x = 0
while x < length:
	x += 1
	if toggle == True and x != length:
		temp3 = temp2.split('@classify:')[1].split(':', 1)[0]
		if(temp2.split(':', 1)[0] == temp.split(',')[0]):
			if(temp.split(',')[1].rstrip() == 'FAIL'):
				fails += 1
			else:
				diff = temp2.split('@classify:')[1].split(':', 1)[1].rstrip()
				temp5 = '{"id":' + '"' + temp.split(',')[0] + '",' + '"description":' + '"' + diff + '"}'
				info.append(temp5)
				live += 1
				x += -1
		else:
			skip = True
			x += -1
		if(skip == False):
			temp = killed.readline()
			temp2 = mutants.readline()
		else:
			x += -1
			temp2 = mutants.readline()
			skip = False
	else:
		temp6 = ''
		for b,i in enumerate(info):
			if(b != len(info)-1):
				temp6 += i + ','
			else:
				temp6 += i
		if(fails == 0):
			percent = 0
		elif(live == 0):
			percent = 1
		else:
			percent = str(round(fails/(live+fails), 2))
		final += '[{"id": "' + '%s' % temp3 + '", "percentage": "' + '%s' % percent + '", "live": [' + '%s' % temp6 + ']}], \n'
		info = []
		temp3 = temp2.split('@classify:')[1].split(':', 1)[0]
		percent = 0
		totalKill += fails
		totalLive += live
		fails = 0
		live = 0
		toggle = True
	if(temp2.split('@classify:')[1].split(':', 1)[0] != temp3):
		toggle = False
	else:
		toggle = True

final = final[:-3] + '}'
data = open('data.js', 'w')
data.write(final)
data.close()
if(totalKill == 0):
	totalPercent = 0
elif(totalLive == 0):
	totalPercent = 1
else:
	totalPercent = str(round(totalKill/(totalLive+totalKill), 2))
percentages = open('percent.js', 'w')
percentages.write('var totalpercent = {"killedPercentage": "%s", "livePercentage": "%s"}' % (totalPercent, str(round(1-float(totalPercent), 2))))
percentages.close()