import time
import os
from random import randrange
from slackclient import SlackClient

# Cont variable
SLACK_CLIENT = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
BOT_ID = SLACK_CLIENT.api_call("auth.test")["user_id"]
CHANNEL_LIST = SLACK_CLIENT.api_call("channels.list").get("channels", [])
ANSWER_LIST = [
    "Umm, interesting I will ask my master for its meaning",
    "I think it cool",
    "Howdy!",
    "What's up?",
    "I see",
    "Anythings else?",
    "I'm done!!!"
]

def findChannelsID(channelName, channelList):
    """
    """
    match = [ch.get("id") for ch in channelList if ch.get("name") == channelName]
    return match[0]

if __name__ == "__main__":
    """
    """
    if (SLACK_CLIENT.rtm_connect(with_team_state=False)):
        print("I'm online rn, please order me...")
        responseChannels = findChannelsID("general", CHANNEL_LIST)
        SLACK_CLIENT.api_call(
            "chat.postMessage",
            channel=responseChannels,
            text="Hello, My name is BackTalker",
        )
        while True:
            data = SLACK_CLIENT.rtm_read()
            if not data:
                continue
            else:
                newData = data[0]
                print(newData)
                if (newData.get("type") == "message") and (newData.get("subtype") != "bot_message"):
                    SLACK_CLIENT.api_call(
                        "chat.postMessage",
                        channel=responseChannels,
                        text=ANSWER_LIST[randrange(len(ANSWER_LIST))]
                    )
            
            time.sleep(1)
    else:
        print("Something wrong, please check your internet connection!")