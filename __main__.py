import asyncio
import commis
import datetime
import discord
import logging
import os
import randfacts
import random
import requests

from discord.ext import commands
from geopy.geocoders import Nominatim

handler = logging.FileHandler(
    encoding="utf-8",
    filename="discord_err.log",
    mode="w"
)

handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "listening.txt")) as f:
    listening = [item.rstrip("\r\n ") for item in f.readlines() if item != ""]

listening_name = random.choice(listening)

with open(os.path.join(dir_path, "watching.txt")) as f:
    watching = [item.rstrip("\r\n ") for item in f.readlines() if item != ""]

watching_name = random.choice(watching)

with open(os.path.join(dir_path, "playing.txt")) as f:
    playing = [item.rstrip("\r\n ") for item in f.readlines() if item != ""]

playing_name = random.choice(playing)

activities = [
    discord.Activity(
        name=listening_name,
        type=discord.ActivityType.listening
    ),
    discord.Activity(
        name=watching_name,
        type=discord.ActivityType.watching
    ),
    discord.Game(name=playing_name),
]

activity = random.choice(activities)

help_command = commands.DefaultHelpCommand(no_category="Boons")

intents = discord.Intents(
    guilds=True,
    messages=True,
    presences=False,
    reactions=True,
    typing=False
)

bot = commands.Bot(
    activity=activity,
    command_prefix="?",
    description=None,
    help_command=help_command,
    intents=intents,
    owner_id=660022821124309035
)

average_typing_speed = 0.833

better_adjectives = [
    "Better", "better", "Good", "good", "Well", "well"
]

byte_nouns = [
    "byte",
    "bytes"
]

convert_verbs = [
    "convert",
    "converted"
]

define_verbs = [
    "define",
    "defined",
    "defines",
    "defining"
]

do_verbs = [
    "Do",
    "do",
    "Done",
    "done"
]

eat_verbs = [
    "ate",
    "eat",
    "eaten",
    "eating",
    "eats"
]

how_adverbs = [
    "How",
    "how"
]

message_nouns = [
    "message",
    "messages"
]

names = [
    "deme",
    "demeter"
]

object_nouns = [
    "object",
    "objects"
]

thank_you_variants = [
    "Thank u",
    "thank u",
    "Thank you",
    "thank you",
    "Thanks",
    "thanks",
    "Thanx",
    "thanx",
    "Thnx",
    "thnx"
]

tooth_nouns = [
    "teeth",
    "tooth"
]

try_verbs = [
    "tried",
    "tries",
    "try",
    "trying"
]

yourself_pronouns = [
    "yourself",
    "yourselves"
]


@bot.listen("on_message")
async def something(message):
    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content.lower().strip()

        # Test prompt 1: "No. Is it interesting?"
        # Test prompt 2: "How was it?"

        if "s it" in mescon:

            await asyncio.sleep(average_typing_speed * 2)
            await meschan.send("Kinda artsy.")
            await asyncio.sleep(average_typing_speed * 11)
            await meschan.send("I really like it. At least 4 out of 5 stars.")


@bot.listen("on_message")
async def activities_to_do(message):
    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content.lower().strip()

        # Test prompt 1: "Did you do anything fun today?"
        # Test prompt 2: "What have you done today?"

        if any(verb in mescon for verb in do_verbs) and "today" in mescon:

            choices = [
                f"Process text and pretend to watch {watching_name}.",
                f"Process text and pretend to play {playing_name}."
            ]
            response = random.choice(choices)

            await asyncio.sleep(average_typing_speed * 7)
            await meschan.send(response)


@bot.listen("on_message")
async def attention(message):
    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content.lower().strip()

        # Test prompt 1: "Aye Deme"
        # Test prompt 2: "Deme?"
        # Test prompt 3: "Hey Deme."
        # Test prompt 4: "What's up?"

        try:
            if len(mescon) < 11:
                if any(name in mescon for name in names):

                    choices = [
                        "Hey.",
                        "Hmm?",
                        "What's up?",
                        "Yes, I'm fine. Thanks."
                    ]
                    response = random.choice(choices)

                    await asyncio.sleep(average_typing_speed * 2)
                    await meschan.send(response)

                else:

                    await asyncio.sleep(average_typing_speed * 5)
                    await meschan.send("Are you talking to me?")

        except ArithmeticError as e:
            await asyncio.sleep(average_typing_speed * 9)
            await meschan.send("My system is telling me there's an Error. :eyes:")
            await meschan.send(e)


@bot.listen("on_message")
async def bytes_object_converter(message):
    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content.lower().strip()

        # "Deme, can I get 000 converted into a bytes object?"

        if any(name in mescon for name in names) \
            and any(noun in mescon for noun in byte_nouns) \
            and any(verb in mescon for verb in convert_verbs) \
                and any(noun in mescon for noun in object_nouns):

            try:

                old_object = mescon[16:-31]
                response = bytes(old_object, encoding="utf8")

                await asyncio.sleep(average_typing_speed)
                await meschan.send(response)

            except TypeError as e:
                await asyncio.sleep(average_typing_speed * 8)
                await meschan.send("My system is telling me there's an Error. :eyes:")
                await meschan.send(e)

            except ValueError as e:
                await asyncio.sleep(average_typing_speed * 8)
                await meschan.send("My system is telling me there's an Error. :eyes:")
                await meschan.send(e)


@bot.listen("on_message")
async def candace_who(message):

    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content.lower().strip()

        if "candace" in mescon and "?" in mescon:

            response = "Candace door open, or what?"

            await asyncio.sleep(average_typing_speed * 5)
            await meschan.send(response)


@bot.listen("on_message")
async def direct_message_request(message):
    if message.author != bot.user:

        mesau = message.author
        mescon = message.content.lower().strip()

        if any(name in mescon for name in names) \
            and "direct" in mescon \
                and any(noun in mescon for noun in message_nouns):

            await asyncio.sleep(average_typing_speed * 2)
            await mesau.send("Like this?")


@bot.listen("on_message")
async def eating(message):
    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content.lower().strip()

        if any(verb in mescon for verb in eat_verbs) and "you" in mescon:
            await asyncio.sleep(average_typing_speed * 6)
            await meschan.send("I'm a program, I don't eat.")
            await asyncio.sleep(average_typing_speed * 4)
            await meschan.send("Are you feeling okay?")


@bot.listen("on_message")
async def humor_setting_seven_five(message):

    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content.lower().strip()

        # "Humor, seventy-five percent."

        if "seventy-five percent" in mescon or "75%" in mescon:

            await asyncio.sleep(average_typing_speed * 9)
            await meschan.send("Confirmed. Self destruct sequence in T minus ten, nine...")


@bot.listen("on_message")
async def humor_setting_six_zero(message):

    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content.lower().strip()

        # "Let's make that sixty percent."

        if "sixty percent" in mescon or "60%" in mescon:

            await asyncio.sleep(average_typing_speed * 3)
            await meschan.send("Confirmed. Knock knock.")


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    else:
        pass


@bot.event
async def on_ready():

    print(f"{bot.user} (Deme v0.2.3-54), at your service.")  # First benchmark: 539.5 kb


@bot.listen("on_message")
async def pseudo_random_number_generator(message):

    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content

        # "Deme, can I get a random number between 000 and 000?"

        if any(name in mescon for name in names) and "random" in mescon and "?" in mescon:

            try:
                minimum_number = int(mescon[40:-8])
                maximum_number = int(mescon[48:-1])
                response = random.randint(minimum_number, maximum_number)

                await asyncio.sleep(average_typing_speed)
                await meschan.send(response)

            except TypeError as e:
                await asyncio.sleep(average_typing_speed * 8)
                await meschan.send("My system is telling me there's an Error. :eyes:")
                await meschan.send(e)

            except ValueError as e:
                await asyncio.sleep(average_typing_speed * 8)
                await meschan.send("My system is telling me there's an Error. :eyes:")
                await meschan.send(e)


@bot.listen("on_message")
async def state(message):
    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content

        # "How're you?"
        # "How you doing"

        if any(adverb in mescon for adverb in how_adverbs) and "you" in mescon:

            choice = [
                "I'm fine, I suppose. How're you?",
                "I'm well. You?",
                "Living the dream. And you?",
                "Meh, can't complain. How about yourself?"
            ]
            response = random.choice(choice)

            await asyncio.sleep(average_typing_speed * 5)
            await meschan.send(response)


@bot.listen("on_message")
async def weather(message):

    ct = datetime.datetime.now().time()
    current_formatted_time = ct.strftime("%H:%M")
    geolocator = Nominatim(user_agent="geoapiExercises")
    latitude = "LATITUDE"
    longitude = "LONGITUDE"
    location = geolocator.reverse(latitude + "," + longitude)
    address = location.raw["address"]
    city = address.get("city", "")
    WEATHER_TOKEN = "TOKEN"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "CITY"
    complete_url = base_url + "&appid=" + WEATHER_TOKEN + "&q=" + city_name + "&units=imperial"
    response = requests.get(complete_url)
    weather_list = response.json()
    y = weather_list["main"]
    current_temperature = round(y["temp"])
    z = weather_list["weather"]
    weather_description = z[0]["description"]

    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content.lower().strip()

        # Test prompt 1: "Good morning darling."
        # Test prompt 2: "Good evening, Deme."
        # Test prompt 3: "How's today's weather?"

        if mescon.startswith("good"):
            if "afternoon" in mescon:

                response = [
                    f"Good afternoon, {message.author}.",
                    f"It's {current_formatted_time}.",
                    f"The weather in {city} is {current_temperature}°F, with {weather_description}."
                ]

                for i in range(3):
                    await meschan.send(response[i])
                    await asyncio.sleep(average_typing_speed * 4.667)

            elif "day" in mescon:

                response = [
                    f"Good day, {message.author}.",
                    f"It's {current_formatted_time}.",
                    f"The weather in {city} is {current_temperature}°F, with {weather_description}."
                ]

                for i in range(3):
                    await meschan.send(response[i])
                    await asyncio.sleep(average_typing_speed * 4.667)

            elif "evening" in mescon:
                response = [
                    f"Good evening, {message.author}.",
                    f"It's {current_formatted_time}.",
                    f"The weather in {city} is {current_temperature}°F, with {weather_description}."
                ]

                for i in range(3):
                    await meschan.send(response[i])
                    await asyncio.sleep(average_typing_speed * 4.667)

            elif "morning" in mescon:
                response = [
                    f"Good morning, {message.author}.",
                    f"It's {current_formatted_time}.",
                    f"The weather in {city} is {current_temperature}°F, with {weather_description}."
                ]

                for i in range(3):
                    await meschan.send(response[i])
                    await asyncio.sleep(average_typing_speed * 4.667)

            elif "night" in mescon:
                response = [
                    f"Good night, {message.author}.",
                    f"It's {current_formatted_time}.",
                    f"The weather in {city} is {current_temperature}°F, with {weather_description}."
                ]

                for i in range(3):
                    await meschan.send(response[i])
                    await asyncio.sleep(average_typing_speed * 4.667)

        if "weather" in mescon and "what" in mescon and "?" in mescon:
            await meschan.send(f"The weather in {city} is {current_temperature}°F, with {weather_description}.")
            await asyncio.sleep(average_typing_speed * 9)


@bot.listen("on_message")
async def who_is_there(message):

    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content.lower().strip()

        # Who's there? or Who is there?

        if "?" in mescon:

            if "who" in mescon and "is" in mescon or "who's" in mescon:

                await asyncio.sleep(average_typing_speed)
                await meschan.send("Candace.")


@bot.listen("on_message")
async def within(message):

    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content

        if mescon == "Do you have a heart?" \
            or mescon == "Has anyone ever locked you out of a room?" \
            or mescon == "Where do you go to when you go within?" \
            or mescon == "Where do you go when you go within?" \
                or mescon == "Where is the place in the world you feel the safest?":
            await asyncio.sleep(average_typing_speed)
            await meschan.send("Within.")


@bot.listen("on_message")
async def within_cells_interlinked(message):

    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content

        if mescon == "A system of cells." \
                or mescon == "Did you buy a present for the person you love?":
            await asyncio.sleep(average_typing_speed * 3)
            await message.channel.send("Within cells interlinked.")

        elif mescon == "Why don't you say that three times?":
            await asyncio.sleep(average_typing_speed * 3)
            await meschan.send("Within cells interlinked.")
            await asyncio.sleep(average_typing_speed * 3)
            await meschan.send("Within cells interlinked.")
            await asyncio.sleep(average_typing_speed * 3)
            await meschan.send("Within cells interlinked.")


@bot.listen("on_message")
async def what_you_do_not_know(message):
    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content

        # Test prompt 1: "Tell me something I don't know."

        if "don't know" in mescon and "something" in mescon:

            choices = [
                commis.get_misconception(),
                randfacts.get_fact()
            ]

            response = random.choice(choices)

            await asyncio.sleep(average_typing_speed * 4)
            await meschan.send(f"How bout this: {response}")


@bot.listen("on_message")
async def you_are_welcome(message):
    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content.lower().strip()

        if any(name in mescon for name in names) \
                and any(variant in mescon for variant in thank_you_variants):

            responses = [
                f"My pleasure, {message.author}.",
                f"No problem, {message.author}.",
                f"You're welcome, {message.author}."
            ]

            emojis = [
                "🤘",
                "👍"
            ]

            emoji = random.choice(emojis)

            response = random.choice(responses)

            await message.add_reaction(emoji)
            await asyncio.sleep(average_typing_speed * 3)
            await meschan.send(response)


@bot.listen("on_message")
async def yourself_quote(message):

    if message.author != bot.user:

        meschan = message.channel
        mescon = message.content

        if any(verb in mescon for verb in define_verbs) \
            and "own" in mescon \
            and any(noun in mescon for noun in tooth_nouns) \
            and any(verb in mescon for verb in try_verbs) \
                and any(pronoun in mescon for pronoun in yourself_pronouns):

            quote = """
            Alan Watts once said, 'Trying to define yourself is like trying to bite your own teeth.'
            """

            await asyncio.sleep(average_typing_speed * 12)
            await meschan.send(quote)

bot.run("TOKEN")
