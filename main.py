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



# Crie um objeto bot do discord

bot = commands.Bot(command_prefix="!", help_command=None, intents=discord.Intents.all())






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
@bot.command(name='animes1')
async def animes1(ctx):
    response =  requests.get('http://localhost:5000/animes')
    json = response.json()
    
    
    await ctx.send(f"```html\nTitulo: {json[0]['titulo']}\n\nSobre: {json[0]['sobre']}\n\nAutor: {json[0]['autor']}\n```")
@bot.command(name='animes2')
async def animes2(ctx):
    response =  requests.get('http://localhost:5000/animes')
    json = response.json()
    
    
    await ctx.send(f"```html\nTitulo: {json[1]['titulo']}\n\nSobre: {json[1]['sobre']}\n\nAutor: {json[1]['autor']}\n```")
@bot.command(name = 'animes3')
async def animes3(ctx):
    response =  requests.get('http://localhost:5000/animes')
    json = response.json()
    
    
    await ctx.send(f"```html\nTitulo: {json[2]['titulo']}\n\nSobre: {json[2]['sobre']}\n\nAutor: {json[2]['autor']}\n```")
@bot.command(name = 'animes4')
async def animes4(ctx):
    response =  requests.get('http://localhost:5000/animes')
    json = response.json()
    
    
    await ctx.send(f"```html\nTitulo: {json[3]['titulo']}\n\nSobre: {json[3]['sobre']}\n\nAutor: {json[3]['autor']}\n```")
@bot.command(name = 'animes5')
async def animes5(ctx):
    response =  requests.get('http://localhost:5000/animes')
    json = response.json()
    
    
    await ctx.send(f"```html\nTitulo: {json[4]['titulo']}\n\nSobre: {json[4]['sobre']}\n\nAutor: {json[4]['autor']}\n```")

@bot.command(name = 'animes6')
async def animes6(ctx):
    response =  requests.get('http://localhost:5000/animes')
    json = response.json()
    
    
    await ctx.send(f"```html\nTitulo: {json[5]['titulo']}\n\nSobre: {json[5]['sobre']}\n\nAutor: {json[5]['autor']}\n```")

@bot.command(name = 'animes7')
async def animes7(ctx):
    response =  requests.get('http://localhost:5000/animes')
    json = response.json()
    
    
    await ctx.send(f"```html\nTitulo: {json[6]['titulo']}\n\nSobre: {json[6]['sobre']}\n\nAutor: {json[6]['autor']}\n```")

@bot.command(name = 'animes8')
async def animes8(ctx):
    response =  requests.get('http://localhost:5000/animes')
    json = response.json()
    
    
    await ctx.send(f"```html\nTitulo: {json[7]['titulo']}\n\nSobre: {json[7]['sobre']}\n\nAutor: {json[7]['autor']}\n```")

@bot.command(name = 'animes9')
async def animes9(ctx):
    response =  requests.get('http://localhost:5000/animes')
    json = response.json()
    
    
    await ctx.send(f"```html\nTitulo: {json[8]['titulo']}\n\nSobre: {json[8]['sobre']}\n\nAutor: {json[8]['autor']}\n```")

@bot.command(name = 'animes10')
async def animes10(ctx):
    response =  requests.get('http://localhost:5000/animes')
    json = response.json()
    
    
    await ctx.send(f"```html\nTitulo: {json[9]['titulo']}\n\nSobre: {json[9]['sobre']}\n\nAutor: {json[9]['autor']}\n```")

@bot.command(name = 'animes11')
async def animes11(ctx):
    response =  requests.get('http://localhost:5000/animes')
    json = response.json()
    
    
    await ctx.send(f"```html\nTitulo: {json[10]['titulo']}\n\nSobre: {json[10]['sobre']}\n\nAutor: {json[10]['autor']}\n```")


    

    



# Rode o bot
bot.run(token)