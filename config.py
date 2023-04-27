import os

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    API_KEY = os.environ.get("API_KEY")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))
