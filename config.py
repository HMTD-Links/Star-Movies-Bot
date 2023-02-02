import os
import logging
from os import getenv
from os import environ

class Config(object):
      API_HASH = getenv("API_HASH", "5264bf4663e9159565603522f58d3c18")
      API_ID = int(getenv("API_ID", 11973721))
      BOT_TOKEN = getenv("BOT_TOKEN", "5949999646:AAGNAzsUTMutsqtnSk2R4MkGgCQ0uMtqbIU")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001342411240"))
