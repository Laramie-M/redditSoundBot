import time
import praw

r = praw.Reddit('Sound cloud test bot by J_Mallory v 1.0')
r.set_oauth_app_info(client_id='rPfCPCykpQ5V2w',
                     client_secret="aTgnyAZ6lLFNZjRV_g76qh4GEaE",
                     redirect_uri='https//127.0.0.1:65010/authorize_callback')
existing_posts = []

while True:
    subreddit = r.get_subreddit('financialindependence')
    for submission in subreddit.get_new(limit=10):
        title = submission.title
        print(title)
        if title not in existing_posts:
            existing_posts.append(title)
            print("added post")
        else:
            print("I've seen this post")
    time.sleep(100)
