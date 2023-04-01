import discord
import os
import requests
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import argparse
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter







# Crie um objeto ArgumentParser
parser = argparse.ArgumentParser()

# Adicione o argumento --verbose
parser.add_argument('--verbose', action='store_true', help='Imprime informações detalhadas e de depuração durante a execução do código')

# Parse os argumentos da linha de comando
args = parser.parse_args()

# Verifique se o argumento --verbose foi passado
if args.verbose:
    print('Informações detalhadas e de depuração serão impressas durante a execução do código')


token = os.getenv('token')
API_URL = "https://api-json-zeta.vercel.app/dados.json"



# Crie um objeto bot do discord

bot = commands.Bot(command_prefix="!", help_command=None, intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.event
async def anime(message):
    if message.author == bot.user:
        return

    if message.content.startswith(name='anime'):
        # Chama a API de piadas
        response = requests.get('https://api-json-zeta.vercel.app/dados.json')

        if response.status_code == 200:
            # Exibe a piada no Discord
            data = response.json()
            await message.channel.send(f"{data['setup']}\n\n{data['punchline']}")
        else:
            await message.channel.send("Não foi possível encontrar uma piada.")






# Quando o bot estiver pronto, imprima uma mensagem no console
@bot.event
async def on_ready():
    print('Bot esta pronto')

# Comando para fazer o bot entrar em um canal de voz
@bot.command()
async def oi(ctx):
    await ctx.reply(f"Salve, aqui é o AnimesBot, prazer {ctx.author}")


#Help
@bot.command()
async def helpanime(ctx):
    animes = ['1. Attack on Titan', '2. One Piece', '3. Pokemon', '4. Naruto', '5. One Punch-Man', '6. Boku no Hero Academia', '7. Dragon Ball', '8. Classroom of the Elite', '9. DrStone', '10. GENJITSU SHUGI YUUSHA NO OUKOKU SAIKENKI', '11. Bleach']
    ordem = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    mensagem2 = "Para usar basta colocar: !animes1 ou o codigo de sua preferencia\n"
    mensagem = "Lista de animes:\n"
    for i, indice in enumerate(ordem, 1):
        mensagem += f"{i}. {animes[indice-1].split('.')[1]}\n"
    await ctx.send(f"{mensagem2}\n{mensagem}")


#Minha API
@bot.command(name='anime')
async def anime(ctx, id: int):
    response = requests.get(f"{API_URL}/{id}")
    json = response.json()

    await ctx.send(f"```html\nTitulo: {json[id]['titulo']}\n\nSobre: {json[id]['sobre']}\n\nAutor: {json[id]['autor']}\n```")






    

    



# Rode o bot
bot.run(token)