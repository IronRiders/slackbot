# IronRiders/slackbot

The Slack bot of FRC Team 4180: The Iron Riders

[![Build Status](https://travis-ci.org/IronRiders/slackbot.svg?branch=master)](https://travis-ci.org/IronRiders/slackbot)

# Set up

After cloning the repository, install the depedencies via run `pip3 install -r requirements`

To run the bot, use `python3 ./run.py`

You will need to have an environment variable named `SLACK_API_TOKEN` in order to run the bot. Ask in the #ironriders-bot channel for it.

# Creating new behaviors

The bot's behavior is defined by _plugins_. Plugins are simple python files that with function thats are called something happens. Plugin functions can both passively _listen_ for something, or actively _respond_ to a command.

See the [welcome plugin](https://github.com/IronRiders/slackbot/blob/master/plugins/welcome.py) for a reference implementation of passively listening.

When creating a new plugin file, you must also register it by assing it to the `PLUGINS` list in [slackbot_settings.py](https://github.com/IronRiders/slackbot/blob/master/slackbot_settings.py)
