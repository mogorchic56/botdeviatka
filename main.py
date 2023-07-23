import disnake
import requests
import time
from disnake.ext import commands
import mysql.connector
req = requests.get('https://ifconfig.co/')

print(req)


bot = commands.Bot(command_prefix="!", help_command = None,intents=disnake.Intents.all())
print('start')


host = 'db4.myarena.ru'
database = 'u35192_devitka'
user = 'u35192_devitka'
password = '123456qwe'

try:
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password


    )

    if connection.is_connected():
        print('Успешное подключение к базе данных MySQL')

except mysql.connector.Error as error:
    print('Ошибка при подключении к базе данных MySQL:', error)
@bot.event
async def on_ready():
  while True:
    time.sleep(3)
    req = requests.get('https://api.battlemetrics.com/servers/17389558')
    task = req.json()
    data = task.get('data')
    count = data.get('attributes')
    name = count.get('name')
    players = count.get('players')
    maxPlayers = count.get('maxPlayers')
    status = count.get('status')
    print(f'{name}: {players}/{maxPlayers}.\n {status}')
    if status == 'online':
      activity = disnake.Activity(
          name = f"🟢 {players}/{maxPlayers}",
          type = disnake.ActivityType.watching,
      )
      await bot.change_presence(activity=activity)
    else:
        activity = disnake.Activity(
          name = "🔴 Сервер выключен",
          type = disnake.ActivityType.watching,
        )
        await bot.change_presence(activity=activity)
    print(f"Bot {bot.user} is ready to work!")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1128186670521516124)
    embed = disnake.Embed(
        title="Новый участник!",
        description=f"{member.name}",
        color=0xFF0000
    )
    await channel.send(embed=embed)
  



@bot.command()
async def statics(member):
    print(help)
    channel = bot.get_channel(1128186670521516124)
    monitoring = disnake.Embed(
    title = on_ready.name,
    description=f"{on_ready.players}/{on_ready.maxPlayers}",
    color=0xFF0000
    )
    await channel.send(embed=monitoring)
print('Запустил')
bot.run("MTEzMTU4NzczNDIwOTg0MzI1MA.GQenn8.RzdiICTDVXg-mbkyY1zn85naUDReJO25YH0MbI")
from replit import db
