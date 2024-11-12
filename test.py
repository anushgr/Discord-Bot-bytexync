import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True  # Required to access message content
bot = commands.Bot(command_prefix="!", intents=intents)

# Event to confirm bot is running
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

# Calculator command
@bot.command(name="calcy")
async def calculate(ctx, expression: str):
    try:
        result = eval(expression)  # Warning: eval can be unsafe
        await ctx.send(f"Result: {result}")
    except Exception as e:
        await ctx.send(f"Error: {e}")

# About us command
@bot.command(name="about")
async def about_us(ctx):
    await ctx.send("Bytexync Bot - Your Utility Companion! Created for various server utilities.")

# Help command
@bot.command(name="helo")
async def help_command(ctx):
    commands_list = """
    **Bytexync Utility Bot Commands:**
    - !about: Information about the bot.
    - !help: Display this help message.
    - !timeout <user> <seconds>: Timeout a user temporarily.
    - !roles: Show available roles.
    - !socials: Show social links.
    - !updates: Show recent updates.
    - !calcy <expression>: Perform calculations.
    - !strictmode <on/off>: Enable or disable strict mode.
    """
    await ctx.send(commands_list)

# Timeout command
@bot.command(name="timeout")
@has_permissions(manage_messages=True)
async def timeout_user(ctx, member: discord.Member, seconds: int):
    try:
        await member.timeout_for(discord.utils.timedelta(seconds=seconds))
        await ctx.send(f"{member.mention} has been timed out for {seconds} seconds.")
    except Exception as e:
        await ctx.send(f"Failed to timeout {member.mention}: {e}")

# User roles command
@bot.command(name="roles")
async def show_roles(ctx):
    roles = "\n".join([role.name for role in ctx.guild.roles if role != ctx.guild.default_role])
    await ctx.send(f"Available roles in this server:\n{roles}")

# Social links command
@bot.command(name="socials")
async def social_links(ctx):
    socials = """
    **Follow us on:**
    - Instagram: "https://www.instagram.com/bytexync"
    """
    await ctx.send(socials)

# Updates command
@bot.command(name="updates")
async def updates(ctx):
    await ctx.send("**Recent Updates:**\n- New commands added!\n- Bot stability improvements.")


# Strict mode command
strict_mode_enabled = False

@bot.command(name="strictmode")
async def strict_mode(ctx, mode: str):
    global strict_mode_enabled
    if mode.lower() == "on":
        strict_mode_enabled = True
        await ctx.send("Strict mode enabled.")
    elif mode.lower() == "off":
        strict_mode_enabled = False
        await ctx.send("Strict mode disabled.")
    else:
        await ctx.send("Invalid option. Use `!strictmode on` or `!strictmode off`.")

# Run the bot
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True  # Required to access message content
bot = commands.Bot(command_prefix="!", intents=intents)

# Event to confirm bot is running
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

# Calculator command
@bot.command(name="calcy")
async def calculate(ctx, expression: str):
    try:
        result = eval(expression)  # Warning: eval can be unsafe
        await ctx.send(f"Result: {result}")
    except Exception as e:
        await ctx.send(f"Error: {e}")

# About us command
@bot.command(name="about")
async def about_us(ctx):
    await ctx.send("Bytexync Bot - Your Utility Companion! Created for various server utilities.")

# Help command
@bot.command(name="helo")
async def help_command(ctx):
    commands_list = """
    **Bytexync Utility Bot Commands:**
    - !calcy <expression>: Perform calculations.
    - !about: Information about the bot.
    - !helo: Display this help message.
    - !timeout <user> <seconds>: Timeout a user temporarily.
    - !roles: Show available roles.
    - !socials: Show social links.
    - !updates: Show recent updates.
    - !invite: Get the bot invite link.
    - !strictmode <on/off>: Enable or disable strict mode.
    """
    await ctx.send(commands_list)

# Timeout command
@bot.command(name="timeout")
@has_permissions(manage_messages=True)
async def timeout_user(ctx, member: discord.Member, seconds: int):
    try:
        await member.timeout_for(discord.utils.timedelta(seconds=seconds))
        await ctx.send(f"{member.mention} has been timed out for {seconds} seconds.")
    except Exception as e:
        await ctx.send(f"Failed to timeout {member.mention}: {e}")

# User roles command
@bot.command(name="roles")
async def show_roles(ctx):
    roles = "\n".join([role.name for role in ctx.guild.roles if role != ctx.guild.default_role])
    await ctx.send(f"Available roles in this server:\n{roles}")

# Social links command
@bot.command(name="socials")
async def social_links(ctx):
    socials = """
    **Follow us on:**
    - Twitter: [twitter link]
    - Instagram: [instagram link]
    - GitHub: [github link]
    """
    await ctx.send(socials)

# Updates command
@bot.command(name="updates")
async def updates(ctx):
    await ctx.send("**Recent Updates:**\n- New commands added!\n- Bot stability improvements.")

# Invite link command
@bot.command(name="invite")
async def invite(ctx):
    invite_link = f"https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8"
    await ctx.send(f"Invite Bytexync to your server: {invite_link}")

# Strict mode command
strict_mode_enabled = False

@bot.command(name="strictmode")
async def strict_mode(ctx, mode: str):
    global strict_mode_enabled
    if mode.lower() == "on":
        strict_mode_enabled = True
        await ctx.send("Strict mode enabled.")
    elif mode.lower() == "off":
        strict_mode_enabled = False
        await ctx.send("Strict mode disabled.")
    else:
        await ctx.send("Invalid option. Use `!strictmode on` or `!strictmode off`.")

# Run the bot
bot.run("") #enter your bot token and run the file
