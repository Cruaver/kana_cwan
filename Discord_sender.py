import datetime
import discord
import asyncio
import random
import datetime

client = discord.Client()
minute = str(datetime.datetime.now().minute)
timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d")) + " " + str(datetime.datetime.now().hour + 2) + ":" + \
            minute


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
    if message.author == "156939319917936640":
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
                                      "/5BDC9FCF/t51.2885-19/s320x320/26065436_154405111872446_8536586386604556288_n"
                                      ".jpg")

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
                                  description="Tous les membres, y compris le Staff, se doivent de respecter le "
                                              "règlement "
                                              "sous peine de sanctions.\n\n Il est donc impératif de le lire afin de "
                                              "maintenir une bonne ambiance dans le serveur et permettre à tous de "
                                              "passer "
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
                                      "/5BDC9FCF/t51.2885-19/s320x320/26065436_154405111872446_8536586386604556288_n"
                                      ".jpg")

            embed.add_field(name="règles 1",
                            value="Le respect mutuel est impératif pour un bon fonctionnement en communauté. Ainsi, "
                                  "__**provocation, harcèlement et usurpation d'identité**__ sont totalement "
                                  "__**prohibées**__. Il s'agit d'un **acte grave**.",
                            inline=True)
            embed.add_field(name="règles 2", value="Il vous est demandé de __**respecter les fonctions des "
                                                   "channels**__.",
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
                            value="Nous avons eu les résultats des changements des salons comme vous pouvez le voir, "
                                  "nous remarquons que le nouveau système a eu un petit impact sur les salons vocaux, "
                                  "cela est dû a la participation des membres du serveur, nous les remercions "
                                  "fortement, "
                                  "qu’ils continuent ainsi.",
                            inline=True)
            embed.add_field(name=":tada: __Les Nouveaux Du Staff__ :",
                            value="Nous avons introduit dans notre discord 2 nouvelles personnes donc : **Kana Chan** "
                                  "qui "
                                  "est **PRÉFETS** , nous espérons qu’il saura faire ce rôle comme il se doit.\n\n"
                                  "**Pleym** qui est **GRAPHS / MONTEURS**, avec ses talents incroyables,"
                                  " nous espérons qu’il saura combler vos souhaits pour nos streamer adorés :relaxed:"
                                  "\n\n**Skaeren** qui était déjà **ADMINISTRATEURS** dans notre discord, "
                                  "revient parmi nous, il est maintenant "
                                  "rétrogradé **MODERATEURS**, espérant qu’il redeviendra **ADMINISTRATEURS**",
                            inline=True)
            embed.add_field(name=":gear: __Les Changement Du Staff__ :",
                            value="**Skygorter41** : Monté en **ADMINISTRATEURS** \n**Sei** : Monté en **CHEF "
                                  "MODERATEUR**\n**Dala** : Rétrogradé en **MODERATEURS**")

            embed.add_field(name=":Zwin_NANI: __Les Changement Du Staff__ :",
                            value="Nous espérons qu’ils sauront accomplir leur devoir.  Voilà c’est tout "
                                  "pour ce débriefing, désolé si j’ai raté quelque chose ( Ah oui, nous avons chanté, "
                                  "**Skygorter41**, **Pleym**, **Sei** et **Kana Chan**, nous attendons que **Zwin** "
                                  "nous envoie la vidéo ). A la prochaine réunion pour le débriefing. "
                                  "Passez une agréable journée / soirée.")

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
