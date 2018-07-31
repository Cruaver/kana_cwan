import datetime
import discord
import asyncio
import random
import datetime

client = discord.Client()
timestamp = datetime.datetime.now().strftime("%Y-%m-%d") + " " + str(datetime.datetime.now().hour + 2) + ":" + str(
    datetime.datetime.now())


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id='469090469960351767')
    while not client.is_closed:
        counter += 1
        await client.send_message(channel, "No fake")
        await asyncio.sleep(5)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!tmz_rendu'):
        embed = discord.Embed(colour=discord.Colour(0xff0000),
                              url="https://discordapp.com/oauth2/authorize?client_id=469088879207514132&scope=bot",
                              description="Compte-rendu de la réunion du 10/06/2018\n\n")

        embed.set_thumbnail(
            url="https://scontent-ams3-1.cdninstagram.com/vp/8ec180462bdc5f880ae2f908b43b0ccf/5BDC9FCF/t51.2885-19"
                "/s320x320/26065436_154405111872446_8536586386604556288_n.jpg")
        embed.set_author(name="Honoka",
                         url="https://discordapp.com/oauth2/authorize?client_id=469088879207514132&scope=bot",
                         icon_url="https://cdn.discordapp.com/avatars/222139815980695552"
                                  "/ecb5a324d354fcfe92ba3e2ae99b32df.png?size=2048")
        embed.set_footer(text=timestamp,
                         icon_url="https://scontent-ams3-1.cdninstagram.com/vp/8ec180462bdc5f880ae2f908b43b0ccf"
                                  "/5BDC9FCF/t51.2885-19/s320x320/26065436_154405111872446_8536586386604556288_n.jpg")

        embed.add_field(name=":calendar: __Bilan de la semaine__ :",
                        value="- La communauté n'est pas très active en ce moment en raison des révisions et des "
                              "examens\n\n- Recrutement de 2 nouveaux membres du Staff : @Izumi et @Amon🔮 en "
                              "@🎲Animation🎲\n\n- Les serveurs annexes n’impacteront en aucun cas l’avenir de "
                              "TMZ\n\n")
        embed.add_field(name="\n:tada: __Animation__ :",
                        value="- Les examens seront pris en compte dans l'organisation des événements\n\n- De "
                              "nouveaux événements feront leur apparition dans les semaines à venir\n\n- Pas de "
                              "Responsable Animation pour le moment\n\n")

        await client.send_message(message.channel, content="**Compte-rendu**", embed=embed)

    elif message.content.startswith('!tmz'):
        embed = discord.Embed(title="Les règles", colour=discord.Colour(0xff0000),
                              url="https://discordapp.com/oauth2/authorize?client_id=469088879207514132&scope=bot",
                              description="Tous les membres, y compris le Staff, se doivent de respecter le règlement "
                                          "sous peine de sanctions.\n\n Il est donc impératif de le lire afin de "
                                          "maintenir une bonne ambiance dans le serveur et permettre à tous de passer "
                                          "un bon moment en notre compagnie. Nous vous informons que le Staff en "
                                          "charge de la @Gestion se réfère toujours au règlement avant de mettre "
                                          "quelque sanction que ce soit.")

        embed.set_thumbnail(
            url="https://scontent-ams3-1.cdninstagram.com/vp/8ec180462bdc5f880ae2f908b43b0ccf/5BDC9FCF/t51.2885-19"
                "/s320x320/26065436_154405111872446_8536586386604556288_n.jpg")
        embed.set_author(name="Honoka",
                         url="https://discordapp.com/oauth2/authorize?client_id=469088879207514132&scope=bot",
                         icon_url="https://cdn.discordapp.com/avatars/222139815980695552"
                                  "/ecb5a324d354fcfe92ba3e2ae99b32df.png?size=2048")
        embed.set_footer(text=timestamp,
                         icon_url="https://scontent-ams3-1.cdninstagram.com/vp/8ec180462bdc5f880ae2f908b43b0ccf"
                                  "/5BDC9FCF/t51.2885-19/s320x320/26065436_154405111872446_8536586386604556288_n.jpg")

        embed.add_field(name="règles 1",
                        value="Le respect mutuel est impératif pour un bon fonctionnement en communauté. Ainsi, "
                              "__**provocation, harcèlement et usurpation d'identité**__ sont totalement "
                              "__**prohibées**__. Il s'agit d'un **acte grave**.",
                        inline=True)
        embed.add_field(name="règles 2", value="Il vous est demandé de __**respecter les fonctions des channels**__.",
                        inline=True)

        await client.send_message(message.channel, content="**RÈGLEMENT**", embed=embed)

    elif message.content.startswith('!GR_Rendu'):
        embed = discord.Embed(colour=discord.Colour(0xff0000),
                              url="https://discordapp.com/oauth2/authorize?client_id=469088879207514132&scope=bot",
                              description="__**Compte rendu de la réunion du 29/07/2018**__")

        embed.set_thumbnail(
            url="https://cdn.discordapp.com/icons/289845545151889408/25a4223c378f0bea5ff1c743af739e14.png")
        embed.set_author(name="Skygorter41",
                         url="https://discordapp.com/oauth2/authorize?client_id=469088879207514132&scope=bot",
                         icon_url="https://cdn.discordapp.com/avatars/244807977373138956"
                                  "/df627cfadbc07dcc72c85ee83ff69a78.png?size=2048")
        embed.set_footer(text=timestamp,
                         icon_url="https://cdn.discordapp.com/icons/289845545151889408"
                                  "/25a4223c378f0bea5ff1c743af739e14.png")

        embed.add_field(name=":calendar: __Bilan de la semaine__ :",
                        value="Nous avons eux les résultats des changements des salons comme vous pouvez le voir, "
                              "nous remarquons que les nouveau système des salons a eux un petit impacte sur les "
                              "salons vocal, cela est du grave au nouveau système, et de la participation des membres "
                              "du serveur, nous les remercions fortement, qu’il continue ainsi. ",
                        inline=True)
        embed.add_field(name=":tada: __Les Nouveau Du Staff__ :",
                        value="Nous avons introduit dans nôtres discord 2nouvelle personne dont : @🌺💖Kana "
                              "Chan💖🌺#7440 qui est @👋 PRÉFETS 👋 , nous espérons qu’il sera faire ce rôle comme il "
                              "se doit.\n\n@Pleym#2213 qui est @🖌🎨 GRAPHS / MONTEURS 🎨🖌 , avec ces talents "
                              "incroyable nous espérons qu’il sera combler vos souhait pour nos streamer adorés "
                              ":relaxed:\n\n@Skaeren#4624 qui était déjà @📙 ADMINISTRATEURS 📙  dans notre discord, "
                              "mais pour des raisons il à quitter, et il revient parmi nous, il est maintenant "
                              "rétrogradé @🔧 MODERATEURS 🔧 , espérant qu’il redeviendra ce qu’il était avant.",
                        inline=True)
        embed.add_field(name=":gear: __Les Changement Du Staff__ :",
                        value="@Skygorter41#1152 : Monté en @📙 ADMINISTRATEURS 📙 \n@Sei#8698 : Monté en @🔧 CHEF "
                              "MODERATEUR 🔧\n@Ikumi#0562 : Rétrogradé en @🔧 MODERATEURS 🔧")
        embed.add_field(name=":Zwin_NANI: __Les Changement Du Staff__ :",
                        value="Nous espérons qu’il seront accomplir leur devoir qui a était donné. Voilà c’est tout "
                              "pour ce débriefing, désoler si j’ai rater quelque chose ( Ah oui, nous avons chanter, "
                              "@Skygorter41#1152 et @Pleym#2213 et @Sei#8698 et @🌺💖Kana Chan💖🌺#7440, "
                              "nous attendons que @Zwin#7322 nous envoie la vidéo )A la prochaine réunion pour le "
                              "prochain débriefing, sur ceux passer une agréable journée / soirée, et je vous "
                              "souhaite d’agréer mes salutation distingués")
        await client.send_message(message.channel, content="**Compte-rendu**", embed=embed)

    if message.content.startswith('!hug'):
        embed = discord.Embed(title="Love", colour=discord.Colour(0xff0000), url="https://discordapp.com",
                              description="HUG", timestamp=datetime.datetime.utcfromtimestamp(1531914637))

        embed.set_image(url="https://media.tenor.com/images/8efd27e0de55465601ce4fa7dc1423ed/raw")
        embed.set_author(name="Kana Chan")

        embed.add_field(name="Un Calins",
                        value="-------------------------------------------------------------------------")

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!love'):
        embed = discord.Embed(colour=discord.Colour(0xff0000),
                              url="https://discordapp.com/oauth2/authorize?client_id=469088879207514132&scope=bot")

        embed.set_image(url="https://puu.sh/AYL7P/bbe229b0e9.png")
        embed.set_thumbnail(url="https://fr.seaicons.com/wp-content/uploads/2015/10/heart-icon2.png")
        embed.set_author(name="Kana Chan",
                         url="https://discordapp.com/oauth2/authorize?client_id=469088879207514132&scope=bot",
                         icon_url="https://cdn.discordapp.com/avatars/156939319917936640"
                                  "/f32bb6c7f9995b102ff6a8aa0f0fb762.png?size=2048")
        embed.set_footer(text="18 juillet 2018 à 14h32",
                         icon_url="https://fr.seaicons.com/wp-content/uploads/2015/10/heart-icon2.png")

        embed.add_field(name="Je t'aime",
                        value="Je commence à éprouver de réelle sentiment pour toi je t'aime sincèrement **rougie**")

        await client.send_message(message.channel, content="***Ma belle déclaration***", embed=embed)
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!digy'):
        msg = 'DIGY DIGY HOLLE'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!deleteme'):
        msg = await client.send_message(message.channel, 'I will delete myself now...')
        await client.delete_message(msg)

    if message.content.startswith('!editme'):
        msg = await client.send_message(message.author, '10')
        await asyncio.sleep(3)
        await client.edit_message(msg, '40')

    if message.content.startswith('!guess'):
        await client.send_message(message.channel, 'devine un nombre entre 1 et 10')

        def guess_check(m):
            return m.content.isdigit()

        guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'trop longggggg tes nullll {}.'
            await client.send_message(message.channel, fmt.format(answer))
            return
        if int(guess.content) == answer:
            await client.send_message(message.channel, 'Bravo !')
        else:
            await client.send_message(message.channel, 'Nan Bouh tes nulll s\'etais {}.'.format(answer))


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


# client.loop.create_task(my_background_task())
client.run('NDY5MDg4ODc5MjA3NTE0MTMy.DjCpCQ.4GszIlCfFH7T5WTeCzxeyOYG9lY')
