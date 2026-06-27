import discord
import random
# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

def gen_pass (pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
    


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "cara"
    else:
        return "coroa"


def bye():
    bye = ["bye!", "See you later!", "Bye! Have a great day!"]
    return random.choice(bye)

def hello():
    hello = ["Hi! What your need?", "Hello!", "Hey!", "Hi!"]
    return random.choice(hello)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(hello())
    elif message.content.startswith('$bye'):
        await message.channel.send(bye())
    elif message.content.startswith('$genpass'):
        senha = gen_pass(10)
        await message.channel.send(senha)
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    else:
        await message.channel.send(message.content)

client.run("MTUyMDIzNDI1NTQzMzYwMTAzNA.GtYQtj.lnv_TszRzRsDfvscNZBn71BD6KGj5ezvmh8SWQ")
