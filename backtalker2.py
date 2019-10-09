import os
import time
import re
import datetime as dt
from slackclient import SlackClient

from modules.all import *

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# backtalker's user ID in Slack: value is assignn
backtalker_id = None

# constants
RTM_READ_DELAY = 1
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"


def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == backtalker_id:
                return message, event["channel"]
    return None, None


def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # 1st gourp has username, 2nd group called remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    """
        Executes bot command if the command is known
    """
    default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)

    response = None

    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some code then I can do that!"
    elif command.startswith("date"):
        response = currentDate()
    elif command.startswith("time"):
        response = currentTime()
    elif command.startswith("your my best friend") or command.startswith("you are my best friend"):
        response = "Thanks so much, buddy!!! \n Your the best!!"
    elif command.startswith("hello") or command.startswith("hi") or command.startswith("hey"):
        response = "Hello, My name is BackTalker"
    elif command.startswith("thanks") or command.startswith("thank you"):
        response = "Your Welcome"
    elif command.startswith("math"):
        chopCommand = command.split(" ")
        response = "The answer for {} is {}".format(chopCommand[1], str(eval(chopCommand[1])))
    elif command.startswith("weather"):
        response = currentWeather()


    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Backtalker is connected and running!!")

        backtalker_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection is not working. Please check ur connection.")