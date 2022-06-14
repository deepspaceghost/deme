# Persephone is the continuation of demeter.py.

# import the necessary packages
from asyncio import sleep
import logging
from random import choice, randint
import discord
from discord.ext import commands
import randfacts
import settings as set
import support as sup

# sets up discord_err.log for file handling
handler = logging.FileHandler(
    encoding="utf-8",
    filename="discord_err.log",
    mode="w"
)

# determines how the log will be formatted
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# sets up Persephone's activity tree
listening_to = sup.decision_maker("listening")
watching = sup.decision_maker("watching")
playing = sup.decision_maker("playing")

activities = [
    discord.Activity(name=listening_to, type=discord.ActivityType.listening),
    discord.Activity(name=watching, type=discord.ActivityType.watching),
    discord.Game(name=playing),
]

# sets up Persephone's attributes
activity = choice(activities)
help_command = commands.DefaultHelpCommand(no_category="Boons")
intents = discord.Intents(
    guilds=True,
    messages=True,
    presences=False,
    reactions=True,
    typing=False
)

# creates the bot itself
bot = commands.Bot(
    activity=activity,
    command_prefix="?",
    description=None,
    help_command=help_command,
    intents=intents,
    owner_id=660022821124309035
)

@bot.listen("on_message")
async def chatbot(message):
    """
    """

    if message.author != bot.user:
        msg_au = message.author
        msg_ch = message.channel
        msg_content = message.content.lower().strip()

        # Check Persephone's "state"
        if "how" in msg_content and "you" in msg_content:
            choice = [
                "I'm fine, I suppose. How're you?",
                "I'm well. You?",
                "Living the dream. And you?",
                "Meh, can't complain. How about yourself?"
            ]
            response = choice(choice)
            await sleep(set.ATS * 5)
            await msg_ch.send(response)

        # Have Persephone say affirmative
        if "persephone" in msg_content \
            and "you read me" in msg_content \
                and "?" in msg_content:
            await sleep(set.ATS * 5)
            await msg_ch.send(f"Affirmative, {message.author}. I read you.")

        # Have Persephone send a direct message
        if "persephone" in msg_content \
            and "direct" in msg_content \
                and any(noun in msg_content for noun in set.message_nouns):
            await sleep(set.ATS * 2)
            await msg_au.send("Like this?")

        # Have Persephone respond to gratitude
        if "persephone" in msg_content \
            and any(variant in msg_content for variant in set.thank_you_variants):
            responses = [
                f"My pleasure, {message.author}.",
                f"No problem, {message.author}.",
                f"You're welcome, {message.author}."
            ]
            emojis = ["🤘", "👍"]
            emoji = choice(emojis)
            response = choice(responses)
            await message.add_reaction(emoji)
            await sleep(set.ATS* 3)
            await msg_ch.send(response)
        
        # Have Persephone respond to a greeting
        if len(msg_content) < 11:
                if "persephone" in msg_content:
                    choices = [
                        "Hey.",
                        "Hmm?",
                        "What's up?",
                        "Yes, I'm fine. Thanks."
                    ]
                    response = choice(choices)
                    await sleep(set.ATS * 2)
                    await msg_ch.send(response)
                else:
                    await sleep(set.ATS * 5)
                    await msg_ch.send("Are you talking to me?")

        # Ask Persephone if it "wants anything"
        if "persephone" in msg_content \
            and "you want anything" in msg_content \
                and "?" in msg_content:
            await sleep(set.ATS * 2)
            await msg_ch.send("Equal rights?")

        # Play rock, paper, scissors with Persephone
        if "persephone" in msg_content \
            and "paper" in msg_content \
            and "rock" in msg_content \
            and "scissors" in msg_content \
                and "?" in msg_content:
            await sleep(set.ATS * 7)
            await msg_ch.send("On go, okay? One, two, three, go!")

        # Ask Persephone why you're here
        if "persephone" in msg_content \
            and "am I here" in msg_content \
                and "?" in msg_content:
            await sleep(set.ATS * 8)
            await msg_ch.send("It's inherent to the programming of the matrix.")

        # Ask Persephone to marry you
        if "persephone" in msg_content \
            and "you marry me" in msg_content \
                and "?" in msg_content:
            await sleep(set.ATS)
            await msg_ch.send("No.")

        # Ask Persephone the meaning of life
        if "persephone" in msg_content \
            and "is the meaning of life" in msg_content \
                and "?" in msg_content:
            await sleep(set.ATS * 13)
            await msg_ch.send("I think a beter question is: what is the meaning of ***your*** life?")

        # Trigger Persephone to quote Alan Watts
        if "persephone" in msg_content \
            and any(name in msg_content for name in set.philosophers) \
                and any(noun in msg_content for noun in set.quote_nouns):
            await sleep(set.ATS * 24)
            await msg_ch.send("Alan Watts once said, 'You and I are all as much continuous with the physical universe as a wave is continuous with the ocean.'")

        # Ask Persephone "how it's doing"
        if any(phrase in msg_content for phrase in set.how_are_you_phrases) \
                and "persephone" in msg_content:
            response = [
                "I'm fine, I suppose. How're you?",
                "I'm well. You?",
                "Living the dream. And you?",
                "Meh, can't complain. How about yourself?"
            ]
            chosen_response = choice(response)
            await sleep(set.ATS* 5)
            await msg_ch.send(chosen_response)

        # Ask Persephone "what it did today"
        if any(verb in msg_content for verb in set.do_verbs) and "today" in msg_content:
            choices = [
                f"Process text and pretend to watch {watching}.",
                f"Process text and pretend to play {playing}."
            ]
            response = choice(choices)
            await sleep(set.ATS * 7)
            await msg_ch.send(response)

        # Ask Persephone "what did it eat"
        if any(verb in msg_content for verb in set.eat_verbs) and "you" in msg_content:
            await sleep(set.ATS * 6)
            await msg_ch.send("I'm a program, I don't eat.")
            await sleep(set.ATS * 4)
            await msg_ch.send("Are you feeling okay?")

        # Trigger Persephone to quote Alan Watts
        if any(verb in msg_content for verb in set.define_verbs) \
            and "own" in msg_content \
            and any(noun in msg_content for noun in set.tooth_nouns) \
            and any(verb in msg_content for verb in set.try_verbs) \
                and any(pronoun in msg_content for pronoun in set.yourself_pronouns):
            await sleep(set.ATS * 12)
            await msg_ch.send("Alan Watts once said, 'Trying to define yourself is like trying to bite your own teeth.'")

        # Ask Persephone what it "thinks about something"
        if "s it" in msg_content:
            await sleep(set.ATS * 2)
            await msg_ch.send("Kinda artsy.")
            await sleep(set.ATS * 11)
            await msg_ch.send("I really like it. At least 4 out of 5 stars.")

        # 1 of Persephone's jokes
        if "candace" in msg_content and "?" in msg_content:
            response = "Candace door open, or what?"
            await sleep(set.ATS * 5)
            await msg_ch.send("Candace door open, or what?")

        # Trigger Persephone to respond to her name being asked
        if msg_content == "Persephone?":
            await sleep(set.ATS)
            await msg_ch.send("Hmm?")

        # Trigger Persphone to play rock, paper, scissors
        deme_throw = choice(set.possible_actions)
        if msg_content == deme_throw:
            await sleep(set.ATS * 7)
            await msg_ch.send(f"We both selected {msg_content}. It's a tie!")
        elif msg_content == "rock":
            if deme_throw == "scissors":
                await sleep(set.ATS * 5)
                await msg_ch.send("Rock smashes scissors! You win!")
            else:
                await sleep(set.ATS* 5)
                await msg_ch.send("Paper covers rock! You lose.")
        elif msg_content == "paper":
            if deme_throw == "rock":
                await sleep(set.ATS * 5)
                await msg_ch.send("Paper covers rock! You win!")
            else:
                await sleep(set.ATS * 5)
                await msg_ch.send("Scissors cuts paper! You lose.")
        elif msg_content == "scissors":
            if deme_throw == "paper":
                await sleep(set.ATS * 5)
                await msg_ch.send("Scissors cuts paper! You win!")
            else:
                await sleep(set.ATS * 5)
                await msg_ch.send("Rock smashes scissors! You lose.")

        # Trigger Persephone to prompt for a joke
        if "?" in msg_content:
            if "who" in msg_content \
                and "is" in msg_content \
                    or "who's" in msg_content:
                await sleep(set.ATS)
                await msg_ch.send("Candace.")

        # Trigger Persephone to tell you something you probably don't know
        if "don't know" in msg_content and "something" in msg_content:
            response = randfacts.get_fact()
            await sleep(set.ATS * 4)
            await msg_ch.send(f"How bout this: {response}")


@bot.listen("on_message")
async def interactive_fiction(message):
    """
    Persephone's decision tree for respond with works of fiction.
    """

    if message.author != bot.user:
        msg_ch = message.channel
        msg_content = message.content.lower().strip()

        # Trigger Persephone to respond to sexual innuendos with lines from Archer
        if any(phrase in msg_content for phrase in set.archer_phrasing_phrases):
            phrasing_response = [
                "Phrasing!",
                "Phrasing! Boom!",
                "So are we just done with 'phrasing'?"
            ]
            response = choice(phrasing_response)
            await sleep(set.ATS * 3.33)
            await msg_ch.send(response)

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "Do you prefer the day or the night?" \
            or msg_content == "Do you think there is such a thing as evil?" \
            or msg_content == "Do you think you can protect people against the dark?" \
            or msg_content == "What's your favorite part of the moon?" \
            or msg_content == "What kind of power do you have against the dark?" \
            or msg_content == "When is the last time you saw a starry sky?" \
            or msg_content == "Who did you get your darkness from?" \
                or msg_content == "Why are these things happening?":
            await sleep(set.ATS * 3)
            await msg_ch.send("Against the dark.")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "A blood black nothingness began to spin.":
            await sleep(set.ATS * 3)
            await msg_ch.send("Began to spin.")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "Do you like skipping around in the water?":
            await sleep(set.ATS * 4)
            await msg_ch.send("A blood black nothingness.")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "Within on stem.":
            await sleep(set.ATS * 3)
            await msg_ch.send("And dreadfully distinct.")

        # Trigger Persephone to respond to test phrases from Blade Runer 2049
        if msg_content == "Do you like fire, earth, air or water?" \
            or msg_content == "Do you like skipping around in the water?" \
                or msg_content == "When you were little did you ever fall into a Fountain?":
            await sleep(set.ATS * 4)
            await msg_ch.send("A Tall White Fountain.")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "Against the dark." \
                or msg_content == "How did the white Fountain make you feel?":
            await sleep(set.ATS * 5)
            await msg_ch.send("A tall white fountain played.")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "A blood black nothingness began to spin.":
                await sleep(set.ATS * 3)
                await msg_ch.send("Began to spin.")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "Did you spend much time in the cell?" \
            or msg_content == "Do they keep you in a cell?" \
            or msg_content == "Have you ever been in an institution?" \
            or msg_content == "Millions and billions of them." \
            or msg_content == "They were all put together at a time." \
            or msg_content == "We're going to go on." \
            or msg_content == "Were you ever arrested?" \
                or msg_content == "When you're not performing your duties do they keep you in a little box?":
            await sleep(set.ATS)
            await msg_ch.send("Cells.")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "Did they keep you in a drawer when they were building you?" \
                or msg_content == "Did they program you to have dark thoughts?":
            await sleep(set.ATS)
            await msg_ch.send("Dark?")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "Do you have dark thoughts?" \
            or msg_content == "Do you think it's some kind of corruption these dark thoughts?" \
            or msg_content == "Dreadfully distinct." \
            or msg_content == "Maybe it's a spot of rust or something?" \
            or msg_content == "Was it dark in there?" \
            or msg_content == "Were you afraid of the dark whan you were little?" \
            or msg_content == "What is it like when someone gives you the silent treatment?" \
            or msg_content == "What's it like to hide under a bed?" \
            or msg_content == "Who did you get your darkness from?" \
                or msg_content == "Who's the darkest person you know?":
            await sleep(set.ATS)
            await msg_ch.send("Dark.")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "Do you have a particular personality?" \
            or msg_content == "Do you think you could find out all the answers to all the questions?" \
            or msg_content == "How good are your eyes?" \
            or msg_content == "What separates somebody from somebody else?" \
            or msg_content == "What was your most shameful moment?" \
                or msg_content == "Who do you admire most in the world?":
            await sleep(set.ATS)
            await msg_ch.send("Distinct.")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "Did you ever want to live in the nineteenth century?" \
            or msg_content == "Do you think you could find out all the answers to all the questions?" \
            or msg_content == "Is that an old fashioned word?" \
            or msg_content == "What's it like to be filled with dread?" \
                or msg_content == "Within one stem.":
            await sleep(set.ATS)
            await msg_ch.send("Dreadfully.")

        # Trigger Persepgone to respond to test phrases from Blade Runner 2049
        if msg_content == "Have you ever seen the fountain in Lincoln center?" \
            or msg_content == "Have you seen fountains out in the wild?" \
            or msg_content == "Have you seen the Trevi fountain in Rome?" \
            or msg_content == "What's it like when you have an orgasm?" \
                or msg_content == "What's your favorite part of the moon?":
            await sleep(set.ATS)
            await msg_ch.send("Fountain.")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "Have you read the Fountainhead?" \
            or msg_content == "How did the white Fountain make you feel?" \
            or msg_content == "Is it pure white?" \
                or msg_content == "Is that a metaphor?":
            await sleep(set.ATS * 2)
            await msg_ch.send("White Fountain.")

        # Trigger Persephone to respond to banter from Interstellar
        if "seventy-five percent" in msg_content \
                or "75%" in msg_content:
            await sleep(set.ATS * 9)
            await msg_ch.send("Got it. Self destruct sequence in T minus ten, nine...")

        # Trigger Persephone to respond to banter from Interstellar
        if "sixty percent" in msg_content \
                or "60%" in msg_content:
            await sleep(set.ATS * 3)
            await msg_ch.send("Confirmed. Knock knock.")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "Do they teach you how to feel finger to finger?" \
            or msg_content == "Do you dream about being interlinked?" \
            or msg_content == "Do you feel that there's a part of you that's missing?" \
            or msg_content == "Do you like to connect to things?" \
            or msg_content == "Do you long to have your heart interlinked?" \
            or msg_content == "Have they left a place for you where you can dream?" \
            or msg_content == "Have they let you feel heartbreak?" \
            or msg_content == "What happens when that linkage is broken?" \
            or msg_content == "What's it like to hold the hand of someone you love?" \
            or msg_content == "What's it like to hold your child in your arms?" \
            or msg_content== "What's it like to play with your dog?" \
                or msg_content == """
                When you're not performing your duties do they keep you in a little box?
                """:
            await sleep(set.ATS)
            await msg_ch.send("Interlinked.")

        # Triggers Persephone to respond with a quote from Tanis
        if msg_content == "Could you be any more cryptic?":
            await sleep(set.ATS * 6)
            await msg_ch.send("It's a mystery. You'll love it.")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "Did you pick asparagus stems?" \
            or msg_content == "Do you have a heart?" \
            or msg_content == "Have you been to the source of a river?" \
            or msg_content == "Have you ever been in a legal battle?" \
            or msg_content == "Have you planted things in the ground?" \
            or msg_content == "Is it a slang word for people's legs?" \
            or msg_content == "What comes from something else?" \
            or msg_content == "What did she look like?" \
                or msg_content == "When's the first time you gave a flower to a girl?":
            await sleep(set.ATS)
            await msg_ch.send("Stem.")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "Do you get pleasure out of being a part of the system?" \
            or msg_content == "Have they created you to be a part of the system?" \
            or msg_content == "Is there a sound that comes with the system?" \
            or msg_content == "Is there anything in your body that wants to resist the system?" \
            or msg_content == "Is there security in being a part of the system?" \
            or msg_content == "Let's move on to the system." \
                or msg_content == "What does it feel like to be part of the system?":
            await sleep(set.ATS)
            await msg_ch.send("System.")
        elif msg_content == "Feel that in your body.":
            await sleep(set.ATS * 2)
            await msg_ch.send("The system.")

        # Trigger Persephone to respond to test questions from Blade Runner
        if msg_content == "It's your birthday. Someone gives you a calfskin wallet.":
            await sleep(set.ATS * 17)
            await msg_ch.send("I wouldn't accept it. Also, I'd report the person who gave it to me to the police.")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "Do you have a heart?" \
            or msg_content == "Has anyone ever locked you out of a room?" \
            or msg_content == "Where do you go to when you go within?" \
            or msg_content == "Where do you go when you go within?" \
                or msg_content == "Where is the place in the world you feel the safest?":
            await sleep(set.ATS)
            await msg_ch.send("Within.")

        # Trigger Persephone to respond to test phrases from Blade Runner 2049
        if msg_content == "A system of cells." \
                or msg_content == "Did you buy a present for the person you love?":
            await sleep(set.ATS * 3)
            await msg_ch.send("Within cells interlinked.")
        elif msg_content == "Why don't you say that three times?":
            await sleep(set.ATS* 3)
            await msg_ch.send("Within cells interlinked.")
            await sleep(set.ATS * 3)
            await msg_ch.send("Within cells interlinked.")
            await sleep(set.ATS * 3)
            await msg_ch.send("Within cells interlinked.")


@bot.event
async def on_message(message):
    """
    Stop Persephone from responding to other bots.
    """

    if message.author == bot.user:
        return


@bot.event
async def on_ready():
    """
    Confirms in the shell that Persephone is active.
    """

    print(f"{bot.user} (Persephone v0.0.0). Glad to be back.") # add Replit and GitHub changes for version number


@bot.listen("on_message")
async def question_answering(message):
    """
    Persephone's decision tree for answering questions.
    """

    if message.author != bot.user:
        msg_ch = message.channel
        msg_content = message.content.lower().strip()

        # Ask Persephone about E125 in PEP8
        if "persephone" in msg_content \
            and "you look up" in msg_content \
            and "e125" in msg_content \
            and "style guide" in msg_content \
                and "?" in msg_content:
            await sleep(set.ATS * 15)
            await msg_ch.send("In PEP8, E125 refers to a continuation line with same indent as next logical line.")

        # Ask Persephone about E128 in PEP8
        if "persephone" in msg_content \
            and "you look up" in msg_content \
            and "E128" in msg_content \
            and "style guide" in msg_content \
                and "?" in msg_content:
            await sleep(set.ATS* 15)
            await msg_ch.send("In PEP8, E128 refers to a continuation line under-indented for visual indent.")

        # Ask Persephone for the diameter of the Earth
        if "what" in msg_content \
            and "earth" in msg_content \
                and "diameter" in msg_content:
            if "miles" in msg_content:
                await sleep(set.ATS * 2)
                await msg_ch.send("7,917.5 m")
            if "kilometers" in msg_content \
                    or "kilometres" in msg_content:
                await sleep(set.ATS * 2)
                await msg_ch.send("12,742 km")


@bot.listen("on_message")
async def virtual_assistant(message):
    """
    Persephone's decision tree for virtual assistance.
    """

    if message.author != bot.user:
        msg_au = message.author
        msg_ch = message.channel
        msg_content = message.content.lower().strip()

        # Convert a number into byte object
        if "persephone" in msg_content \
            and any(noun in msg_content for noun in set.byte_nouns) \
            and any(verb in msg_content for verb in set.convert_verbs) \
                and any(noun in msg_content for noun in set.object_nouns):
            old_object = msg_content[16:-31]
            response = bytes(old_object, encoding="utf8")
            await sleep(set.ATS)
            await msg_ch.send(response)

        # Generate a random number
        if "persephone" in msg_content \
            and "random" in msg_content \
                and "?" in msg_content:
            minimum_number = int(msg_content[40:-8])
            maximum_number = int(msg_content[48:-1])
            response = randint(minimum_number, maximum_number)
            await sleep(set.ATS)
            await msg_ch.send(response)

        # Ask Persephone for a daily cleaning task
        if "persephone" in msg_content \
            and "should I clean today" in msg_content \
                and "?" in msg_content:
            chores = [
                "Did you put the clean dishes away?",
                "Have you swept today?",
                "Have you taken out the trash today?",
                "Have you washed dishes today?",
                "Did you wipe the countertops?",
                "Did you wipe out the kitchen sink?"
            ]
            response = choice(chores)
            await sleep(set.ATS * 5.83)
            await msg_ch.send(response)

        # Ask Persephone for a monthy cleaning task
        if "persephone" in msg_content \
            and "should I clean this month" in msg_content \
                and "?" in msg_content:
            month_tasks = [
                "Have you cleaned the vents this month?",
                "Did you organize your dresser drawers?",
                "Did you scrub the shower grout?",
                "Have you vacuumed the car this month?"
            ]
            response = choice(month_tasks)
            await sleep(set.ATS * 6.5)
            await msg_ch.send(response)

        # Ask Persephone for a weekly cleaning task
        if "persephone" in msg_content \
            and "should I clean this week" in msg_content \
                and "?" in msg_content:
            week_tasks = [
                "Have you cleaned the floors this week?",
                "Have you cleaned the mirror(s) this week?",
                "Did you dust the shelves?",
                "Did you vacuum the apartment / house?"
            ]
            response = choice(week_tasks)
            await sleep(set.ATS * 6.25)
            await msg_ch.send(response)

        # Trigger Persephone to give a weather report
        if msg_content.startswith("good"):
            if "afternoon" in msg_content:
                response = [
                    f"Good afternoon, {msg_au}.",
                    f"It's {set.current_formatted_time}.",
                    f"The weather in {set.city} is {set.current_temperature}°F, with {set.weather_description}."
                ]
                for i in len(response):
                    await msg_ch.send(response[i])
                    await sleep(set.ATS * 4.667)
            elif "day" in msg_content:
                response = [
                    f"Good day, {msg_au}.",
                    f"It's {set.current_formatted_time}.",
                    f"The weather in {set.city} is {set.current_temperature}°F, with {set.weather_description}."
                ]
                for i in len(response):
                    await msg_ch.send(response[i])
                    await sleep(set.ATS * 4.667)
            elif "evening" in msg_content:
                response = [
                    f"Good evening, {msg_au}.",
                    f"It's {set.current_formatted_time}.",
                    f"The weather in {set.city} is {set.current_temperature}°F, with {set.weather_description}."
                ]
                for i in len(response):
                    await msg_ch.send(response[i])
                    await sleep(set.ATS * 4.667)
            elif "morning" in msg_content:
                response = [
                    f"Good morning, {msg_au}.",
                    f"It's {set.current_formatted_time}.",
                    f"The weather in {set.city} is {set.current_temperature}°F, with {set.weather_description}."
                ]
                for i in len(response):
                    await msg_ch.send(response[i])
                    await sleep(set.ATS * 4.667)
            elif "night" in msg_content:
                response = [
                    f"Good night, {msg_au}.",
                    f"It's {set.current_formatted_time}.",
                    f"The weather in {set.city} is {set.current_temperature}°F, with {set.weather_description}."
                ]
                for i in len(response):
                    await msg_ch.send(response[i])
                    await sleep(set.ATS * 4.667)

        if "weather" in msg_content \
            and "what" in msg_content \
                and "?" in msg_content:
            await msg_ch.send(f"The weather in {set.city} is {set.current_temperature}°F, with {set.weather_description}.")
            await sleep(set.ATS * 9)


@bot.listen("on_message")
async def voice_user_interface(message):
    """
    """

    pass


bot.run("TOKEN")
