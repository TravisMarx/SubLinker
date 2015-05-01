import time
import praw
import re

r = praw.Reddit('Mentioned Subreddit linker v 1.0')

r.login("", "")


regex = ur"(?:r/).[^\(\)\]\.\s\:]*"
done = open('done.txt', 'a+')
already_done = []
	
dontLink = [' ']
subList = [' ']

while True:
	print ("Scanning...")
	subreddit = r.get_subreddit(subList)
	for submission in subreddit.get_new(limit=300):
		# Just variables
		op_title = submission.title.lower()
		subtolink = re.findall(regex, op_title)
		trueSub = ''.join(subtolink)
		addedComment =  " /%s "  % trueSub
		# Start checking and doing stuff
		if (
	 	len(subtolink) > 0
		and submission.id not in already_done
		and trueSub not in dontLink):
			submission.add_comment(addedComment)
			already_done.append(submission.id)
			done.write(submission.id +'\n')
			print ("""Comment added to %s titled "%s""" % (submission.id, submission.title))
		# Nothing there? Skip it.
		else:
			pass
	print ("Sleeping...")
	print ("Commented on %s items total this session" % len(already_done))
	time.sleep(300) #Time to wait before next check
	
			
