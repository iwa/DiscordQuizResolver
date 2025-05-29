import discord
from discord.ext import commands
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Controller as MouseController, Button
import time
import random

## LOGGER
import logging

logger = logging.getLogger("Bot")

# Create handler (e.g., console output)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# Formatter for nice output
formatter = discord.utils._ColourFormatter()
handler.setFormatter(formatter)

# Attach handler to logger
logger.addHandler(handler)
logger.propagate = False # prevent duplicate logs from root logger

## CONSTANTS
TOKEN = ''
OWNER_USER_ID = 125325519054045184  # iwa
TARGET_USER_ID = 1362130996337573978  # xilo's bot
TARGET_CHANNEL_ID = 990936529989951528  # gneral

X = 1400  # X coordinate for mouse movement
Y = 1040  # Y coordinate for mouse movement

# Initialize controllers
keyboard = KeyboardController()
mouse = MouseController()

def gui_movemouse(x, y):
    mouse.position = (x, y)

def gui_action(message):
    mouse.click(Button.left, 1)

    keyboard.type(message)

    time.sleep(random.uniform(1.2, 2.8))

    keyboard.tap(Key.enter)

def get_response(question: str) -> str:
    responses = {
        "Here at parkour civilization no one jump for the ...": "beef",
        "Les premiers seront les derniers": "paradoxe",
        "Final Fantasy VII": "cloud",
        "Je suis mort de fatigue, j'ai une montagne de devoirs": "hyperbole",
        "Quelle protéine est meilleure pour les muscles : animale ou végétale": "animale",
        "Il criait, hurlait, rugissait": "accumulation",
        "il nous a quittés": "euphémisme",
        "The Legend of Zelda": "link",
        "La mort est représentée par une femme tenant une faux": "allégorie",
        "Quelle substance bloque l’adénosine": "caféine",
        "Combien d’étapes dans un cycle de sommeil": "4",
        "Nombre de cycle de sommeil pour une longue sieste sans se dérégler": "1",
        "Metal Gear Solid": "solid snake",
        "Heureux qui, comme Ulysse...": "ellipse",
        "Un moment, une heure, un jour, une vie": "gradation",
        "Quel type de jeu vidéo propose une expérience où chaque partie est totalement isolée, sans aucune progression conservée entre les runs, et utilise un système de combat au tour par tour": "roguelike",
        "Quel genre de jeu permet d'améliorer son personnage ou débloquer du contenu permanent après chaque partie, tout en gardant une mécanique de mort permanente": "roguelite",
        "Combien d’acides aminés essentiels existe-t-il": "8",
        "Quelle vitamine est associée à l’immunité": "C",
        "God of War": "kratos",
        "Idéalement, combien d’heures faut-il dormir par nuit": "8",
        "Quelle horloge est influencée par la lumière": "horloge hormonale",
        "Quel joueur coréen professionnel de League of Legends": "faker",
        "Quel est le nom de la vitamine également connue sous le nom de rétinol": "a",
        "Je suis venu, j'ai vu, j'ai vaincu": "asyndète",
        "Les voiles au loin descendaient vers Harfleur": "synecdoque",
        "Boire un verre": "métonymie",
        "Combien de minutes dure un cycle complet en moyenne": "50",
        "Le vent sifflait dans les arbres": "personnification",
        "Quel élément naturel synchronise l’horloge biologique": "lumière",
        "Ce n’est pas mauvais du tout": "litote",
        "Parmi les gaz qui composent l'air sur Terre, quel est le gaz présent en la plus grande quantité": "azote",
        "Combien d’acides aminés essentiels existe-t-il": "8",
        "Quel métal est problématique dans les gros poissons": "mercure",
        "Quelle hormone est sécrétée après une hausse de glycémie": "insuline",
        "Rien ne se perd, rien ne se crée, tout se ...": "transforme",
        "Il était vêtu de probité candide et de lin blanc": "zeugma",
        "obscure clarté": "oxymore",
        "Cette femme est une déesse": "métaphore",
        "Quelle molécule s’accumule quand on reste éveillé": "adénosine",
        "Pourquoi boire dès le réveil": "déshydratation",
        "Je suis mort de fatigue, j'ai une montagne de devoirs": "hyperbole",
        "Ping": "pong",
        "mort, vieux capitaine, il est temps !": "apostrophe",
        "Quel est le pseudo du meilleur joueur français à Super Smash Bros Ultimate": "Glutonny",
        "il nous a quittés": "euphémisme",
    }

    for key, value in responses.items():
        if key in question:
            return value

    return ""

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=':', intents=intents, status=discord.Status.invisible)

@bot.event
async def on_ready():
    logger.info('Bot connected')

@bot.event
async def on_message(message: discord.Message):
    if message.author.id == OWNER_USER_ID:
        if message.content.startswith('!test'):
            gui_movemouse(x = X, y = Y)
            return

    if message.author.id == TARGET_USER_ID and message.channel.id == TARGET_CHANNEL_ID:
        content = message.clean_content

        response = get_response(content)

        if response:
            gui_movemouse(x = X, y = Y)
            gui_action(response)
            logger.info(f"Response: {response}")
        else:
            logger.info("No response found.")

bot.run(TOKEN)