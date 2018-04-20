# UCI CS Helper Bot

This is a simple bot for Reddit that is meant to help out people at UCI. As I browse /r/UCI, I noticed that there are quite a few people who want to become Computer Science majors, but were accepted as Undeclared/Undecided, or as an non-CS, alternative major. So I got an idea to make this bot in order to help these people out. 

The bot goes through a bunch of hot submissions in [/r/UCI](https://www.reddit.com/r/UCI/) and checks their titles and their text with a regular expression. If the title or the text of the submission matches the regular expression, and if the bot does not see the submission's id in repliedto.txt, the bot will reply to the submission with a message. 

Unfortuately, I was unable to get the bot to deal with comments. In its current state, the bot will respond to pretty much any message dealing with the topic of changing major to Computer Science, even if the message is not actually soliciting advice about how to get into the CS major. I thought of using some sort of NLP to help the bot deal with comments, but I know nothing about how to go about doing that, and I was in a rush to test this bot out in the real world. I was in such a rush because I was aware that it was a little bit late for my bot to help many people, and I didn't want to spend too long trying to learn NLP -- which is certainly a complicated subject -- only to have to test my bot out on posts and comments that are quite old. I already had to learn [PRAW](https://github.com/praw-dev/praw) and I decided that it would be better to keep my bot simple for now, as this was my first bot for Reddit.

However, I am satisfied with my bot, and I am happy to show its source code to the world. It was challenging coming up with an appropriate regular expression. I found [regex101.com](https://regex101.com/) to be invaluable in that regard. 


## Built With
* [PRAW](https://github.com/praw-dev/praw) -- "a python package that allows for simple access to Reddit's API."


