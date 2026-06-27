import discord

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$genpass'):
        senha = gen_pass(10)
        await message.channel.send(senha)
    
    else:
        await message.channel.send(message.content)

client.run("MTUyMDIzNDI1NTQzMzYwMTAzNA.GpLX6R.LvubV12FNWSDY3q4vJFoSEHE0jgLI2L_qQXwuk")
