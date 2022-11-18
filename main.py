import discord
import json
from discord.ext import commands
import os

file = open('config.json', 'r')
config = json.load(file)

bot = commands.Bot(config['prefix'], intents=discord.Intents.all())


# Действия по активации бота
@bot.event
async def on_ready():
    print('BOT ONLINE')
    # channel = bot.get_channel(1033010362913652892)
    # await channel.send("https://www.youtube.com/watch?v=CYrvm-tryHM")


# Отправка гифок
@bot.command(name='gif')
async def gif(ctx, gif_name='dolb'):
    await ctx.channel.purge(limit=1)
    file = f'gifs/{gif_name}.gif'
    if os.path.exists(file):
        await ctx.send(file=discord.File(os.path.abspath(file)))
        await ctx.send(embed=discord.Embed(description=f'{gif_name} *by **{ctx.author.display_name}***', color=0x249c44))
    else:
        files = (' | '.join(os.listdir('gifs'))).replace('.gif', '')
        text = f'{gif_name} ? Такой гифки нет, братан. Вот весь список:\n{files}'
        await ctx.send(embed=discord.Embed(description=text, color=0xd1bd28))


# Анекдоты
anek_num = -1
anek_file = open('files/anekdots', 'r')
anek_arr = ['']
anek_count = 1
for line in anek_file:
    if line == '\n':
        anek_arr.append('')
        anek_count += 1
    else:
        anek_arr[anek_count - 1] += line
anek_count
@bot.command(name='anek')
async def anek(ctx, num=''):
    global anek_num
    try:
        num = (int(num))
        if 1 <= num <= anek_count:
            anek_num = num - 1
        else:
            anek_num = (anek_num + 1) % anek_count
    except:
        anek_num = (anek_num + 1) % anek_count
    text = f'*Упаковщица № * {anek_num + 1}\n\n' + anek_arr[anek_num]
    await ctx.send(embed=discord.Embed(description=text, color=0x8e4cd4))


bot.remove_command('help')



bot.run(config['token'])
