import logging, sys
from slackbot.bot import Bot

logger = logging.getLogger("slackbot")
logger.setLevel(logging.DEBUG)

stdout = logging.StreamHandler()
stdout.setLevel(logging.DEBUG)
stdout.setFormatter(logging.Formatter("%(asctime)s %(module)10s %(levelname)5s - %(message)s", "%Y-%m    -%d %H:%M:%S"))

logger.addHandler(stdout)

logger = logging.getLogger("plugins")
logger.setLevel(logging.DEBUG)

stdout = logging.StreamHandler()
stdout.setLevel(logging.DEBUG)
stdout.setFormatter(logging.Formatter("%(asctime)s %(module)10s %(levelname)5s - %(message)s", "%Y-%m    -%d %H:%M:%S"))

logger.addHandler(stdout)

def main():
    logger.info("Starting up...");
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()