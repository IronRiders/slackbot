import tbapy
from slackbot.bot import respond_to

tba = tbapy.TBA('NRIotr26Z49TOHAI1H1VQtrZ9rXQOaApuia9oCr9pbwsWImjbDNYU4f3znFdlvea')

@respond_to("detail (\d+)")
def detail(message, number):
    team = tba.team(int(number))
    reply = "Team %s, %s, out of %s, %s %s. %s - Founded in %s." % (int(number), team.nickname, team.city, team.state_prov, team.country, team.website, team.rookie_year)
    message.reply(reply)
