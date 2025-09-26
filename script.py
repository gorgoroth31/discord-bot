import discord
import random
import time

class Balance():
    balance = []

class MyClient(discord.Client, Balance):

#Einloggen
    async def on_ready(self):
        print("Login finished")

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):

        if message.author == client.user:
            return

        elif message.content.startswith("hello bot"):
            await message.channel.send("Hello!")
          
        elif message.content == "$help" or message.content == "$help ":
            await message.channel.send("Alle Befehle:\n$roulette\n$joke\n$info\n$dice\n$coin\n$balance")

        elif message.content.startswith('$help'):
            help_key = message.content.split(' ')[1]

            if help_key == "help":
                await message.channel.send("Du Trickster")

            elif help_key == "roulette":
                await message.channel.send("Mit $roulette kannst du entweder auf schwarz oder rot setzen(Coin-system ist in Arbeit)")

            elif help_key == "joke":
                await message.channel.send("Mit $joke kannst du dir einen kostenlosen Witz generieren lassen!!")

            elif help_key == "info":
                await message.channel.send("Mit $info bekommst einen Link über technische Infos über den Bot\n<Nur für Nerds>")

            elif help_key == "dice":
                await message.channel.send("Gibt eine zufällige Zahl zwischen 1 und 6 aus")

            elif help_key == "coin":
                await message.channel.send("Wirft eine Münze")

            elif help_key == "balance":
                await message.channel.send("Zeigt dein Guthaben an(In Arbeit)")

#Roulette
        elif message.content.startswith("$roulette"):

            bid = message.content.split('')[1]
            bid_param = -3

            if bid.lower() == "schwarz":
                bid_param = -1
            elif bid.lower() == "rot":
                bid_param = -2

            else:
                try:
                    bid_param == int(bid)
                except:
                    bid_param = -3
            if bid_param == -3:
                await message.channel.send("Ungültige Eingabe")
                return
            result = random.randint(0, 36)

            if result %2 == 0:
                color = "schwarz"

            elif result %2 == 1:
                color = "rot"

            if bid_param == -1:
                won = result%2 == 0 and not result == 0

            elif bid_param == -2:
                won = result%2 == 1

            else:
                won = result == bid_param

            if won:
                await message.channel.send("$$$ Du hast gewonnen $$$")
                await message.channel.send("Die Nummer war " + str(result) + " und somit " + str(color))
                #balance(message.author) = balance(message.author) +50
            else:
                await message.channel.send("Leider verloren pog")
                await message.channel.send("Die Nummer war " + str(result) + " und somit " + str(color))
                #balance(message.author) = balance(message.author) + 50

#Jokes

#Hier muss immer erweitert werden, wenn neue Witze dazukommen

        elif message.content == "$joke" or message.content == "$jokes":
            zahl = random.randint(1, 13)

            while True:
                if zahl % 2 == 1:
                    break
                else:
                    zahl = random.randint(1, 21)

            jokes = [" ", "Warum sollte man nie Cola und Bier gleichzeitig trinken?", "Weil man sonst colabiert",
                     "Was essen Autos am liebsten?", "Parkplätzchen",
                     "Wer wohnt im Dschungel und schummelt immer?", "Mogli",
                     "Wieso können Skelette schlecht lügen?", "Weil sie so gut zu durchschauen sind",
                     "Was sagt der große Stift zum kleinen Stift?", "Wachs-mal-Stift",
                     "Wie war die Stimmung in der DDR?", "Sie hielt sich in Grenzen",
                     "You have encountered the secret joke and you WILL laugh", "penis",
                     "Was ist grün und steht vor der Tür?", "Ein Klopfsalat",
                     "Was ist rot und schlecht für die Zähne?", "Ein Ziegelstein",
                     "Was machen zwei wütende Schafe?", "Sie kriegen sich in die Wolle",
                     "Gute Nachricht: Ich bekomme endlich den obersten Knopf meiner superengen Jeans zu","Schlechte Nachricht: Habe sie leider nicht an"
                     ]

            emoji_rand = random.randint(1, 8)
            emojis = ["", ":grin:", ":laughing:", ":joy:",":rofl:", ":stuck_out_tongue_closed_eyes:",
                      ":stuck_out_tongue_winking_eye:", ":zany_face:", ":PogChamp:"]
            await message.channel.send(jokes[zahl])
            time.sleep(3)
            await message.channel.send(jokes[zahl + 1] + " " + emojis[emoji_rand])

        elif message.content == "$info":
            await message.channel.send("Hier, du Nerd:\nwww.imgur.com/a/G6rU8")

        elif message.content == "$dice":
            dice = random.randint(1,6)
            await message.channel.send(dice)

        elif message.content == "$coin":
            coin = random.randint(1,2)
            if coin == 1:
                await message.channel.send("Kopf")
            elif coin == 2:
                await message.channel.send("Zahl")

        elif message.content == "$balance":
            await message.channel.send("Ist in Arbeit. Hab Geduld :D")
            #await message.author.send(balance(message.author))

        elif message.content == "SeniorBot Go":
            members = message.guild.members
            members = [i for i in members if not i.bot]
            print(members)

    # loggt, welcher nutzer gerade am tippen ist, deaktiviert weil nervig
    async def on_typing(self,channel, user, when):
        return
        #print(str(user) + " tippt gerade in " + str(channel) + " seit " + str(when))

    async def on_message_delete(self, message):
        print("Gelöschte Nachricht " + str(message.content) + " von " + str(message.author))


    async def on_message_edit(self, before, after):
        print("Changed messange " + before.content + " to " + after.content)


client = MyClient()
client.run("$env.clientkey")
