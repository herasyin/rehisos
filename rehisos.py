# сopyleft: ⌨ 2022 >>-her--> all rights not reserved

from discord.ext import commands
import discord

from datetime import datetime
import time
import random
import requests
import sys, os, json
import psycopg2
from vault import *

DATABASE_URL = os.environ['DATABASE_URL']
TOKEN = os.environ['DISCORD_TOKEN']

# from home import *  # HOME RUN


intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='.', intents=intents)


print(sys.version)

@client.event
async def on_ready():
	try:
		with psycopg2.connect(DATABASE_URL, sslmode='require') as database:
			cursor = database.cursor()
			for guild in client.guilds:
				for member in guild.members:
					cursor.execute('SELECT register FROM members WHERE discord_id = {};'.format(member.id))
					if cursor.fetchone() is None:
						try:
							cursor.execute("INSERT INTO members (name, discord_id, mention, score) VALUES ('{}', {}, '{}', 0);".format(member.name, member.id, member))
							await logit('MEMBER', client, member=member)
						except psycopg2.errors.UniqueViolation as e:
							await logit('ERROR_', client, member=member, e=e)
	except Exception as e:
		await logit('ERROR_', client, e=e)
	print('ready 2 say hui!!111')


 #░░░░░░ ░░   ░░  ░░░░░  ░░░░░░░░
#▒▒      ▒▒   ▒▒ ▒▒   ▒▒    ▒▒
#▒▒      ▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒    ▒▒
#▓▓      ▓▓   ▓▓ ▓▓   ▓▓    ▓▓
 #██████ ██   ██ ██   ██    ██


@client.event
async def on_member_join(member):
	HI = ['как же без тебя было скучно!', 'хай.',
		  'добро пожаловать!', 'ты блядь еще кто?',
		  'я ждал тебя и вот ты здесь.',
		  'ну и ава у тебя, это лечится вообще?',
		  'мне кажется, мы подружимся.']
	channel = client.get_channel(CHAT_ID) if member.guild.id == HERA_ID else member.guild.system_channel
	await channel.send(f'{member.mention} {random.choice(HI)}')

	# BIG BROTHER NOTE 🖉
	try:
		with psycopg2.connect(DATABASE_URL, sslmode='require') as database:
			cursor = database.cursor()
			cursor.execute('SELECT register FROM members WHERE discord_id = {};'.format(member.id))
			if cursor.fetchone() is None:
				cursor.execute("INSERT INTO members (name, discord_id, mention, score) VALUES ('{}', {}, '{}', 0);".format(member.name, member.id, member))
				await logit('MEMBER', client, member=member)
			else:
				await logit('MEMBER', client, member=member, cursor=cursor)
	except Exception as e:
		await logit('ERROR_', client, member=member, e=e)


@client.event
async def on_member_remove(member):
	BYE = ['откис еблан.', 'съебался в ужасе.', 'ну и пиздуй!',
	   'вышел в окно.', 'прощай, я не буду скучать.',
	   'прощай, я буду скучать.']
	channel = member.guild.system_channel
	await channel.send(f'{member} {random.choice(BYE)}')


@client.event
async def on_message(message):
	await client.process_commands(message)
	message_ = message.content.lower()
	bad_word = ['пидор', 'педик', 'педрилла', 'pidor', 'пидорас', 'пидарас']
	for i in message_.split():
		if i in bad_word:
			await message.channel.send('осуждаю пидора, который это спизданул!')
			break
	dont_call_rehisos = ['rehisos', 'рехисос', 'rehisos,', 'рехисос,']
	for i in message_.split():
		if i in dont_call_rehisos and message.author.name != 'rehisos':
			fuck_off = [
				'не поминай имя бога в суе, долбоеб.', 'че?',
				f'отебись, я сплю <:fuckyou:742675532600049704>',
				f'да - это я <:rehisos:742685931722506330>'
			]
			await message.channel.send(random.choice(fuck_off))
			break
	manglish = [u'англичанин']
	for i in message_.split():
		if i in manglish and random.choice(range(100)) > 33:
			TYPEMESS = ["hui▌\n␀", "hui\n␀",
			            "hui▌\n␀", "hui\n␀",
			            "hui▌\n␀", "hu▌\n␡",
			              "h▌\n␡", "hi▌\n␡",
				          "hi\n␀", "hi\n␛",
				        "~~hi~~\n␛"]
			await message.channel.send(f'{message.author.name}, hui\n␌')
			type_message = message.channel.last_message
			for line in TYPEMESS:
				time.sleep(1.1) if '␀' in line else time.sleep(0)
				await type_message.edit(content=f'{message.author.name}, {line}')
			await type_message.delete(delay=1.0)
			break
	masquarade = [u'paint']
	for i in message_.split():
		if i in masquarade and random.choice(range(100)) > 0:
			frames = paint()
			await message.channel.send(frames[0])
			type_message = message.channel.last_message
			for frame in frames[1:]:
				time.sleep(1)
				await type_message.edit(content=frame)
			await type_message.delete(delay=1.0)
			break

	# DATABASE // EVERY COIN HELPS ⛃⛂
	try:
		with psycopg2.connect(DATABASE_URL, sslmode='require') as database:
			cursor = database.cursor()
			cursor.execute('UPDATE members SET score = score + 1 WHERE discord_id = {};'.format(message.author.id))
	except Exception as e:
		await logit('ERROR_', client, author=message.author.name, e=e)



 #░░░░░░  ░░░░░░  ░░░    ░░░ ░░░    ░░░  ░░░░░  ░░░    ░░ ░░░░░░  ░░░░░░░
#▒▒      ▒▒    ▒▒ ▒▒▒▒  ▒▒▒▒ ▒▒▒▒  ▒▒▒▒ ▒▒   ▒▒ ▒▒▒▒   ▒▒ ▒▒   ▒▒ ▒▒
#▒▒      ▒▒    ▒▒ ▒▒ ▒▒▒▒ ▒▒ ▒▒ ▒▒▒▒ ▒▒ ▒▒▒▒▒▒▒ ▒▒ ▒▒  ▒▒ ▒▒   ▒▒ ▒▒▒▒▒▒▒
#▓▓      ▓▓    ▓▓ ▓▓  ▓▓  ▓▓ ▓▓  ▓▓  ▓▓ ▓▓   ▓▓ ▓▓  ▓▓ ▓▓ ▓▓   ▓▓      ▓▓
 #██████  ██████  ██      ██ ██      ██ ██   ██ ██   ████ ██████  ███████


@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
	await ctx.channel.purge(limit=amount + 1)


@client.command()
@commands.has_permissions(administrator=True)
async def roadmap(ctx):
	await ctx.channel.purge(limit=1)
	with open(os.path.join('texted', 'roadmap.txt'), encoding='utf-8') as road_map:
		roadmap_message = "".join(road_map.readlines())
		await ctx.channel.send(f'```{roadmap_message}```')


@client.command(aliases = ['plot', 'chart'])
async def grafic(ctx, *value):
	await ctx.channel.purge(limit=1)
	if value:
		pre_data = ' '.join((f'`{i+1:02}: {x}`' for i, x in enumerate(value[:12])))
		await ctx.channel.send(f'{pre_data}\n{describe(value)}')
	else:
		await ctx.channel.send(f'<:fuckyou:742675532600049704>',
			'нет данных — нет графика')


@client.command()
async def weather(ctx, *city):
	await ctx.channel.purge(limit=1)
	try:
		city = [word for word in city]
		check = [s for s in ''.join(city) if u'\u0400'<=s<=u'\u04FF' or
											 u'\u0500'<=s<=u'\u052F']
		russian = True if check else False
		for i in range(len(city)):
			if '-' in city[i]:
				word = city[i].split('-')
				words = []
				for w in word:
					if w.lower() != 'на':
						words.append(w.capitalize())
					else:
						words.append(w.lower())
				city[i] = '-'.join(words) if russian else ' '.join(words)
			else:
				city[i] = city[i].capitalize() if city[i].lower() != 'на' else city[i]
		city = '-'.join(city) if russian else ' '.join(city)
		url = f'http://wttr.in/{city}'
		params = {'format': '4', 'M': '', 'm': '', 'lang': 'ru'}
		response = requests.get(url, params=params)
		if response.status_code == 200:
			report = response.text.replace(': ', ':  ').replace(' 🌡️', '`🌡️').replace('m/s', 'm/s`')
			await ctx.channel.send(report)
		elif response.status_code == 404:
			await ctx.channel.send(f'🡶 **ERR⛶R {response.status_code}  <:vsrat:743399038337941527>**﹖ \
				                    ┊{ctx.author.name}, что это, блять, за город? {city}')
			message = ctx.channel.last_message
			time.sleep(2)
			await message.edit(content=f'🡶 **ERR⛶R {response.status_code}  <:vsrat:743399038337941527>**﹖ \
				                        ┊{ctx.author.name}, что это, блять, за город? ~~{city}~~')
		else:
			await ctx.channel.send(f'{ctx.author.name}, сорян, но тут ошибка **{response.status_code}**\n ')
	except requests.ConnectionError:
		await ctx.channel.send('<сетевая ошибка>')
	except Exception as e:
		await logit('ERROR_', client, e=e)


@client.command()
async def moonday(ctx, asi=False):
	await ctx.channel.purge(limit=1)
	date = datetime.today()
	year = date.year
	month = date.month
	day = date.day
	hour = date.hour
	minute = date.minute
	second = date.second
	magicdate = 2448065.4133449076  # 22.06.1990 21:55 - newmoon
	moonmonth = 29.530588853

	year_ = year + 4800 - (14 - month) // 12
	month_ = month + 12 * ((14 - month) // 12) - 3
	JDN = day + (153 * month_ + 2) // 5 + 365 * year_ + year_ // 4 - year_ // 100 + year_ // 400 - 32045
	JD = JDN + (hour - 12) / 24 + minute / 1440 + second / 86400
	moon_day = (JD - magicdate) % moonmonth
	phase = {
		            moon_day <  1.84566: "Новолуние `🌑`",            #          ▄▄▄
		 1.84566 <= moon_day <  5.53699: "Молодая луна `🌒`",         #      ▄▄▓▒██████▄
		 5.53699 <= moon_day <  9.22831: "Первая четверть `🌓`",      #    ▄█▒░▒▒▒███▓▒▓█▌
		 9.22831 <= moon_day < 12.91963: "Прибывающая луна `🌔`",     #   ▐█▒░░░▒▒▒█▓▓▒▒▓█▌
		12.91963 <= moon_day < 16.61096: "Полнолуние `🌕`",           #   █▓▒▒░▒▓▒▓██▓▒▓███
		16.61096 <= moon_day < 20.30228: "Убывающая луна `🌖`",       #   ▐██▒▓▒▒▓████▓███▌
		20.30228 <= moon_day < 23.99361: "Последняя четверть `🌗`",   #    ▀███▓▓████████▌
		23.99361 <= moon_day < 27.68493: "Старая луна `🌘`",          #      ▀▀████████▀
		            moon_day > 27.68493: "Новолуние `🌑`"             #          ▀▀▀
	}

	ekadasi = ''
	if 11.1 < moon_day < 11.9 or 26.1 < moon_day < 26.9:
		ekadasi = 'Ēkādaśi time!'
	else:
		dop = JDN + 32044
		dop_ = {
		     moon_day < 11: int(11 - moon_day),
		12 < moon_day < 26: int(26 - moon_day),
		     moon_day > 27: int(29.530588853 - moon_day + 11)
		}
		dop1 = dop + dop_[True]
		dop2 = 4 * (dop1 + 3) // 146097
		dop3 = dop1 - 146097 * dop2 // 4
		dop4 = (4 * dop3 + 3) // 1461
		dop5 = dop3 - 1461 * dop4 // 4
		dop6 = (5 * dop5 + 2) // 153
		e_day = dop5 - (153 * dop6 + 2) // 5 + 1
		e_month = dop6 + 3 - 12 * (dop6 // 10)
		e_year = 100 * dop2 + dop4 - 4800 + dop6 // 10
		ekadasi = 'Ēkādaśi: `{:02}.{:02}.{:02}`'.format(e_day, e_month, e_year)

	await ctx.channel.send(f'**DAY {round(moon_day, 1)}** • {phase[True]}')
	await ctx.channel.send(ekadasi) if asi else time.sleep(0)


@client.command()
async def bones(ctx):
	await ctx.channel.purge(limit=1)
	author = ctx.message.author
	devilsbones = [
		'<:one:930072005489868810>',
		'<:two:930072005309505617>',
		'<:three:930072005498253312>',
		'<:four:930072005124947969>',
		'<:five:930072005401800735>',
		'<:six:930072005540212756>'
	]
	throw = [random.choice(range(6)) for x in range(2)]
	hahaha = [
		u'ебать ты лох', u'две дырки, как у твоей...',
		u'хуя везунчик, может тебе в церковь сходить?',
		u'ну ничего, может в следующий раз повезет (нет)',
		u'ахахахахахах', u'лучше не ходи в казино',
		u'все хватит, кто следующий бросает?'
	]
	reverence = [u'везучий пиздюк', u'ШЕСТЁРОЧКИ!!!', u'с тобой на деньги играть не буду']
	await ctx.channel.send(f'{devilsbones[throw[0]]} {devilsbones[throw[1]]}')
	if not sum(throw):
		await ctx.channel.send(f'{author.mention}, {random.choice(hahaha)}')
	if sum(throw) == 10:
		await ctx.channel.send(f'{author.mention}, {random.choice(reverence)}')


@client.command(aliases=['market'], cog_name='1234')
async def stock(ctx, company, per='W'):
	try:
		await ctx.channel.purge(limit=1)
		company = company.upper()
		long_ = {'W': 604800, 'M': 2592000}
		url = 'http://api.bcs.ru/udfdatafeed/v1/history'
		params = {
		    'symbol': company,
		    'resolution': 'W',
		    'from': '{:.0f}'.format(time.time() - long_[per]*16),
		    'to': '{:.0f}'.format(time.time())
		}
		response = json.loads(requests.get(url, params=params).text)
		prices = [int(price) for price in response['h'][-12:]] if per == 'W' else []
		names = [time.strftime("%b", time.localtime(day)) for day in response['t'][-12:]] if per == 'W' else []
		if per == 'M':
			while len(names) < 12:
				for i, day in enumerate(response['t'][::-1]):
					if time.strftime("%b", time.localtime(day)) not in names:
						names.append(time.strftime("%b", time.localtime(day)))
						prices.append(response['h'][~i])
			names = names[::-1]
			prices = prices[::-1]
		arrow = {prices[-1] > prices[-2]: '🡭',
				 prices[-1] < prices[-2]: '🡮'}
		title = (f'🝄 {company} {prices[-1]}{arrow[True]}\n' +
			f'🝙 stock prices for last 12 {"months" if per == "M" else "weeks"}:\n\n')
		await ctx.channel.send(describe(prices, title, names[:12]))
	except Exception as e:
		traceback = sys.exc_info()[2]
		await logit('ERROR_', client, e=e)
		raise e.with_traceback(traceback)



#░░░░░░   ░░░░░  ░░░░░░░░  ░░░░░
#▒▒   ▒▒ ▒▒   ▒▒    ▒▒    ▒▒   ▒▒
#▒▒   ▒▒ ▒▒▒▒▒▒▒    ▒▒    ▒▒▒▒▒▒▒
#▓▓   ▓▓ ▓▓   ▓▓    ▓▓    ▓▓   ▓▓
#██████  ██   ██    ██    ██   ██


@client.command(hidden=True)
@commands.has_permissions(administrator=True)
async def data(ctx, action=None, *command):
	await ctx.channel.purge(limit=1)
	try:
		with psycopg2.connect(DATABASE_URL, sslmode='require') as database:
			action = action if not action else action.upper()
			command = command if not command else ' '.join(command)
			cursor = database.cursor()
			match action:
				case 'SELECT':
					cursor.execute("SELECT {};".format(command))
					description = [description[0] for description in cursor.description]
					records = cursor.fetchall()
					await ctx.send(formater(records, 'キ', description))
				case 'PRINT':
					cursor.execute("SELECT month, {} FROM means ORDER BY register DESC LIMIT 12;".format(command))
					records = cursor.fetchall()
					names = [column[0] for column in records[::-1]]
					values = [value[1] for value in records[::-1]]
					title = f'fix\n🜁\n {command.upper()} CHART\n\n'
					await ctx.channel.send(describe(values, title, names))
				case 'HELP':
					await ctx.channel.send(HELPSQL)
				case None:
					cursor.execute("SELECT table_name, column_name FROM information_schema.columns WHERE table_schema = 'public' ORDER BY table_name;")
					description = [description[0] for description in cursor.description]
					records = cursor.fetchall()
					await ctx.channel.send(formater(records, '🜁', description))
				case _:
					cursor.execute(f"{action} {command};")
					await logit('ACTION', client, action=action, command=command)
					await ctx.channel.send('<a:loading:933335927659561070> ok')
	except Exception as e:
		await logit('DAFUCK', client, action=action, command=command, e=e)
		trace = sys.exc_info(e)[2]
		raise e.with_traceback(trace)


@client.command(aliases = ['pw'], hidden=True)
@commands.has_permissions(administrator=True)
async def password(ctx, action=None, *package):
	await ctx.channel.purge(limit=1)
	try:
		with psycopg2.connect(DATABASE_URL, sslmode='require') as database:
			action = action if not action else action.upper()
			cursor = database.cursor()
			match action:
				case 'SEE':
					cursor.execute("SELECT signature FROM repository WHERE place = '{}';".format(package[0]))
					sign = cursor.fetchone()
					decoded = decoder(sign[0], ctx.guild.name)
					await ctx.channel.send('`🔏 password:`  ||{}||'.format(decoded))
					message = ctx.channel.last_message
					if decoded not in message.content:
						await ctx.channel.purge(limit=5)
					else:
						await message.delete(delay=3.0)
				case 'ADD':
					cursor.execute("INSERT INTO repository (place, signature) \
									VALUES ('{}', '{}');".format(package[0], crypter(package[1], ctx.guild.name)))
					await ctx.channel.send('<:tea:847101198308999208> ok')
				case 'UPD':
					cursor.execute("UPDATE repository SET signature = '{}' \
									WHERE place = '{}';".format(crypter(package[1], ctx.guild.name), package[0]))
					await ctx.channel.send('<:worker:791586102825582602> ok')
				case 'GEN':
					generated = generator(package[0]) if package else generator(random)
					await ctx.channel.send('`🔏 generated:` ||{}||'.format(generated))
				case None:
					cursor.execute('SELECT place, signature FROM repository;')
					description = [description[0] for description in cursor.description]
					records = cursor.fetchall()
					await ctx.channel.send(formater(records, '⸕', description))
	except Exception as e:
		await logit('ERROR_', client, e=e)


#░░░░░░░ ░░░░░░  ░░░░░░   ░░░░░░  ░░░░░░
#▒▒      ▒▒   ▒▒ ▒▒   ▒▒ ▒▒    ▒▒ ▒▒   ▒▒
#▒▒▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒    ▒▒ ▒▒▒▒▒▒
#▓▓      ▓▓   ▓▓ ▓▓   ▓▓ ▓▓    ▓▓ ▓▓   ▓▓
#███████ ██   ██ ██   ██  ██████  ██   ██


@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		wrong_command = ctx.message.content.split(' ')[0]
		await ctx.send(f'{ctx.author.name}, это {wrong_command} что за хуйня<:vsrat:743399038337941527>﹖')
		message = ctx.channel.last_message
		time.sleep(2)
		await ctx.send(f'нет такой команды')
		await message.edit(content=f'{ctx.author.name}, это ~~{wrong_command}~~ что за хуйня<:vsrat:743399038337941527>﹖')
	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'{ctx.author.name}, хуя разогнался, не указывай мне что делать!')


@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.name}, сколько удалять? в штууках')


#░░░░░░   ░░░░░░  ░░      ░░░░░░░
#▒▒   ▒▒ ▒▒    ▒▒ ▒▒      ▒▒
#▒▒▒▒▒▒  ▒▒    ▒▒ ▒▒      ▒▒▒▒▒
#▓▓   ▓▓ ▓▓    ▓▓ ▓▓      ▓▓
#██   ██  ██████  ███████ ███████


@client.event
async def on_raw_reaction_add(payload):
	if payload.message_id == POST_ID:
		channel = client.get_channel(payload.channel_id)
		message = await channel.fetch_message(payload.message_id)
		member = discord.utils.get(message.guild.members, id=payload.user_id)
		try:
			emoji = str(payload.emoji)
			role = discord.utils.get(message.guild.roles, id=ROLES[emoji])
			await member.add_roles(role)
		except Exception as e:
			await message.remove_reaction(payload.emoji, member)
			await logit('ERROR_', client, member=member, e=e)


@client.event
async def on_raw_reaction_remove(payload):
	channel = client.get_channel(payload.channel_id)
	message = await channel.fetch_message(payload.message_id)
	member = discord.utils.get(message.guild.members, id=payload.user_id)
	try:
		emoji = str(payload.emoji)
		role = discord.utils.get(message.guild.roles, id=ROLES[emoji])
		await member.remove_roles(role)
	except Exception as e:
		await logit('ERROR_', client, member=member, e=e)

client.run(TOKEN)
