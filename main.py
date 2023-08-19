import nextcord
import datetime
from datetime import datetime
import time
import os
import requests
import asyncio
from nextcord.ext import commands
from nextcord import Interaction , SlashOption
import json
import asyncio
intents = nextcord.Intents.all()
intents.members = True
ids = [1001446159065305168,]
client = commands.Bot(command_prefix='a!',intents=intents)

class buttons(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
        self.value = None
        
    
    
    @nextcord.ui.button(label='Gernel Commands', style= nextcord.ButtonStyle.blurple)  
    async def Gernel(self ,button:nextcord.ui.Button,interaction:nextcord.Interaction):
            embed=nextcord.Embed(title="Commands AllBot",description="Show commands allbot", color=0x2e42e8)
            embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/0qYaDszCG50Q7SheMA4KbtnWJGxXdKfuGt1gyISSsio/%3Fwidth%3D663%26height%3D663/https/images-ext-1.discordapp.net/external/bCvImkfFPkqZURyr-W7df3c-koWuy_Xfpp19hSjD1nA/%253Fsize%253D1024/https/cdn.discordapp.com/avatars/985925917748641852/c964f09ae06efbcfc73b601ffd266c55.png?width=622&height=622")
            embed.add_field(name="***autoreaction***", value="autoreaction add\nautoreaction list\nautoreaction remove", inline=True)
            embed.add_field(name="***autoreply***", value="autoreply add\nautoreply list\nautoreply remove", inline=True)
            embed.add_field(name='avatar',value='avatar user\navatar server')
            embed.add_field(name='autorole',value='autorole add\nautorole list\nautorole remove \nautorole toggle')
            embed.add_field(name='banner',value='banner user\n banner server',)
            embed.add_field(name="***ملاحظه***", value="لازال العديد من الأوامر لمعرفتها جميعا إتصل بالدعم", inline=False)
            await interaction.response.send_message(embed=embed , ephemeral=True)
            self.value = True
    @nextcord.ui.button(label='Fun Commands', style= nextcord.ButtonStyle.blurple) 
    async def fun(self ,button:nextcord.ui.Button,interaction:nextcord.Interaction):
        embed=nextcord.Embed(title="Fun command")
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/4St5cpJN44g29j6gff6nblHGjIzKeTEubrstRrrtO94/%3Fwidth%3D622%26height%3D622/https/images-ext-2.discordapp.net/external/0qYaDszCG50Q7SheMA4KbtnWJGxXdKfuGt1gyISSsio/%253Fwidth%253D663%2526height%253D663/https/images-ext-1.discordapp.net/external/bCvImkfFPkqZURyr-W7df3c-koWuy_Xfpp19hSjD1nA/%25253Fsize%25253D1024/https/cdn.discordapp.com/avatars/985925917748641852/c964f09ae06efbcfc73b601ffd266c55.png?width=622&height=622")
        embed.add_field(name="اسئله", value="cuttweet", inline=True)
        embed.add_field(name="اكتب بسرعه", value="/fast ", inline=True)
        embed.add_field(name="عواصم", value="/capitals", inline=True)
        embed.add_field(name="فكك", value="/fkk ", inline=True)
        embed.add_field(name="عدد الأحرف", value="/letters", inline=True)
        embed.add_field(name="رياضيات", value="/math ", inline=True)
        embed.add_field(name="جمع", value="/plural", inline=True)
        embed.add_field(name="عدد النقاط", value="/points ", inline=True)
        await interaction.response.send_message(embed=embed , ephemeral=True)
        self.value = True
    @nextcord.ui.button(label='Admin Commands', style= nextcord.ButtonStyle.red) 
    async def admin(self ,button:nextcord.ui.Button,interaction:nextcord.Interaction):
        embed=nextcord.Embed(title="Admin Command", color=0xeb181f)   
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/4St5cpJN44g29j6gff6nblHGjIzKeTEubrstRrrtO94/%3Fwidth%3D622%26height%3D622/https/images-ext-2.discordapp.net/external/0qYaDszCG50Q7SheMA4KbtnWJGxXdKfuGt1gyISSsio/%253Fwidth%253D663%2526height%253D663/https/images-ext-1.discordapp.net/external/bCvImkfFPkqZURyr-W7df3c-koWuy_Xfpp19hSjD1nA/%25253Fsize%25253D1024/https/cdn.discordapp.com/avatars/985925917748641852/c964f09ae06efbcfc73b601ffd266c55.png?width=622&height=622")
        embed.add_field(name="طرد", value="/band\nkick", inline=True)
        embed.add_field(name="active", value="activeconfig add \nactiveconfig list\n/activeconfig remove", inline=True)
        embed.add_field(name="greet", value="greet channel\ngreet message\ngreet test\ngreet time\ngreet toggle ", inline=True)
        embed.add_field(name="ملاحظه", value="اوامر الترحيب معقده قليلا إتصل بالدعم وسيقوم بتنصيبها في سرفرك", inline=True)
        embed.add_field(name='text manage' ,value='mute\ntimeout\n' , inline=True)
        embed.add_field(name='channel manage' , value='hide all\nhide channel\nunhide all\nunhide chabbel\nlock all\nlock channel\nunlock all\nlock channel')
        embed.set_footer(text="one bot in the server")
        await interaction.response.send_message(embed=embed , ephemeral=True)
        self.value = True
        
        
    
#to load the cogs from ./cogs folder
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')
  


@client.event
async def on_ready():
  print(f"{client.user} now online")

@client.command()
async def ch(ctx,url:str):
    imag = requests.get(url).content
    await client.user.edit(avatar=imag)
    await ctx.send("Done.")
    




@client.slash_command(name='ping',description='ping of bot',guild_ids=ids)
async def _ping(interaction: Interaction):
    await interaction.response.send_message(f'{round(client.latency * 1000)}/ms.' , ephemeral=True)

@client.slash_command(name='commands',description='Commands Gernal AllBot')
async def _comands(interaction: Interaction):
    view = buttons()
    embed=nextcord.Embed(title="About Bot")
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/0qYaDszCG50Q7SheMA4KbtnWJGxXdKfuGt1gyISSsio/%3Fwidth%3D663%26height%3D663/https/images-ext-1.discordapp.net/external/bCvImkfFPkqZURyr-W7df3c-koWuy_Xfpp19hSjD1nA/%253Fsize%253D1024/https/cdn.discordapp.com/avatars/985925917748641852/c964f09ae06efbcfc73b601ffd266c55.png?width=622&height=622")
    embed.add_field(name="whats AllBot", value="تم تأسيس البوت بقياده<@946105292574326824> وبمساعده <@840563268607279114>\n و فكرة البوت لاتزال هادفة إلى تحقيق نجاحات اكبر", inline=False)
    
    await interaction.response.send_message(embed=embed , view=view)
    await view.wait()


member_save = {}
timer = 120
@client.listen('on_message') 
async def anti_mention(ctx):
    # ايدي رتبة الميوت
    muteRole = nextcord.utils.get(ctx.guild.roles, id=1018105415323615322)
    # ايدي رتبة الي تستطيع الناس تمنشنك بدون تحذير من خلالها
    role = nextcord.utils.get(ctx.guild.roles, id=1018105408340099163)
    # ايديك
    member_ID = nextcord.utils.get(ctx.guild.members, id=946105292574326824)
    if ctx.mentions:
        name = ctx.mentions[0].id
        if (ctx.author.bot):
            pass
        else:
            if role in ctx.author.roles:
                pass
            else:
                if name == member_ID.id:
                    if ctx.author == member_ID:
                        pass
                    else:
                        try:
                            last_use = datetime.now() - member_save[ctx.author.id]
                        except KeyError:
                            last_use = None
                            member_save[ctx.author.id] = datetime.now()
                        if last_use is None or last_use.seconds > timer:
                            member_save[ctx.author.id] = datetime.now()
                            embed = nextcord.Embed(description=f"> **الرجاء عدم منشنتة المسؤولين الا للضرورة في حالة التكرار سيتم اعطائك ميوت** \n\n{ctx.author.mention}",color=nextcord.Color.gold())
                            await ctx.reply(embed=embed)
                        else:
                            embed = nextcord.Embed(description=f"> **تم اعطائك ميوت بسبب تكرار منشن المسؤولين** \n\n{ctx.author.mention}",color=nextcord.Color.red())
                            await ctx.reply(embed=embed)
                            await ctx.author.add_roles(muteRole)
                            await asyncio.sleep(100)
                            await ctx.author.remove_roles(muteRole)


to = 'MTE0MTY0MjQ2NDY0NjY2NDI2NA'
kn = 'D8HXhhPcsEAnXQz9ci6_x6EvWLAH3vBHh6vORw'

client.run(to + '.GYQ3S2.'+ kn)