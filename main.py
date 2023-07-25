import discord
from discord.ext import commands
import requests
import os
import time
import mysql.connector
import asyncio
import lxml
from config import token_discord
from bs4 import BeautifulSoup

url = 'https://ifconfig.co/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='l-box')
for quote in quotes:
  print(quote)
  


host = 'db4.myarena.ru'
database = 'u35192_devitka'
user = 'u35192_devitka'
password = '123456qwe'
global mydb
try:
    mydb = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password


    )

    if mydb.is_connected():
        print('Успешное подключение к базе данных MySQL')

except mysql.connector.Error as error:
    print('Ошибка при подключении к базе данных MySQL:', error)
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
print('start')

@bot.event
async def on_ready():
  print('Запустился')
  bot.loop.create_task(send_message())
  #bot.loop.create_task(on_message())
  #mydb = mysql.connector.connect(
     #   host=host,
      #  database=database,
       # user=user,
        #password=password)
  #if mydb.is_connected():
     #   print('Успешное подключение к базе данных MySQL')
async def on_message():
        channel = bot.get_channel(1132323086167978025)
        embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await channel.send(embed=embedVar)
        
async def send_message():
      channel = bot.get_channel(1133039161453064375)
      mycursor = mydb.cursor()
      mycursor.execute("SELECT * FROM log_game ORDER BY Date DESC LIMIT 50")
      myresult = mycursor.fetchall()
      await channel.send(myresult[4])
          #await asyncio.sleep(15)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1132323086167978025)
    embed = discord.Embed(
        title="Новый участник!",
        description=f"{member.name}",
        color=0xFF0000
    )
    await channel.send(embed=embed)

      
@bot.command()
async def statics(member):
    print('hello')


print('Запустил')
bot.run(f'{token_discord}')
