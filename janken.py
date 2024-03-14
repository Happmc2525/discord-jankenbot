import discord
from discord import Option
import random
import time

TOKEN = 'ここにbotのトークンを入れる'
DISCORD_SERVER_IDS = ここにサーバーのidを入れる

client = discord.Bot(intents=discord.Intents.all())

@client.slash_command(name="janken", description="じゃんけんコマンド", guild_ids=[DISCORD_SERVER_IDS])
async def on_message(message: discord.Message):
    await message.respond("最初はグー、じゃんけん")

    draw = "あいこ(そのままもう一度入力)"
    wn = 'kati.png'
    lst = 'make.png'

    def jankencheck(m):
        return (m.author == message.author) and (m.content in ["グー", "チョキ", "パー"])

    while True:
        jbot = random.choice(("グー", "チョキ", "パー"))
        reply = await client.wait_for("message", check=jankencheck)
        if reply.content == jbot:
            jkekka = draw
            await message.channel.send(jbot)
            await message.channel.send(jkekka)
        else:
            if reply.content == "グー":
                if jbot == "チョキ":
                    jkekka = wn
                    await message.channel.send("チョキ")
                    break
                else:
                    jkekka = lst
                    await message.channel.send("パー")
                    break
            elif reply.content == "チョキ":
                if jbot == "パー":
                    jkekka = wn
                    await message.channel.send("パー")
                    break
                else:
                    jkekka = lst
                    await message.channel.send("グー")
                    break
            else:
                if jbot == "グー":
                    jkekka = wn
                    await message.channel.send("グー")
                    break
                else:
                    jkekka = lst
                    await message.channel.send("チョキ")
                    break
    await message.channel.send(file=discord.File(jkekka))

client.run(TOKEN)
