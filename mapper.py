#!/usr/bin/env python

import sys


blist = ["Bernie Sanders","#bernie","Sanders","#Bernie2016", "@berniesanders","#feelthebern"]
clist = ["Senator Ted Cruz","Ted Cruz","Senator Ted Cruz","SenTedCruz"]
dlist = ["Democrat"]
hlist = ["Hillary Clinton","@HillaryClinton","Clinton","Hillary"]
rlist = ["Republican"]
tlist = ["Donald Trump","Trump",  "@realDonaldTrump", "#Trump"]

positive = []
negative = []
sent     = []
fo = open('positive.txt','r')
for line in fo:
    positive.append(line.replace('\n',""))
fo.close()
 
fo = open('negative.txt','r')
for line in fo:
    negative.append(line.replace('\n',""))
fo.close()
 
fo = open('sent_words.txt','r')
for line in fo:
    sent.append(line.replace('\n',"").split('\t'))
fo.close()

rating = 0.0
# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	if "TwEeT: " in line:
		line = line.strip()
		# split the line into words
		line = line.replace(':',',')
                line = line.replace(',','')
                line = line.replace('!','')
		for x in positive:
        		if x in line.lower():
            			rating += .5
		for x in negative:
        		if x in line.lower():
            			rating -= .5

		for x in sent:
        		if x[0] in line.lower():
            			rating += float(x[1])

		for w in blist:
			if w.lower() in line.lower().split():
				print '%s\t%s' % ('Bernie',rating)
		for w in hlist:
			if w.lower() in line.lower().split():
				print '%s\t%s' % ('Hillary',rating)
		for w in tlist:
			if w.lower() in line.lower().split():
				print '%s\t%s' % ('Trump',rating)
		for w in clist:
			if w.lower() in line.lower().split():
				print '%s\t%s' % ('Cruz',rating)
		for w in rlist:
			if w.lower() in line.lower().split():
				print '%s\t%s' % ('Republican',rating)
		for w in dlist:
			if w.lower() in line.lower().split():
				print '%s\t%s' % ('Democrat',rating)

