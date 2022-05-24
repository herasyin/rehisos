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

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)
client.remove_command('help')


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
	channel = client.get_channel(CHAT_ID) if member.guild.id == HERA_ID else member.guild.system_channel
	await channel.send(f'{member.mention} {random.choice(HI)}')

	# DATABASE // WELLCOME TO BIG BROTHER NOTE 🖉
	try:
		with psycopg2.connect(DATABASE_URL, sslmode='require') as database:
			cursor = database.cursor()
			cursor.execute('SELECT register FROM members WHERE discord_id = {};'.format(member.id))
			if cursor.fetchone() is None:
				cursor.execute("INSERT INTO members (name, discord_id, mention, score) VALUES ('{}', {}, '{}', 0);".format(member.name, member.id, member))
				await logit('MEMBER', client, member=member)
			else:
				await logit('MEMBER', client, member=member, cursor=cursor)
	except Exceprion as e:
		await logit('ERROR_', client, member=member, e=e)


@client.event
async def on_member_remove(member):
	channel = member.guild.system_channel
	await channel.send(f'{member} {random.choice(BYE)}')


@client.event
async def on_message(message):
	await client.process_commands(message)
	message_ = message.content.lower()
	bad_word = [u'пидор', u'педик', u'педрилла', 'pidor', u'пидорас', u'пидарас']
	for i in message_.split():
		if i in bad_word:
			await message.channel.send(u'осуждаю пидора, который это спизданул!')
			break
	black_word = ['nigger', u'нигер', u'нига', u'ниггер', u'негр', 'nigga', 'niga', 'niger']
	for i in message_.split():
		if i in black_word:
			await message.channel.send(random.choice(RACISTS_JOCKES))
			break
	dont_call_rehisos = ['rehisos', u'рехисос', 'rehisos,', u'рехисос,']
	for i in message_.split():
		if i in dont_call_rehisos and message.author.name != 'rehisos':
			fuck_off = [
				u'не поминай имя бога в суе, долбоеб.',
				u'че?',
				f'отебись, я сплю {ICON[4]}',
				f'да - это я {ICON[2]}'
			]
			await message.channel.send(random.choice(fuck_off))
			break
	lust = [u'нюдсы']
	for i in message_.split():
		if i in lust and random.choice(range(100)) > 66:
			await paint(message.channel, 'nude', time)
			break
	warrior = [u'воин']
	for i in message_.split():
		if i in warrior and random.choice(range(100)) > 66:
			await paint(message.channel, 'warr', time)
			break
	masquarade = [u'masquarade']
	if message_ in masquarade:
		await message.channel.send('Рекламный плакат телешоу **Implant Outsource**')
		time.sleep(1)
		await message.channel.send(f'{FILES_URL[0]}928076725118726164{FILES_URL[1]}22.01.04_-_23.56.01.26.png')
		time.sleep(1)
		await message.channel.send('сиськи из Индонезии, жопа из Сомали, знучит не так плохо')
	manglish = [u'англичанин']
	for i in message_.split():
		if i in manglish and random.choice(range(100)) > 33:
			await message.channel.send(f'{message.author.name}, hui\n␌')
			type_message = message.channel.last_message
			for line in TYPEMESS:				
				time.sleep(1.1) if '␀' in line else time.sleep(0)
				await type_message.edit(content=f'{message.author.name}, {line}')
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
async def help(ctx):
	await ctx.channel.purge(limit=1)
	author = ctx.message.author
	wannaplay = [f'{author.mention}, никто тебе не поможет!', HELPMESSAGE]
	await ctx.send(random.choice(wannaplay))


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
		pre_data = ' '.join((f'`{LABEL["rome"][i]} {x}`' for i, x in enumerate(value[:12])))
		await ctx.channel.send(f'{pre_data}\n{describe(value)}')
	else:
		await ctx.channel.send(f'{ICON[3]} нет данных — нет графика')


@client.command()
async def today(ctx):
	await ctx.channel.purge(limit=1)
	TODAY_TEMPLE = '⸙    🙼  **{}**\n   🙼  **{}**\n🙼  **{}**'
	date = datetime.today()
	numday = date.weekday()
	fulldate = date.strftime('%d %B %Y')
	days = {
		0: ['MOONDAY', 'TIME: TO PARTY'],
		1: ['TRUESDAY', 'TIME: НЕ СУЩЕСТВУЕТ'],
		2: ['WHENSDAY', 'TIME: HUETIME'],
		3: ['THENSDAY', 'TIME: LATE'],
		4: ['FREEDAY', 'TIME: NOT ENOUGH'],
		5: ['SATANDAY', 'TIME: GIVE A FUCK'],
		6: ['SADSDAY', 'TIME: TO DIE', 'TIME: TO CRY']
	}
	await ctx.channel.send(TODAY_TEMPLE.format(days[numday][0], fulldate.upper(), days[numday][1]))
	if numday == 6:
		message = ctx.channel.last_message
		await message.edit(content=TODAY_TEMPLE.format(days[numday][0], fulldate.upper(), days[numday][2]))


@client.command()
async def weather(ctx, *city):
	await ctx.channel.purge(limit=1)
	try:
		city = [word for word in city]
		check = [symb for symb in ''.join(city) if u'\u0400' <= symb <= u'\u04FF' or u'\u0500' <= symb <= u'\u052F']
		russian = True if len(check) != 0 else False
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
			await ctx.channel.send(f'🡶 **ERR⛶R {response.status_code}  {ICON[0]}**﹖ \
				                    ┊{ctx.author.name}, что это, блять, за город? {city}')
			message = ctx.channel.last_message
			time.sleep(2)
			await message.edit(content=f'🡶 **ERR⛶R {response.status_code}  {ICON[0]}**﹖ \
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
async def whoami(ctx):
	await ctx.channel.purge(limit=1)
	thatsyou = [
		'высокомерное уебище, который дрочит на свое отражение в зеркале.',
		'безвольная марионетка, кто как хочет - так тобой и дрочит.',
		'с ебаниной, определенно, главное не волнуйся, я щас позвоню куда надо и тебе помогут...',
		'ты просто чудо, милашка и красавчик!'
	]
	whoyouare = random.choice(thatsyou)
	await ctx.channel.send('дай подумать...')
	await ctx.channel.send('<a:loading:933335927659561070>')
	time.sleep(3)
	await ctx.channel.purge(limit=2)
	await ctx.channel.send(f'{ctx.author.name} {whoyouare}')
	if thatsyou.index(whoyouare) == 0:
		await ctx.channel.send(f'{FILES_URL[0]}928076723990458428{FILES_URL[1]}22.01.04_-_23.44.26.40.png')
	if thatsyou.index(whoyouare) == 1:
		await ctx.channel.send(f'{FILES_URL[0]}928728107106598932{FILES_URL[1]}22.01.06_-_02.17.15.49.png')
	if thatsyou.index(whoyouare) == 2:
		await ctx.channel.purge(limit=1)
		await ctx.channel.send(f'{ctx.author.name} убей их! Просто сделай это!')
		await ctx.channel.purge(limit=1)
		await ctx.channel.send(f'{ctx.author.name} у̸͎̺͕͊̐͐б̴̫̠̓̚͜е̴͙̝̦́͊͘й̵̡̻̽͌̓ и̴͚͙͑̾͊х̴͎͎̦̈́͐͛!̸̦͖͍̽̐͝ П̵̢̝͚̔̿̒р̴͓̺̦̿̚͝о̵͙͔͛̔͜͠с̵̢̢͇̒̾͠т̴͔̻͙̾̾̔о̵̻̙̽̈́͊ с̸̦̪͉͐͌̚д̸̝̘͊̈́͒е̸̡͋͜͜͠͝л̸̟͍̦͑͝͝а̴̢̞̦͐̾̕й̴͔̘̘̾̓͝ э̵̢͔̝̓͠͝т̴̻̦̝́͋о̸̼̟̝͐̈́!̵̡͔̐͌̕')
		await ctx.channel.purge(limit=1)
		await ctx.channel.send(f'{ctx.author.name} {whoyouare}')
		await ctx.channel.send(f'{FILES_URL[0]}928076725433286666{FILES_URL[1]}22.01.05_-_00.31.31.25.png')
	if thatsyou.index(whoyouare) == 3:
		await ctx.channel.purge(limit=1)
		whoyouare = random.choice(thatsyou)
		await ctx.channel.send('<a:loading:933335927659561070>')
		time.sleep(3)
		await ctx.channel.purge(limit=1)
		await ctx.channel.send(f'{ctx.author.name} {whoyouare}')
		time.sleep(1)
		if thatsyou.index(whoyouare) == 0:
			await ctx.channel.send(f'{FILES_URL[0]}928076723990458428{FILES_URL[1]}22.01.04_-_23.44.26.40.png')
		if thatsyou.index(whoyouare) == 1:
			await ctx.channel.send(f'{FILES_URL[0]}928728107106598932{FILES_URL[1]}22.01.06_-_02.17.15.49.png')
		if thatsyou.index(whoyouare) == 2:
			await ctx.channel.purge(limit=1)
			await ctx.channel.send(f'{ctx.author.name} убей их! Просто сделай это!')
			await ctx.channel.purge(limit=1)
			await ctx.channel.send(f'{ctx.author.name} ⛤у̸͎̺͕͊̐͐б̴̫̠̓̚͜е̴͙̝̦́͊͘й̵̡̻̽͌̓ и̴͚͙͑̾͊х̴͎͎̦̈́͐͛!̸̦͖͍̽̐͝ П̵̢̝͚̔̿̒р̴͓̺̦̿̚͝о̵͙͔͛̔͜͠с̵̢̢͇̒̾͠т̴͔̻͙̾̾̔о̵̻̙̽̈́͊ с̸̦̪͉͐͌̚д̸̝̘͊̈́͒е̸̡͋͜͜͠͝л̸̟͍̦͑͝͝а̴̢̞̦͐̾̕й̴͔̘̘̾̓͝ э̵̢͔̝̓͠͝т̴̻̦̝́͋о̸̼̟̝͐̈́!̵̡͔̐͌̕⛤')
			await ctx.channel.purge(limit=1)
			await ctx.channel.send(f'{ctx.author.name} {whoyouare}')
			await ctx.channel.send(f'{FILES_URL[0]}928076725433286666{FILES_URL[1]}22.01.05_-_00.31.31.25.png')
		if thatsyou.index(whoyouare) == 3:
			await ctx.channel.purge(limit=1)
			whoyouare = random.choice(thatsyou)
			await ctx.channel.send('<a:loading:933335927659561070>')
			time.sleep(3)
			await ctx.channel.purge(limit=1)
			await ctx.channel.send(f'{ctx.author.name} {whoyouare}')
			time.sleep(1)
			if thatsyou.index(whoyouare) == 0:
				await ctx.channel.send(f'{FILES_URL[0]}928076723990458428{FILES_URL[1]}22.01.04_-_23.44.26.40.png')
			if thatsyou.index(whoyouare) == 1:
				await ctx.channel.send(f'{FILES_URL[0]}928728107106598932{FILES_URL[1]}22.01.06_-_02.17.15.49.png')
			if thatsyou.index(whoyouare) == 2:
				await ctx.channel.purge(limit=1)
				await ctx.channel.send(f'{ctx.author.name} убей их! Просто сделай это!')
				await ctx.channel.purge(limit=1)
				await ctx.channel.send(f'{ctx.author.name} ⛤у̸͎̺͕͊̐͐б̴̫̠̓̚͜е̴͙̝̦́͊͘й̵̡̻̽͌̓ и̴͚͙͑̾͊х̴͎͎̦̈́͐͛!̸̦͖͍̽̐͝ П̵̢̝͚̔̿̒р̴͓̺̦̿̚͝о̵͙͔͛̔͜͠с̵̢̢͇̒̾͠т̴͔̻͙̾̾̔о̵̻̙̽̈́͊ с̸̦̪͉͐͌̚д̸̝̘͊̈́͒е̸̡͋͜͜͠͝л̸̟͍̦͑͝͝а̴̢̞̦͐̾̕й̴͔̘̘̾̓͝ э̵̢͔̝̓͠͝т̴̻̦̝́͋о̸̼̟̝͐̈́!̵̡͔̐͌̕⛤')
				await ctx.channel.purge(limit=1)
				await ctx.channel.send(f'{ctx.author.name} kill<a:redflame:786878538640130048>kill<a:yees:801342763790499840>kill<a:redflame:786878538640130048>kill')
				await ctx.channel.purge(limit=1)
				await ctx.channel.send(f'{ctx.author.name} {whoyouare}')
				await ctx.channel.send(f'{FILES_URL[0]}928076725433286666{FILES_URL[1]}22.01.05_-_00.31.31.25.png')
			if thatsyou.index(whoyouare) == 3:
				await ctx.channel.purge(limit=1)
				await ctx.channel.send('да ебанный в рот')
				await ctx.channel.send('ладно')
				await ctx.channel.send(f'{ctx.author.name} {whoyouare}')
				await ctx.channel.send(f'{FILES_URL}933299625543237652/unknown.png')


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
	await ctx.channel.send(f'{devilsbones[trow[0]]} {devilsbones[trow[1]]}')
	if not sum(throw):
		await ctx.channel.send(f'{author.mention}, {random.choice(hahaha)}')
	if sum(throw) == 10:
		await ctx.channel.send(f'{author.mention}, {random.choice(reverence)}')

@client.command()
async def fibsearchmerleabrahams(ctx):
	await ctx.channel.purge(limit=1)
	emb = discord.Embed(colour=discord.Colour.from_rgb(233, 0, 38))
	emb.set_author(name='[FIB | FPB | №1419 | Jack Heras]', icon_url=ctx.author.avatar_url)
	emb.set_thumbnail(url='https://media.discordapp.net/attachments/871746192743211018/888067721466626058/NHAcV09.png')
	emb.add_field(name='MERLE ABRAHAMS', value='file#00083041', inline=False)
	emb.add_field(name='GENDER', value='male', inline=True)
	emb.add_field(name='HIGHT', value='5′ 8″', inline=True)
	emb.add_field(name='WEIGHT', value='148 lb', inline=True)
	emb.add_field(name=u'РАССЛЕДОВАНИЕ', value=u'Дело «Бесконечных убийств» с самого начала было сраным тупиком. Из рассказов местных, мы знали кто убийца, но кроме косвенных улик ничего не было. 48 часовой допрос подозреваемого ничего не дал и мы были вынуждены его отпустить. Во время слежки он подошёл к нашей машине и назвал мать агента Томаса «жирной пиздой», поэтому агент Томас нашел у него в заднем кармане 100 грамм отборного кокса и засадили уебка в федеральную тюрьму. Тела жертв так и небыли найдены.', inline=False)
	emb.add_field(name=u'АРЕСТ', value=u'Во время задержания трижды испражнился в патрульной машине, вонь стояла, просто пиздец. Постоянно говорил, что оставил в своей машине монеты для проезда и просил отвезти к месту где огонь извергнулся в бесконечность, что бы забрать их. Зарегистрированных т/с на его имя в базе не было.', inline=False)
	emb.add_field(name=u'СМЕРТЬ', value=u'Merle Abrahams скончался в федеральной тюрьме в декабре 2004, точное время и обстоятельства смери не известны.', inline=False)
	emb.set_image(url=f'{FILES_URL[0]}888153234353586196{FILES_URL[1]}21.09.16_-_20.37.16.12.png')
	emb.set_footer(text='FEDERAL INVESTIGATION BUREAU DATABASE')
	await ctx.channel.send('произвожу поиск по имени Merle Abrahams в базе данных')
	await ctx.channel.send(ICON[-1])
	time.sleep(8)
	await ctx.channel.purge(limit=1)
	await ctx.send(embed=emb)


@client.command(aliases=['market'])
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
		arrow = {prices[-1] > prices[-2]: '🡭', prices[-1] < prices[-2]: '🡮'}
		title = f'{LABEL["RAIN"][3]} {company} {prices[-1]}{arrow[True]}\n{LABEL["RAIN"][4]} stock prices for last 12 {"months" if per == "M" else "weeks"}:\n\n'
		await ctx.channel.send(describe(prices, title, names[:12]))
	except Exception as e:
		traceback = sys.exc_info()[2]
		await logit('ERROR_', client, e=e)
		raise e.with_traceback(traceback)

@client.command()
@commands.has_permissions(administrator=True)
async def setup(ctx, flag=None):
	await ctx.channel.purge(limit=1)
	match flag:
		case '!':
			await ctx.channel.send(CODE, ''.join([f'{x}: {y}\n' for x, y in os.environ.items()], CODE))
			time.sleep(3)
			await ctx.channel.purge(limit=1)
		case None:
			await ctx.channel.send(f'today {random.choice(LABEL["RUNES"])}')
			await today(ctx)
			await ctx.channel.send('▂▂▂▂▂▂▂▂▂▂▂▂')
			time.sleep(1)
			await ctx.channel.send(f'moonday {random.choice(LABEL["RAIN"])}')
			await moonday(ctx, True)
			await ctx.channel.send('▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔')
			time.sleep(1)
			await ctx.channel.send(f'weather {random.choice(LABEL["RAIN"])}')
			await weather(ctx, 'Санкт-Петербург')
			await ctx.channel.send('▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔ ▔')
		case _:
			pass



#░░░░░░   ░░░░░  ░░░░░░░░  ░░░░░
#▒▒   ▒▒ ▒▒   ▒▒    ▒▒    ▒▒   ▒▒
#▒▒   ▒▒ ▒▒▒▒▒▒▒    ▒▒    ▒▒▒▒▒▒▒
#▓▓   ▓▓ ▓▓   ▓▓    ▓▓    ▓▓   ▓▓
#██████  ██   ██    ██    ██   ██


@client.command()
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
					await ctx.send(formater(records, random.choice(LABEL["RAIN"]), description))
				case 'PRINT':
					cursor.execute("SELECT month, {} FROM means ORDER BY register DESC LIMIT 12;".format(command))
					records = cursor.fetchall()
					names = [column[0] for column in records[::-1]]
					values = [value[1] for value in records[::-1]]
					title = f'fix\n{random.choice(LABEL["RAIN"])}\n  {command.upper()} CHART\n\n'
					await ctx.channel.send(describe(values, title, names))
				case 'HELP':
					await ctx.channel.send(HELPSQL)
				case None:
					cursor.execute("SELECT table_name, column_name FROM information_schema.columns WHERE table_schema = 'public' ORDER BY table_name;")
					description = [description[0] for description in cursor.description]
					records = cursor.fetchall()
					await ctx.channel.send(formater(records, random.choice(LABEL['CONTR']), description))
				case _:
					cursor.execute(f"{action} {command};")
					await logit('ACTION', client, action=action, command=command)
					await ctx.channel.send('{} ok'.format(ICON[random.choice((4, 7, -1))]))
	except Exception as e:
		await logit('DAFUCK', client, action=action, command=command, e=e)
		trace = sys.exc_info(e)[2]
		raise e.with_traceback(trace)


@client.command(aliases = ['pw'])
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
					decoded = decoder(sign[0], package[1])
					await ctx.channel.send('`🔏 password:`  ||{}||'.format(decoded))
					message = ctx.channel.last_message
					if decoded not in message.content:
						await ctx.channel.purge(limit=5)
					else:
						await message.delete(delay=3.0)
				case 'ADD':
					cursor.execute("INSERT INTO repository (place, signature) \
									VALUES ('{}', '{}');".format(package[0], crypter(random, package[1], package[2])))
					await ctx.channel.send('{} ok'.format(ICON[random.choice((4, 7, -1))]))
				case 'UPD':
					cursor.execute("UPDATE repository SET signature = '{}' \
									WHERE place = '{}';".format(crypter(random, package[1], package[2]), package[0]))
					await ctx.channel.send('{} ok'.format(ICON[random.choice((4, 7, -1))]))
				case 'GEN':
					generated = generator(random, package[0]) if package else generator(random)
					await ctx.channel.send('`🔏 generated:` ||{}||'.format(generated))
				case None:
					cursor.execute('SELECT place, signature FROM repository;')
					description = [description[0] for description in cursor.description]
					records = cursor.fetchall()
					await ctx.channel.send(formater(records, LABEL['CONTR'][14], description))
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
		await ctx.send(f'{ctx.author.name}, это {wrong_command} что за хуйня{ICON[0]}﹖')
		message = ctx.channel.last_message	
		time.sleep(2)
		await ctx.send(f'нет такой команды')
		await message.edit(content=f'{ctx.author.name}, это ~~{wrong_command}~~ что за хуйня{ICON[0]}﹖')
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
			ICON = str(payload.ICON)
			role = discord.utils.get(message.guild.roles, id=ROLES[ICON])
			if len([i for i in member.roles if i.id not in EXCROLES]) <= MAX_ROLES_PER_USER:
				await member.add_roles(role)
			else:
				await message.remove_reaction(payload.ICON, member)
		except Exception as e:
			await logit('ERROR_', client, member=member, e=e)


@client.event
async def on_raw_reaction_remove(payload):
	channel = client.get_channel(payload.channel_id)
	message = await channel.fetch_message(payload.message_id)
	member = discord.utils.get(message.guild.members, id=payload.user_id)
	try:
		ICON = str(payload.ICON)
		role = discord.utils.get(message.guild.roles, id=ROLES[ICON])
		await member.remove_roles(role)
	except Exception as e:
		await logit('ERROR_', client, member=member, e=e)

client.run(TOKEN)
