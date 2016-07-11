#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
b_rating = 0.0
h_rating = 0.0
t_rating = 0.0
c_rating = 0.0
r_rating = 0.0
d_rating = 0.0

b_tweets = 0
h_tweets = 0
t_tweets = 0
c_tweets = 0
r_tweets = 0
d_tweets = 0


b_final = 0.0
h_final = 0.0
t_final = 0.0
c_final = 0.0
r_final = 0.0
d_final = 0.0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    	line = line.strip()

    # parse the input we got from mapper.py
    	word, count = line.split('\t', 1)
    # convert count (currently a string) to i
	count = float(count)
	if 'Bernie' in word:
		b_rating += count
		b_tweets += 1
	if 'Hillary' in word:
		h_rating += count
		h_tweets += 1
	if 'Trump' in word:
		t_rating += count
		t_tweets += 1
	if 'Cruz' in word:
		c_rating += count
		c_tweets += 1
	if 'Republican' in word:
		r_rating += count
		r_tweets += 1
	if 'Democrat' in word:
		d_rating += count
		d_tweets += 1


if b_tweets!=0:
	b_final = b_rating/float(b_tweets)


if h_tweets!=0:
	h_final = h_rating/float(h_tweets)


if t_tweets!=0:
	t_final = t_rating/float(t_tweets)


if c_tweets!=0:
	c_final = c_rating/float(c_tweets)


if r_tweets!=0:
	r_final = r_rating/float(r_tweets)


if d_tweets!=0:
	d_final = d_rating/float(d_tweets)

print 'Candidate\tRating\t\tTweets Rated\tFinal Rating' 
print 'Bernie\t\t',b_rating,'\t\t',b_tweets,'\t\t',b_final
print 'Hillary\t\t',h_rating,'\t\t',h_tweets,'\t\t',h_final
print 'Trump\t\t',t_rating,'\t\t',t_tweets,'\t\t',t_final
print 'Cruz\t\t',c_rating,'\t\t',c_tweets,'\t\t',c_final
print 'Republican\t',r_rating,'\t\t',r_tweets,'\t\t',r_final
print 'Democrat\t', d_rating,'\t\t',d_tweets,'\t\t',d_final

	#a.append([word,count])
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
#a.sort(key=lambda tup: tup[0])
#for x in a:
#    print(x)
# do not forget to output the last word if needed!
