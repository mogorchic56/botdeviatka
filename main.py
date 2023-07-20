import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all())


@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")


@bot.event
async def on_member_join(member):
    role = member.guild.get_role(1128373004724863026)
    channel = bot.get_channel(1128186670521516124)

    embed = disnake.Embed(
        title="Новый участник!",
        description=f"{member.name}",
        color=0xffffff
    )

    await member.add_roles(role)
    await channel.send(embed=embed)





@bot.command()
async def statics(member):
    channel = bot.get_channel(1128186670521516124)
    monitoring = disnake.Embed(
    title="Новый участник!",
    description=f"member",
    color=0xffffff
    )
    await channel.send(embed=monitoring)


bot.run("MTEzMTU4NzczNDIwOTg0MzI1MA.GyoTts.hLOLP28Pb3yLTf1bjJGjiGatNlzNlwhtZOdlU4")