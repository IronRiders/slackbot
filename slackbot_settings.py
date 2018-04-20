import os

API_TOKEN=os.environ['SLACK_API_TOKEN']
DEFAULT_REPLY="Sorry, I don't understand that"
ERRORS_TO="ironriders-bot"
PLUGINS=[ "plugins.welcome" ]