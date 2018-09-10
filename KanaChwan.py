import discord
import asyncio
import datetime

client = discord.Client()
prefix = "!kana "
minute = str(datetime.datetime.now().minute)
timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d")) + " " + str(datetime.datetime.now().hour + 2) + ":" + \
            minute


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# async def my_background_task():
#     await client.wait_until_ready()
#     counter = 0
#     channel = discord.Object(id='469090469960351767')
#     while not client.is_closed:
#         counter += 1
#         await client.send_message(channel, "No fake")
#         await asyncio.sleep(5)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author == "156939319917936640":
        if message.content.startswith("{}ping".format(prefix)):
            embed = discord.Embed(colour=discord.Colour(0xff0000),
                                  url="https://discordapp.com/oauth2/authorize?client_id=469088879207514132&scope=bot",
                                  description="PONG !!!\n\n")
            await client.send_message(message.channel, content="**Commande Kana Chwan :**", embed=embed)


@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    channel = discord.Object(id='469090469960351767')
    await client.send_message(channel, fmt.format(member, server))


# @client.event
# async def on_message_delete(message):
#     if message.author == client.user:
#         return
#     else:
#         fmt = '{0.author.name} has deleted the message:\n{0.content}'
#         await client.send_message(message.channel, fmt.format(message))
#
#
# @client.event
# async def on_message_edit(before, after):
#     if before.author == client.user:
#         return
#     else:
#         fmt = '**{0.author}** edited their message:\n{1.content}'
#         await client.send_message(after.channel, fmt.format(after, before))

client.run('NDY5MDg4ODc5MjA3NTE0MTMy.DjCpCQ.4GszIlCfFH7T5WTeCzxeyOYG9lY')
