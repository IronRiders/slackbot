from datetime import datetime, timedelta
from pytz import timezone
from tzlocal import get_localzone
from slackbot import settings
from slackbot.bot import respond_to, listen_to
from pprint import pprint

import math, time, logging, slacker, json

logger = logging.getLogger(__name__)
slack = slacker.Slacker(settings.API_TOKEN)

@listen_to("has joined the group")
@listen_to("has joined the channel")
def groupJoined(message):
    logger.debug(pprint(vars(message)))

    user = message.body['user']
    channel_id = message.body['channel']

    logger.info("{} has joined {}. PM'ing rules".format(user, channel_id))
    channel = channel_id.encode('utf-8')
    response = slack.channels.info(channel) \
               if (channel.startswith(b"C")) \
               else slack.groups.info(channel)

    channel = response.body.get("channel" if channel.startswith(b"C") else "group")
    purpose = channel.get('purpose').get('value').encode('utf-8')
    pins = slack.pins.list(channel.get('id')).body.get('items')

    str = "Hi <@{}>! Welcome to *{}*!".format(message.body['user_profile']['name'] if 'user_profile' in message.body else "", channel.get('name'))
    str = "{}\n\nThe purpose of this channel is:\n> {}\nPlease keep that in mind when posting to the channel.".format(str, purpose.decode('utf-8')) if purpose is not None else str

    logger.debug(pins)
    if pins:

        str = "{}\n\nPins are oftentimes messages that contain extremely useful information for members of the channel. The following items have been 'pinned' to the channel:\n".format(str)

        for pin in pins:
            if pin.get('type') == u'message':
                str = "{}- {}\n".format(str, pin.get('message').get('text'))
            elif pin.get('type') == u'file':
                str = "{}- {}\n".format(str, pin.get('file').get('permalink'))

            else:
                logger.warn("Cannot handle pin type {}".format(pin.get('type')))
                logger.warn(pin)

    logger.debug(str)
    dm = message._client.webapi.im.open(message._body['user']).body['channel']['id']
    message._client.send_message(dm, str)

    return

@listen_to("has left the group")
@listen_to("has left the channel")
def groupLeft(message):
    logger.debug(message)
    logger.info("{} has left {}.".format(message._body['user_profile']['name'], message._body['channel']))
    return