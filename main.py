import disnake
from disnake.ext import commands
from parser import name, players, maxPlayers, status

activity = disnake.Activity(
    name=f"{players}/{maxPlayers}",
    type=disnake.ActivityType.watching,
)

bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all(), activity=activity)


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
        color=0xFF0000
    )

    await member.add_roles(role)
    await channel.send(embed=embed)





@bot.command()
async def statics(member):
    channel = bot.get_channel(1128186670521516124)
    monitoring = disnake.Embed(
    title = name,
    description=f"{players}/{maxPlayers}",
    color=0xFF0000
    )
    await channel.send(embed=monitoring)


bot.run("MTEzMTU4NzczNDIwOTg0MzI1MA.GGeP_q.3X4e4Cf1p4PNUO7fGo3y6qICTEq2U0Vki3Q10U")