import discord
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Kamus kategori sampah
kategori_sampah = {
    'apel': 'Organik',
    'banana': 'Organik',
    'plastic bottle': 'Anorganik',
    'glass jar': 'Anorganik',
    # Tambahkan lebih banyak kategori di sini
}

@bot.command(name='sort')
async def sort_trash(ctx, *, trash_item: str):
    trash_item = trash_item.lower()
    kategori = kategori_sampah.get(trash_item, 'kategori tidak ditemukan')
    await ctx.send(f'{trash_item.capitalize()} adalah kategori {kategori}!!!, buanglah pada tempat sampah {kategori}')


bot.run("MTI2NjY5ODU3NDU5OTgxOTMxNg.GkjaxN.E8hEYRQTYxeeVMmTATV5N9f7PT1S605NJVaOHg")
