"""
The logic for the bot. Upon running the bot, the user will be asked whether
he wants to run the bot in debug mode or not. Running in debug mode will have the bot display which submissions it would respond to if it were actually running.

@author SirIsaacNeutron
"""

import praw
import re
import argparse

TRIGGER_PATTERN = re.compile(r'(switch(ing)?|transfer(ring)?\s*(in|into|to)|change?(ing)?|get(ing)?\s*in(to)?).{1,30}([^a-z]cs[^a-z]|comp(uter)?\s*sci(ence)?)', re.IGNORECASE)

NUM_SUBMISSIONS = 1000  # The amount of submissions to parse

MESSAGE = ("Beep, boop. I'm a bot and I noticed you mentioning switching "
           + "into CS. /u/What_question-mark made a pretty good comment "
           + "about that issue. It's very helpful if you are a non-CS "
           + 'major trying to switch into CS. '
           + 'You can see it here: https://www.reddit.com/r/UCI/comments/87djdj/new_student_have_questions_ask_here/dwelhou/'
           + "\n\nBut if you are already in the ICS school, it shouldn't be too "
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
        for line in replied_to:
            if submission.id in line:
                return True

    return False


def _reply(submission: 'submission') -> None:
    """Reply to a submission and write the submission id
    to a file to keep track of submissions the bot replied to.
    """
    with open(REPLIED_TO_FILE_NAME, 'a') as replied_to:
        submission.reply(MESSAGE)
        replied_to.write(submission.id + '\n')


def _debug(hot_submissions: 'hot_submissions') -> None:
    """Print the submission title and submission selftext
    of each submission the bot would reply to if it were
    actually running.
    """
    print('DEBUG MODE')
    submission_num = 0
    for submission in hot_submissions:
        if _in_replied_to_file(submission):
            print('Submission ' + submission.id + ' was already replied to.')
            print('\tTitle:', submission.title)
            continue

        submission_num += 1
        if text_about_switching_to_cs(submission.title):
            print('Should reply to submission:', end=' ')
            print(submission.id, submission.title)

            _print_percentage_done(submission_num / NUM_SUBMISSIONS)
        elif text_about_switching_to_cs(submission.selftext):
            print('Should reply to selftext:', end=' ')
            print(submission.id, submission.selftext)

            _print_percentage_done(submission_num / NUM_SUBMISSIONS)
    print('Finished!')


def _run_bot(hot_submissions: 'hot_submissions') -> None:
    """Have the bot reply to submissions that it thinks are about
    transferring to the CS major.
    """
    print('Running...')
    submission_num = 0
    for submission in hot_submissions:
        if _in_replied_to_file(submission):
            print('Submission ' + submission.id + ' was already replied to.')
            print('\tTitle:', submission.title)
            continue

        submission_num += 1
        if text_about_switching_to_cs(submission.title):
            _reply(submission)
            print('Replied to', submission.title)

            _print_percentage_done(submission_num / NUM_SUBMISSIONS)
        elif text_about_switching_to_cs(submission.selftext):
            _reply(submission)
            print('Replied to selftext:', submission.selftext)

            _print_percentage_done(submission_num / NUM_SUBMISSIONS)

    print('Finished!')


def _create_arg_parser() -> argparse.ArgumentParser:
    """Create all the command line functionality for the bot."""
    arg_parser = argparse.ArgumentParser(description='A bot for Reddit to help out Anteaters who want to switch into CS')
    arg_parser.add_argument('-r', '--run',
            dest='run_bot',
            help='have the bot actually reply to submissions',
            action='store_true')
    arg_parser.add_argument('-d', '--debug',
                        dest='debug_bot',
                        help='merely display the submissions the bot would reply to',
                        action='store_true')

    return arg_parser 


def _initialize_bot_and_get_hot_subms() -> 'hot_submissions':
    """Log the bot into Reddit and return a ListingGenerator representing 
    hot submissions from the UCI subreddit.
    """
    credentials_tuple = _get_credentials_from(CREDENTIALS_FILE_NAME)
    client_id, client_secret, user_agent, username, password = credentials_tuple

    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent,
                         username=username,
                         password=password)

    uci = reddit.subreddit('UCI')
    hot_submissions = uci.hot(limit=NUM_SUBMISSIONS)

    return hot_submissions


if __name__ == '__main__':
    arg_parser = _create_arg_parser()
    args_dict = vars(arg_parser.parse_args())
    
    if args_dict['debug_bot'] is True:
        hot_submissions = _initialize_bot_and_get_hot_subms()
        _debug(hot_submissions)
    elif args_dict['run_bot'] is True:
        hot_submissions = _initialize_bot_and_get_hot_subms()
        _run_bot(hot_submissions)
    else:
        arg_parser.print_help()
