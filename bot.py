import discord
from discord.ext import commands
import random

# Set up bot with command prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Command to allow users to register their skills
user_skills = {}

@bot.command(name='register')
async def register(ctx, *, skills):
    """Register your skills and interests."""
    user_skills[ctx.author] = skills
    await ctx.send(f"{ctx.author.mention} registered with skills: {skills}")

# Command to match users based on skills
@bot.command(name='match')
async def match(ctx):
    """Find a match for networking or mentorship."""
    if ctx.author not in user_skills:
        await ctx.send("You need to register your skills first using !register.")
        return
    
    # Randomly match with another registered user
    potential_matches = [user for user in user_skills if user != ctx.author]
    if potential_matches:
        match_user = random.choice(potential_matches)
        await ctx.send(f"{ctx.author.mention}, you have been matched with {match_user.mention} for networking!")
    else:
        await ctx.send("No other users available for matching at the moment.")

# Command to set up virtual rooms
@bot.command(name='create_room')
async def create_room(ctx, room_name: str):
    """Create a virtual room for collaboration."""
    guild = ctx.guild
    category = discord.utils.get(guild.categories, name="Virtual Rooms")
    if not category:
        category = await guild.create_category("Virtual Rooms")
    room = await guild.create_text_channel(room_name, category=category)
    await ctx.send(f"Room '{room_name}' created successfully!")

# Command to organize a group challenge
@bot.command(name='challenge')
async def challenge(ctx):
    """Start a group challenge."""
    challenges = [
        "Complete a virtual coffee chat with three new people.",
        "Collaborate on a short project within this week.",
        "Share productivity tips in the room daily."
    ]
    challenge = random.choice(challenges)
    await ctx.send(f"New Challenge: {challenge}")

# Run the bot
bot.run('MTMwNjEyMzM2ODIzNTUzMjM3MQ.GfYfMM.LWUCc56CbNJ7YOK3dmQU-TjYY_2Wze3O_lYnB4')