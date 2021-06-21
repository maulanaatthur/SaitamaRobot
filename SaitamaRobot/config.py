# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/SaitamaRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 5725735  # integer value, dont use ""
    API_HASH = "a05b5afc608813c21d67540445bd1ae1"
    TOKEN = "1841281724:AAEdzxODiFAl2pQ7mJyBtwHiQh0mFYcKNjo"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5725735  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "greatestpeopl3"
    SUPPORT_CHAT = "indonesiamillennials"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -584281546
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
       -584281546
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "something://somewhat:user@hosturl:port/databasename"  # needed for any database modules # its "URI" and not "URL" as herok and similar ones only accept it as such
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "calFipcPse18_POnbHj6vxoxRVsZEkvvqeTmElKM0eEUzutkll920fatE2e6yiG9"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        1  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "J6YSX98TCJESPN0X"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "30ZGG5QMQPKR"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "a5914bb1fd978b026c68395ed580947ffd12fb8369426bb93f3b6f4312210215916345889cb503942d65d797e878aea2973bcb5aaec545f2363d9df7803e7799"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
