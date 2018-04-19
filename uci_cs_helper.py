"""

@author SirIsaacNeutron
"""

import praw
import re


TRIGGER_PATTERN = re.compile(r'.*(switch(ing)?|transfer(ing)?|change?(ing)?|get(ing)?\s?in(to)?).*([^a-z]cs|comp(uter)?\ssci(ence)?)', re.IGNORECASE)

NUM_SUBMISSIONS = 1000  # The amount of comments to parse

MESSAGE = ("Beep, boop. I'm a bot and I noticed you mentioning switching "
            + 'into CS. /u/What_question-mark made a pretty good comment '
            + 'about that issue. '
            + 'You can see it here: https://www.reddit.com/r/UCI/comments/87djdj/new_student_have_questions_ask_here/dwelhou/')

# Where client_id and client_secret are stored
# (client_id is in the first line, client_secret the second)
CREDENTIALS_FILE_NAME = 'credentials.txt' 

# Stores the submission id's of all submissions the bot replied to
REPLIED_TO_FILE_NAME = 'repliedto.txt'

def _get_credentials_from(file_name: str) -> (str, str):
    credentials_tuple = tuple()
    with open(file_name) as credentials_file:
        for line in credentials_file:
            line = line.rstrip('\n')
            credentials_tuple += (line,)

    return credentials_tuple


def _print_percentage_done(decimal: float) -> None:
    print('Percentage done:', end=' ')
    print(str(decimal * 100) + '%')


def text_about_switching_to_cs(text: str) -> bool:
    """Return True if a post or comment triggers a bot response,
    else False.
    """
    return True if TRIGGER_PATTERN.search(text) else False


def _reply(submission: 'submission') -> None:
    """Reply to a submission and write the submission id
    to a file to keep track of submissions the bot replied to.
    """
    pass 

if __name__ == '__main__':
    client_id, client_secret = _get_credentials_from(CREDENTIALS_FILE_NAME)

    reddit = praw.Reddit(client_id=client_id,
            client_secret=client_secret,
            user_agent='UCI_CS_Helper_Bot')

    uci = reddit.subreddit('UCI')

    hot_submissions = uci.hot(limit=NUM_SUBMISSIONS)
    current_location = 0

    for submission in hot_submissions:
        _print_percentage_done(current_location / NUM_SUBMISSIONS) 

        current_location += 1
        if text_about_switching_to_cs(submission.title):
            print('Should reply to submission:', submission.title)
            continue

        elif text_about_switching_to_cs(submission.selftext):
            print('Should reply to selftext:', submission.selftext)
            continue

    print('Finished!')
