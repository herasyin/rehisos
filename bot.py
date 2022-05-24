# -*- coding: utf-8 -*-
```
                   ▄▄▄▄▄▄▄▄▄                     
             ▄▄█████████████████▄                
          ▄████████████████████████▄▄            
       ▄██████████████████████████████▄          
     ▄██████▀▀██████████████████▀▀██████▄        
    ▄██████▌     ▀▀▀      ▀▀▀      ███████         
   ▄███████▌                       ████████     ┋   Git dungeon master branch was cleared because of TOKEN ¯\_(ツ)_/¯
  ▐████████                        ▀███████▌    ┋   
  ████████                          ████████    ┋   This is first version of rockstar momfucker discord bot REHISOS -> True;
  ███████▌                          ▐███████▌   ┋   copypaste: 99.9%
  ███████▌                          ▐███████▌   ┋   python knowlege: 0.00113549812354984322158984822
  ████████                          ████████    ┋   commends deleted: 66+
  █████████                        ▄████████    ┋   
   █████████▄▄                   ▄█████████     ┋   now should leave this commit...
    ████▄ ▀██████▄▄        ▄▄█████████████        
     █████  ▀█████          █████████████       
      ▀████▄                ▐██████████▀        
        ▀▀████████          ▐████████▀          
           ▀▀█████          ▐████▀▀             
                ▀▀           ▀▀                  
```


from __future__ import unicode_literals
import discord
from discord.ext import commands
from discord import utils
import random
import config
intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = '.', intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print('ready 4 say hui')

# JOIN/LEAVE
@client.event
async def on_member_join(member):
    channel = member.guild.system_channel
    hi = ['как же без тебя было скучно!', 'хай.', 'добро пожаловать!', 'ты блядь еще кто?', 'я ждал тебя и вот ты здесь.', 'я ждал тебя и вот ты здесь.', 'ну и ава у тебя, это лечится вообще?', 'мне кажется, мы подружимся.']
    await channel.send(f'{member.mention} ' + random.choice(hi))

@client.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    bye = ['откис еблан.', 'съебался в ужасе.', 'ну и пиздуй!', 'вышел в окно.', 'прощай, я не буду скучать.', 'прощай, я буду скучать.']
    await channel.send(f'{member.mention} ' + random.choice(bye))

# CHAT
@client.event
async def on_message(message):
	await client.process_commands(message)
	msg = message.content.lower()
	pid = [u'пидор', u'педик', u'педрилла', 'pidor', u'пидорас', u'пидарас']
	for i in msg.split():
		if i in pid:
			await message.channel.send(u'осуждаю пидора, который это спизданул!')
			break
	nig = ['nigger', u'нигер', u'нига', u'ниггер', u'негр']
	for i in msg.split():
		if i in nig:
			her1 = [u'В машине сидят негp и мексиканец. Кто за рулём? Коп.', u'Негp и мексиканец падают с небоскрёба. Кто упадёт первым? Какая разница?', u'Как узнать, что у негpа недавно был секс? Его глаза всё ещё красные от перцового балончика.', u'Как называется негp на велосипеде? Вор.', u'Почему, когда какие-либо приборы не работают - по ним бьют? С рабами это срабатывало.', u'Негp и мексиканец падают с дерева. Кто упадёт на землюпервым? Мексиканец. Негp не долетит - ему помешает верёвка.', u'Что общего между кроссовками Nice и Ку-Клукс-Кланом? Они заставляют негpов быстро бегать.', u'Как сделать так что бы негp перестал тонуть? Надо просто убрать ногу с его головы.', u'Почему негpы так плохо пахнут? Чтобы слепые их тоже могли ненавидеть.', u'Какие три самых сложных года в жизни негра? Первый класс.', u'Почему негp, когда едет в машине, закрывает все окна? Он думает, что воняет снаружи.', u'Как снять негра с дерева? Перерезать веревку.']
			await message.channel.send(random.choice(her1))
			break
	heras = [u'джек лох', u'джек гей', u'джек какашка', u'джек еблан', u'herasyin лох', u'herasyin гей', u'herasyin еблан']
	if msg in heras:
		her2 = [u'согласен!', u'соглы', u'я тоже так считаю.']
		await message.channel.send(random.choice(her2))
	rehis = ['rehisos', u'рехисос']
	for i in msg.split():
		if i in rehis:
			her3 = [u'не поминай имя бога в суе, долбоеб.', u'че?', 'отебись, я сплю <:fuckyou:742675532600049704>', 'да - это я <:rehisos:742685931722506330>']
			await message.channel.send(random.choice(her3))
			break

# COMMANDS
@client.command()

async def help(ctx, amount = 1):
	await ctx.channel.purge(limit = amount)
	author = ctx.message.author
	await ctx.send(f'{author.mention} никто тебе не поможет!')
	print (author)

@client.command()
@commands.has_permissions(administrator = True)

async def clear(ctx, amount : int):
	await ctx.channel.purge(limit = amount + 1)

@client.command()

async def whoami(ctx, amount = 1):
	await ctx.channel.purge(limit = amount)
	emb = discord.Embed(colour = discord.Colour.from_rgb(233, 0, 38) )
	author = ctx.message.author
	who = ['Сказочный Долбоеб', 'Сперма Осьминога', 'Далсуке Наротан', 'Просто Бог']
	emb.set_author(name = random.choice(who), icon_url = ctx.author.avatar_url)
	await ctx.send(embed = emb)

# ERROR
@client.event
async def on_command_error(ctx, error):
	pass

@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.name}, сколько удалять то?')

	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'{ctx.author.name}, хуя разогнался, не указывай мне что делать!')

#ROLE
@client.event
async def on_raw_reaction_add(payload):
	if payload.message_id == config.POST_ID:
		channel = client.get_channel(payload.channel_id) # получаем объект канала
		message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
		member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию

		try:
			emoji = str(payload.emoji) # эмоджик который выбрал юзер
			role = utils.get(message.guild.roles, id=config.ROLES[emoji]) # объект выбранной роли (если есть)
			if(len([i for i in member.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
				await member.add_roles(role)
				print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
			else:
				await message.remove_reaction(payload.emoji, member)
				print('[ERROR] Too many roles for user {0.display_name}'.format(member))

		except KeyError as e:
			print('[ERROR] KeyError, no role found for ' + emoji)
		except Exception as e:
			print(repr(e))
			
@client.event 
async def on_raw_reaction_remove(payload):
	channel = client.get_channel(payload.channel_id) # получаем объект канала
	message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
	member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию

	try:
		emoji = str(payload.emoji) # эмоджик который выбрал юзер
		role = utils.get(message.guild.roles, id=config.ROLES[emoji]) # объект выбранной роли (если есть)

		await member.remove_roles(role)
		print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))

	except KeyError as e:
		print('[ERROR] KeyError, no role found for ' + emoji)
	except Exception as e:
		print(repr(e))

client.run(config.TOKEN)