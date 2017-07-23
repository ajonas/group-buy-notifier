import getpass
import logging
import praw
import requests
import smtplib
import time

# Enter api and user details below
CLIENT_ID = ''
CLIENT_SECRET = ''
USER_AGENT = 'Group Buy Notifier v0.1b by /u/deftony'
ALERT_USER = ''

USER_PASS = getpass.getpass('Enter reddit password for user {}: '
                             .format(ALERT_USER))

KEYWORDS = ['[GB]', 'Group Buy', 'group buy', 'Interest Check',
            '[IC]', 'interest check']

print('ok')
r = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, 
                user_agent=USER_AGENT, password=USER_PASS,
                username=ALERT_USER)
                
print('ok')
if r:
    print('ok') #TODO remove this
    
alert_user = r.redditor(ALERT_USER)
checked = []
    
#get newest posts from mechmarket
sub = r.subreddit('mechmarket')

while True:
    print('beginning loop..')
    for post in sub.new(limit=100):
        if any(key in post.title for key in KEYWORDS):
            if (post.id not in checked):
                print(post.title)
                message_body = 'Found new post "{}" with link {}'.format(
                                post.title, post.shortlink)
                alert_user.message('New GB or IC found', message_body)
        checked.append(post.id)
    
    print('sleeping for 5 minutes...')
    time.sleep(300)