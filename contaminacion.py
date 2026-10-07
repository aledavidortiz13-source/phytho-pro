from discord.ext import commands
import discord
import random

# Activamos los permisos del bot
intents = discord.Intents.default()
intents.message_content = True

# Creamos el bot y usamos - como prefijo
bot = commands.Bot(command_prefix='-', intents=intents)


# Esta función avisa cuando el bot está conectado
@bot.event
async def on_ready():
    print(f'{bot.user} está en línea')


# Comando para recibir un reto ecológico
@bot.command()
async def reto(ctx, *opciones):

    # Lista de retos
    retos = [
        'Apaga las luces que no uses.',
        'Ahorra agua al bañarte.',
        'No tires basura al suelo.',
        'Usa menos plástico.',
        'Recicla tus residuos.'
    ]

    # Elegimos un reto al azar
    await ctx.send(random.choice(retos))


# Comando para recibir información sobre contaminación
@bot.command()
async def contaminacion(ctx, *actividad):

    # Lista de información
    datos = [
        'La contaminación del aire afecta a personas, animales y plantas.',
        'La basura en los ríos puede afectar a los animales.',
        'Reducir el uso de plástico ayuda al medio ambiente.',
        'Reciclar ayuda a disminuir los residuos.'
    ]

    # Elegimos un dato al azar
    await ctx.send(random.choice(datos))


# Comando que muestra los comandos disponibles
@bot.command()
async def ayuda(ctx, *mensaje):

    await ctx.send(
        '-reto: recibe un reto ecológico\n'
        '-contaminacion: recibe información ambiental\n'
        '-ayuda: muestra los comandos'
    )


# Colocamos el token de nuestro bot
token = ""

# Iniciamos el bot
bot.run(token)



