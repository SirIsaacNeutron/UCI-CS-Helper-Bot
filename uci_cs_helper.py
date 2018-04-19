"""

@author SirIsaacNeutron
"""

import praw
import re


TRIGGER_PATTERN = re.compile(r'.*(switch(ing)?|transfer(ing)?|change?(ing)?|get(ing)?\s?in(to)?).*([^a-z]cs|comp(uter)?\ssci(ence)?)', re.IGNORECASE)

NUM_SUBMISSIONS = 1000  # The amount of comments to parse

MESSAGE = ("Beep, boop. I'm a bot and I noticed you mentioning switching "
            + "into CS. /u/What_question-mark made a pretty good comment "
            + "about that issue. It's very helpful if you are a non-CS "
            + 'major trying to switch into CS.'
            + 'You can see it here: https://www.reddit.com/r/UCI/comments/87djdj/new_student_have_questions_ask_here/dwelhou/'
            + "\nBut if you are already in the ICS school, it shouldn't be too "
            + 'hard to switch into CS or any other ICS major :).')

# Where client_id, client_secret, and the bot's username and
# password are stored
# (client_id is in the first line, client_secret the second, etc.)
CREDENTIALS_FILE_NAME = 'credentials.txt' 

# Stores the submission id's of all submissions the bot replied to
REPLIED_TO_FILE_NAME = 'repliedto.txt'

def _get_credentials_from(file_name: str) -> (str, str):
    """Return a tuple with all the credentials praw.Reddit() needs."""
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


def _in_replied_to_file(submission: 'submission') -> bool:
    """Return True if submission.id is in REPLIED_TO_FILE_NAME,
    else False.
    """
    with open(REPLIED_TO_FILE_NAME) as replied_to:
        return submission.id in replied_to

def _reply(submission: 'submission') -> None:
    """Reply to a submission and write the submission id
    to a file to keep track of submissions the bot replied to.
    """
    with open(REPLIED_TO_FILE_NAME, 'a') as replied_to:
        if not _in_replied_to_file(submission):
            submission.reply(MESSAGE)
            replied_to.write(submission.id + '\n')


def _debug(hot_submissions: 'hot_submissions') -> None:
    """Print the submission title and submission selftext
    of each submission the bot would reply to if it were
    actually running.
    """
    submission_num = 0
    for submission in hot_submissions:
        if _in_replied_to_file(submission):
            print('Submission ' + submission.id + ' was already replied to.')
            continue

        _print_percentage_done(submission_num / NUM_SUBMISSIONS) 

        submission_num += 1
        if text_about_switching_to_cs(submission.title):
            print('Should reply to submission:', submission.title)

        elif text_about_switching_to_cs(submission.selftext):
            print('Should reply to selftext:', submission.selftext)

    print('Finished!')


def _run_bot(hot_submissions: 'hot_submissions') -> None:
    """Have the bot reply to submissions that it thinks are about
    transferring to the CS major.
    """
    submission_num = 0
    for submission in hot_submissions:
        _print_percentage_done(submission_num / NUM_SUBMISSIONS) 

        submission_num += 1
        if text_about_switching_to_cs(submission.title):
            _reply(submission)
            print('Replied to', submission.title)

        elif text_about_switching_to_cs(submission.selftext):
            _reply(submission)
            print('Replied to selftext:', submission.selftext)

    print('Finished!')


if __name__ == '__main__':
    client_id, client_secret, my_username, my_password = _get_credentials_from(CREDENTIALS_FILE_NAME)

    reddit = praw.Reddit(client_id=client_id,
            client_secret=client_secret,
            user_agent='UCI_CS_Helper_Bot by /u/The_Atomic_Comb',
            username=my_username,
            password=my_password)

    uci = reddit.subreddit('UCI')

    hot_submissions = uci.hot(limit=NUM_SUBMISSIONS)
    _run_bot(hot_submissions)



